#! /usr/bin/python
import os
from sys import path
from Settings.Starter import MainLoader
from Settings.Operator import *
from Modules.Menu import *
from Settings.temp import color
from Modules.Logo import *
from Settings.Changer import AnimationOff
from Settings.Changer import regenconfig

import time 

wait = time.sleep

def getconfig():
	try:
		from Settings.Config import Animation
	except Exception:
		print(color.red+'ERROR application Crashed Please Restart!'+color.nocolor)
		regenconfig()
		exit()
		
		
	else:
		print('')

#---INIT---
MainLoader.CheckOne()
from Settings.Starter import SystemOS


Systemos = SystemOS #---0 for Windows / 1 for linux / -1 is UNKOWN
#---INSTALL---
try:
	newlinecheck = 'Downloaded=True;'
	oldlinecheck = 'Downloaded=False;'
	foldercheck = open('Settings/Config.py','r')
	replacer = foldercheck.replace(oldlinecheck,newlinecheck)
	foldercheck = open('Settings/Config.py','w')
	print('DDASDASDADSDADADASDadadsaadasd')
	foldercheck.write(replacer)
	foldercheck.close()
except Exception:
	getconfig()
	# ~ filescheck = open('Settings/Config.py','r')
	# ~ if filescheck.search_text('Credits="Adel_Naim"\n'):
	print(color.green+'All Files Exists!'+color.nocolor)
	# ~ else:
		# ~ exit();
		
else:
	if Systemos == 0:
		windowsinstall()
	else:
		linuxinstall()
	filescheck = open('Settings/Config.py','a')
	filescheck.write('#! /usr/bin/python\n')
	filescheck.write('Animation=True;\n')
	filescheck.write('Downloaded=True;\n')
	filescheck.write('Credits="Adel_Naim"\n')
	
	
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
	#tools menu
	if Systemos == 0:
		#---LOGO---
		windowslogo()
		#---MENU---
		windowsmenutools()
	else:
		#---LOGO---
		linuxlogo()
		#---MENU---
		linuxmenutools()
elif ask =='98':
	os.remove('Settings/Config.py')
	wait(2)
	regetconfig()
	print(color.green+'Reset Was Completed!'+color.nocolor)
	exit()
elif ask =='99':
	AnimationOff() 
	print(color.green+'Animations Was Disabled!'+color.nocolor)
	exit()
elif ask =='0':
	exit()
	
else:
	exit()
