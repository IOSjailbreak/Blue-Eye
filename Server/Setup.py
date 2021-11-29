from os import system
import time

def FIRE():
	print('\033[1;31m!!!FIRING ALL SERVERS!!!!\033[0m')
	system('python ./Server/Numbers/mainnumber.py')

#--TEST--
#FIRE()
