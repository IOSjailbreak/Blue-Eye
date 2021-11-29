#! /usr/bin/python
import os 
import time
import sys

#Animation=True;
#Downloaded=True;
#Credits="Adel_Naim"

def AnimationOff():
	find = "Animation=True;"
	replacer = "Animation=False;"
	folder = open('Settings/Config.py','r')
	readfolder = folder.read()
	replacer = readfolder.replace(find , replacer)
	filewrite = open('Settings/Config.py','w')
	filewrite.write(replacer)

def regetconfig():
		filescheck = open('Settings/Config.py','a')
		filescheck.write('#! /usr/bin/python\n')
		filescheck.write('Animation=True;\n')
		filescheck.write('Downloaded=True;\n')
		filescheck.write('Credits="Adel_Naim"')
