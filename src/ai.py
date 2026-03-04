from groq import Groq
from src.onboard import filepath_str
from pathlib import Path
from os import path
from json import load
from re import sub
#client = Groq(api_key=)
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
  text=text.replace('<think>',agent_name+'thinking:')
  text=text.replace('</think>',agent_name+'thinking ended.')
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
  elif api_type=="brave":
    return os.getenv("groq_api_key")"""

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