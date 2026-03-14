from argparse import ArgumentParser
from src.ai import * 
from src.onboard import *
from sys import version
python_ver=version[0:4]

#Inspired from PicoCLaw (https://github.com/sipeed/picoclaw/)

help_str="""Usage: pyclaw <command>\nCommands:\n- onboard     Initialize pyclaw configuration\n- query     single question, single answer, exits immediately\n- chat     Continous Conversation\n- cron        Manage scheduled tasks\n- version     Show version information\n- help     Show help information"""
pyclaw_ver="0.0.2"

def main():
	parser = ArgumentParser(prog="pyclaw",description="PyClaw - A Python-based AI Assistant")
	parser.add_argument('command',type=str)
	parser.set_defaults(foo=help_str,verbose=False)
	args = parser.parse_args()
	if (args.command==None):
		print(help_str)
	if (args.command=="onboard"):
		check_onboard_already_exists()
	if (args.command=="help"):
		print(help_str)
	if (args.command=="version"):
		print(f"Pyclaw {pyclaw_ver} runs on Python {python_ver}")
	if (args.command=="chat"):
		try:
			while (True):
				prompt = input("You: ")
				if prompt in ['exit','EXIT','Exit','quit','QUIT','Quit']:
					break
				else:
					print(chat(prompt))
			print("Goodbye")
		except KeyboardInterrupt:
			print("\nGoodbye")
	if (args.command=="query"):
		prompt = input("You: ")
		print(chat(prompt))
if __name__=="__main__":
	main()