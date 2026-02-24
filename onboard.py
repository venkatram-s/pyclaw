import os,json
def check_onboard_already_exists:
	path="path"
	if (os.path.exists(path)):
		print(f"Path: {path} already esists!")
	else:
		data={"provider_name":None,"api_base":None,"model_name":None,"api_key":None,"max_tokens":None,}
		os.makedirs(path+"/.pyclaw")
		f=open(path+"/.pyclaw/config.json","a")
		Print("config folder and files are created")
		writetojson(provider_name=input("Enter provider Name: "))
		writetojson(api_base=getpass("Enter API Base URL: "))
		writetojson(model_name=input("Enter Model Name: "))
		writetojson(encrypt1(api_key=getpass("Enter API Key: "))
		writetojson(max_tokens=int(input("Enter Max Tokens: ")))
		writetojson(agent_name=int(input("Enter Agent Name [Enter to leave it blank]: ")))

		writetojson(encrypt1(getpass(ai_api_key)))
		
