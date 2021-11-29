#! /usr/bin/python
import os
from sys import path
from Settings.Starter import MainLoader
from Settings.Operator import *
from Modules.Menu import *
from Server.Setup import FIRE
from Settings.temp import color
from Modules.Logo import *
from Settings.Changer import AnimationOff
from Settings.Changer import regetconfig

import time 

wait = time.sleep

def getconfig():
	try:
		from Settings.Config import Animation
	except Exception:
		print(color.red+'ERROR application Crashed Please Restart!'+color.nocolor)
		os.remove("Settings/Config.py")
		exit()
		
		
	else:
		print('')

#---INIT---
MainLoader.CheckOne()
from Settings.Starter import SystemOS
Systemos = SystemOS #---0 for Windows / 1 for linux / -1 is UNKOWN
#---INSTALL---
try:
	filescheck = open('Settings/Config.py','x')
except Exception:
	getconfig()
	print(color.green+'All Files Exists!'+color.nocolor)
else:
	if Systemos == 0:
		windowsinstall()
	else:
		linuxinstall()
	filescheck = open('Settings/Config.py','a')
	filescheck.write('#! /usr/bin/python\n')
	filescheck.write('Animation=True;\n')
	filescheck.write('Downloaded=True;\n')
	filescheck.write('Credits="Adel_Naim"')
	
	
if Systemos == 0:
		#---LOGO---
		windowslogo()
		#---MENU---
		windowsmenu()
else:
		#---LOGO---
		linuxlogo()
		#---MENU---
		linuxmenu()
		
ask = input(color.red+'Choose Your Option : '+color.nocolor)
if ask =='1':
	FIRE()
elif ask =='98':
	os.remove('Settings/Config.py')
	wait(2)
	regetconfig()
	print(color.green+'Reset was completed!'+color.nocolor)
	exit()
elif ask =='99':
	AnimationOff() 
elif ask =='0':
	exit()
	
else:
	exit()
