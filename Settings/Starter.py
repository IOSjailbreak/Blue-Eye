#! /usr/bin/python
import os 
import time
import sys

SystemOS = -1 #---0 for Windows / 1 for linux / -1 is UNKOWN

#--Testing_Only--
skipdec = '0'

#Do Not Modify
wait = time.sleep

	

class MainLoader:
	def CheckOne():
		global SystemOS
		if sys.platform == 'win32' or sys.platform =='win':
			os.system('cls')
			wait(0.5)
			words = '\033[1;33m[!]Please Wait Checking OS...\033[0m'
			for char in words:
					wait(0.1)
					sys.stdout.write(char)
					sys.stdout.flush()
			wait(0.4)
			print('\033[1;32mFirst Check ✅\033[0m')
			wait(0.2)
			print('\033[1;33m[!]Windows has been detected\033[0m') #orange / 32green / 31 red
			SystemOS = 0
			wait(0.2)
			print('\033[1;32m[+]Your OS is Supported!\033[0m')
			wait(0.5)
			words = '\033[1;33m[!]Checking Files Please Wait..\033[0m'
			for char in words:
				wait(0.1)
				sys.stdout.write(char)
				sys.stdout.flush()
			print('\033[1;32mDone!\033[0m')
			wait(0.3)
			os.system('cls')
			words = '\033[1;33m[!]Loading\033[0m'
			for char in words:
				wait(0.1)
				sys.stdout.write(char)
				sys.stdout.flush()
			wait(0.4)
			print('\033[1;32mDone!\033[0m')
			os.system('cls')
		elif sys.platform == 'linux' or sys.platform == 'Linux':
			try:
				from Settings.temp import *
			except SyntaxError:
				words = '\033[1;31m[!]ERROR , You are not in launcher directory!\033[0m'
				for char in words:
					wait(0.1)
					sys.stdout.write(char)
					sys.stdout.flush()
				exit()
			os.system('clear')
			wait(0.5)
			words = '\033[1;33m[!]Please Wait Checking OS...\033[0m'
			for char in words:
					wait(0.1)
					sys.stdout.write(char)
					sys.stdout.flush()
			wait(0.4)
			print('\033[1;32mDone!\033[0m')
			wait(0.2)
			print('\033[1;33m[!]Linux has been detected\033[0m') #orange / 32green / 31 red
			SystemOS = 1
			wait(0.2)
			print('\033[1;32m[+]Your OS is Supported!\033[0m')
			wait(0.5)
			words = '\033[1;33m[!]Checking Files Please Wait..\033[0m'
			for char in words:
				wait(0.1)
				sys.stdout.write(char)
				sys.stdout.flush()
			print('\033[1;32mDone!\033[0m')
			wait(0.3)
			os.system('clear')
			words = '\033[1;33m[!]Loading\033[0m'
			for char in words:
				wait(0.1)
				sys.stdout.write(char)
				sys.stdout.flush()
			wait(0.3)
			print('\033[1;32mDone!\033[0m')
			os.system('clear')
		else:
			os.system('clear')
			wait(0.5)
			SystemOS = -1
			words = '\033[1;33m[!]Please Wait Checking OS...\033[0m'
			for char in words:
					wait(0.1)
					sys.stdout.write(char)
					sys.stdout.flush()
			wait(0.4)
			print('\033[1;32mDone!\033[0m')
			wait(0.2)
			print('\033[1;31m[x]Your OS is NOT Supported!\033[0m') #orange / 32green / 31 red
			exit()
