#! /usr/bin/python
import os
import sys
import time
wait = time.sleep
from Settings.temp import color


def windowsmenu():
	from Settings.Config import Animation
	if Animation==True:
		words = color.yellow+'[      Menu      ]'+color.nocolor
		for char in words:
			wait(0.02)
			sys.stdout.write(char)
			sys.stdout.flush()
		print('\n')
		print('[1]Get-List')
		print('[98]Reset Files')
		print('[99]Disable-Animations')
		print(color.red+'[0]Exit'+color.nocolor)
		print('\n')
	else:
		print(color.yellow+'[      Menu      ]'+color.nocolor)
		print('\n')
		print('[1]Get-List')
		print('[98]Reset Files')
		print('[99]Disable-Animations')
		print(color.red+'[0]Exit'+color.nocolor)
		print('\n')

def linuxmenu():
	from Settings.Config import Animation
	if Animation==True:
		words = color.yellow+'[      Menu      ]'+color.nocolor
		for char in words:
			wait(0.02)
			sys.stdout.write(char)
			sys.stdout.flush()
		print('')
		print('')
		print('[1]Get-List')
		print('[98]Reset Files')
		print('[99]Disable-Animations')
		print(color.red+'[0]Exit'+color.nocolor)
		print('\n')
	else:
		print(color.yellow+'[      Menu      ]'+color.nocolor)
		print('')
		print('[1]Get-List')
		print('[98]Reset Files')
		print('[99]Disable-Animations')
		print(color.red+'[0]Exit'+color.nocolor)
		print('\n')  
		
def list():
	print(color.yellow+'[      Menu      ]'+color.nocolor)
	print('')
	print('[1]IG-Report')
	print('[2]Soon')
	print('[0]Back')
		
