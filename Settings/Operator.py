#! /usr/bin/python
import sys
import time
import os
from Settings.temp import *
wait = time.sleep

def windowsinstall():
	words = '[!]Downloading Files'
	for char in words:
		wait(0.1)
		sys.stdout.write(char)
		sys.stdout.flush()
	print('------>All files are installed!')
	wait(0.5)
	os.system('cls')
	
def linuxinstall():
	words = color.yellow+'[!]Downloading Files...'+color.nocolor
	for char in words:
			wait(0.1)
			sys.stdout.write(char)
			sys.stdout.flush()
	print('\n')
	print('\033[1;33m[0%]Downloaded!\033[0m')
	os.system('apt-get update')
	os.system('apt-get upgrade')
	os.system('pip install --upgrade pip')
	os.system('pip install wheel')
	print('\033[1;33m[25%]Downloaded!\033[0m')
	os.system('apt-get install python')
	os.system('pkg install figlet')
	print('\033[1;33m[50%]Downloaded!\033[0m')
	os.system('pip3 install lolcat')
	os.system('pip3 install selenium')
	os.system('pip3 install undetected_chromedriver')
	print('\033[1;33m[75%]Downloaded!\033[0m')
	os.system('apt-get update')
	os.system('apt-get upgrade')
	print('\033[1;33m[100%]Downloaded!\033[0m')
	wait(0.5)
	os.system('clear')
	

#--Test_Section--
#windowsinstall()
