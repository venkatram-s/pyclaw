from pathlib import Path
from os import path,makedirs
from onboard import 
#from datetime import 


path_str=str(Path.home())+r"/.pyclaw/logs"
filepath_str=path_str+r"/config.json"

makedirs(path_str,exist_ok=True)
def logger():
	pass