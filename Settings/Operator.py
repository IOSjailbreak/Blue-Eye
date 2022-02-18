#! /usr/bin/python
#downloading is here
import sys
import time
import os
from Settings.temp import color
wait = time.sleep

def windowsinstall():
	words = color.yellow+'[!]Downloading Files...'+color.nocolor
	for char in words:
		wait(0.1)
		sys.stdout.write(char)
		sys.stdout.flush()
	print('')
	print(color.green+'[+]All files are installed!'+color.nocolor)
	os.system('python -m pip install -r requirements/requirments1.txt')
	os.system('python -m pip install -r requirements/requirments2.txt')
	os.system('python -m pip install -r requirements/requirments3.txt')
	os.system('python -m pip install -r requirements/requirments4.txt')
	wait(0.5)
	os.system('cls')
	
def linuxinstall():
	words = color.yellow+'[!]Downloading Files...'+color.nocolor
	for char in words:
			wait(0.1)
			sys.stdout.write(char)
			sys.stdout.flush()
	print('')
	print(color.yellow+'[0%]Downloaded!'+color.nocolor)
	os.system('apt-get update')
	os.system('apt-get upgrade')
	os.system('pip install --upgrade pip')
	os.system('pip install wheel')
	os.system('python3 -m pip install -r requirements/requirments1.txt')
	os.system('python3 -m pip install -r requirements/requirments2.txt')
	os.system('python3 -m pip install -r requirements/requirments3.txt')
	os.system('python3 -m pip install -r requirements/requirments4.txt')
	print(color.yellow+'[25%]Downloaded!'+color.nocolor)
	os.system('apt-get install python')
	os.system('pkg install figlet')
	print(color.yellow+'[50%]Downloaded!'+color.nocolor)
	os.system('pip3 install lolcat')
	os.system('pip3 install selenium')
	os.system('pip3 install undetected_chromedriver')
	print(color.yellow+'[75%]Downloaded!'+color.nocolor)
	os.system('apt-get update')
	os.system('apt-get upgrade')
	print(color.yellow+'[100%]Downloaded!'+color.nocolor)
	wait(0.5)
	os.system('clear')
	

#--Test_Section--
#windowsinstall()
