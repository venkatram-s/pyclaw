from pathlib import Path  
from json import dumps,load
from os import path,makedirs
from pyinputplus import inputURL,inputPassword,inputInt,inputYesNo,inputStr,inputNum

path_str=str(Path.home())+r"/.pyclaw"
filepath_str=path_str+r"/config.json"

def config_file_creator(mode):
	data=dict()
	provider_name=inputStr("Enter provider Name: ")
	data["provider_name"]=provider_name
	api_base=inputURL("Enter API Base URL: ")
	data["api_base"]=api_base
	model_name=input("Enter Model Name: ")
	data["model_name"]=model_name
	ai_api_key=inputPassword("Enter AI API Key: ")
	data["ai_api_key"]=ai_api_key
	brave_api_key=inputPassword("Enter Brave Search API Key: ")
	data["brave_api_key"]=brave_api_key
	max_tokens=inputInt("Enter Max Tokens [Click Enter for 8192]: ",default = 8192,blank=True)	
	data["max_tokens"] = 8192 if max_tokens == "" else max_tokens
	temperature= inputNum("Enter Max Tokens [Click Enter for 8192]: ",default = 0.7,blank=True)
	data["temperature"] = 0.7 if temperature == "" else temperature
	agent_name=inputStr("Enter Agent Name [Click Enter to leave it blank]: ",blank=True,default="PyClaw")
	data["agent_name"]=agent_name
	json_str=dumps(data,indent=4)
	with open(filepath_str,mode) as f:
		f.write(json_str)
	print("config folder and files have been created")

def check_onboard_already_exists():
	if (path.exists(path_str) and path.exists(filepath_str)):
		print(f"Path: {path_str} already exists!")
		opt=inputYesNo("Do you want to recreate a config.json file? (Yes / No): ")
		if (opt=="yes"):
			config_file_creator(mode="w")
		else:
			pass
	else:
		makedirs(path_str)
		config_file_creator(mode="a")

def load_config():
	data=None
	with open(filepath_str, "r") as f:
		data=load(f)
