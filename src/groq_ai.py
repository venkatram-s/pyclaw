from groq import Groq
from src.onboard import filepath_str
from pathlib import Path
from os import path
from json import load
#client = Groq(api_key=)
def load_config():
  data=None
  if (path.exists(filepath_str)):
    with open(filepath_str, "r") as f:
      data=load(f)
  return data

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
  return chat_completion.choices[0].message.content
