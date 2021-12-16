from os import system
from Settings.temp import color
import time

def FIRE():
	print(color.red+'!!!FIRING ALL SERVERS!!!!'+color.nocolor)
	try:
		system('python ./Server/Numbers/mainnumber.py')
	except Exception:
		print(color.red+'PLEASE RUN THE APPLICATION IN APPLICATION DIRECTORY!!!!!!!!!!'+color.nocolor)
		exit()

#--TEST--
#FIRE()
