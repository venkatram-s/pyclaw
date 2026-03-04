from groq import Groq
from src.onboard import filepath_str
from pathlib import Path
from os import path
from json import load,dumps
from re import sub
from requests import request

def load_config():
  data=dict()
  if (path.exists(filepath_str)):
    try:
      with open(filepath_str, "r") as f:
        data=load(f)
    except Exception as e:
      print(f"Exception: {e}")
  return data

def strip_md(text):
  #text=sub(r'(\*\*|__)(.*?)\1', r'\2',text)
  agent_name=load_config()['agent_name']
  text=text.replace('<think>',agent_name+'thinking: \n')
  text=text.replace('</think>',agent_name+'thinking ended.\n')
  text=text.replace('#','')
  text=text.replace('##','')
  text=text.replace('###','')
  text=text.replace('**','')
  text=text.replace('*','')
  text=text.replace('---','\n')
  return text


"""feature in developement
def return_api(api_type):
  if api_type=="groq":
    return os.getenv("groq_api_key")
  elif api_type=="langsearch":
    return os.getenv("langsearch_api_key")"""

def chat(message):
  config=load_config()
  client = Groq(api_key=(config['ai_api_key']))
  chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": message,
        }
    ],temperature=config['temperature'],
    max_completion_tokens=config['max_tokens'],
    model=config['model_name'])
  content = chat_completion.choices[0].message.content
  return strip_md(content)

def langsearch(query):
  langsearch_api=load_config()["langsearch_api_key"]
  payload = json.dumps({
  "query": query,
  "freshness": "noLimit",
  "summary": True,
  "count": 10})
  headers = {
  'Authorization': langsearch_api,
  'Content-Type': 'application/json'
  }
  response = requests.request("POST", url, headers=headers, data=payload)
  return response.text