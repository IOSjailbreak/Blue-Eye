from Assets.Settings import *
from Builder.Thinker import *
import sys
NBApps = 0
NBApps1 = 0
NBApps = input("How Many Apps Do You Want To Start? : ")
test=int(NBApps)
NBofARGV = test-1
CheckExport = input("Use Default Export place? (Y/N)")
if CheckExport=="N" or CheckExport=="n":
	dirc = input('Where Do you want to save the file ? : ')
	print('You Choose Custom Directory!')
	ExportDefault=CheckExport
	NBApps1 = int(NBApps)
	Step2(dirc,NBApps1,launcher1_dir,launcher2_dir,launcher3_dir,launcher4_dir,launcher5_dir,launcher6_dir,launcher7_dir,launcher8_dir,launcher9_dir,launcher10_dir);
elif CheckExport=="Y" or CheckExport=="y":
	print('You Choose Default Directory!')
	ExportDefault=CheckExport
	NBApps1 = int(NBApps)
	Step1(NBApps1,launcher1_dir,launcher2_dir,launcher3_dir,launcher4_dir,launcher5_dir,launcher6_dir,launcher7_dir,launcher8_dir,launcher9_dir,launcher10_dir);
else:
	print('Error Answer!')
	exit()
