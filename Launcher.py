#! /usr/bin/python
import os
from sys import path
from Settings.Starter import MainLoader
from Settings.Operator import *
from Modules.Logo import *
from Modules.Menu import *
from Server.Setup import FIRE

#---Settings---
Download = 0

#---INIT---
MainLoader.CheckOne()
from Settings.Starter import SystemOS
Systemos = SystemOS #---0 for Windows / 1 for linux / -1 is UNKOWN
#---INSTALL---
try:
	filescheck = open('Settings/Config.cfg','x')
except Exception:
	Download = 0
	print('\033[1;32mAll Files Exists\033[0m')
else:
	if Systemos == 0:
		windowsinstall()
	else:
		linuxinstall()
	filescheck = open('Settings/Config.cfg','w')
	filescheck.write('Program Was Installed!, Do not Delete This File or The Setup Will be restart!')
	
		
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
		
ask = input('Choose Your Option : ')
if ask =='1':
	FIRE()
elif ask =='0':
	exit()
else:
	exit()
