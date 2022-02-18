from Assets.Settings import *
from Builder.Thinker import *
from os import sys
import os
import time
PAUSE = time.sleep
# ~ SETTINGS DO NOT EDIT
NBApps = 0
NBApps1 = 0
os.system('cls')
NBApps = input("How Many Apps Do You Want To Start? : ")
test=int(NBApps)
NBofARGV = test-1
# ~ SETTINGS DO NOT EDIT



CheckExport = input("Use Default Export place? (Y/N)")
if CheckExport=="N" or CheckExport=="n":
	word = 'You Choose Custom Directory!'
	for char in word:
		PAUSE(0.05)
		sys.stdout.write(char)
		sys.stdout.flush()
	PAUSE(1)
	os.system('cls')
	dirc = input('Where Do you want to save the file ? : ')
	os.system('cls')
	PAUSE(1)
	os.system('cls')
	ExportDefault=CheckExport
	NBApps1 = int(NBApps)
	Step2(dirc,NBApps1,launcher1_dir,launcher2_dir,launcher3_dir,launcher4_dir,launcher5_dir,launcher6_dir,launcher7_dir,launcher8_dir,launcher9_dir,launcher10_dir);
elif CheckExport=="Y" or CheckExport=="y":
	os.system('cls')
	word = 'You Choose Default Directory!'
	for char in word:
		PAUSE(0.05)
		sys.stdout.write(char)
		sys.stdout.flush()
	PAUSE(1)
	os.system('cls')
	ExportDefault=CheckExport
	NBApps1 = int(NBApps)
	Step1(NBApps1,launcher1_dir,launcher2_dir,launcher3_dir,launcher4_dir,launcher5_dir,launcher6_dir,launcher7_dir,launcher8_dir,launcher9_dir,launcher10_dir);
else:
	print('Error Answer!')
	exit()
