from os import sys
import os

def Step1(NBApps1,launcher1_dir,launcher2_dir,launcher3_dir,launcher4_dir,launcher5_dir,launcher6_dir,launcher7_dir,launcher8_dir,launcher9_dir,launcher10_dir):
	# ~ global launcher1_dir
	# ~ global launcher2_dir
	# ~ global launcher3_dir
	# ~ global launcher4_dir
	# ~ global launcher5_dir
	# ~ global launcher6_dir
	# ~ global launcher7_dir
	# ~ global launcher8_dir
	# ~ global launcher9_dir
	# ~ global launcher10_dir
	test1 = int(NBApps1)
	test2 = test1+1
	if NBApps1 <= 10:
		loader = open('Exported/loader.bat','w')
		loader.write('@echo off')
		for x in range (1,test2):
			text = str(x)
			if x==1:
				if launcher1_dir=="":
					fixer1 = input("Error in launcher "+text+" Please add the directory here : ")
					launcher1_dir=fixer1
					loader.write("\n")
					loader.write('start '+launcher1_dir)
				else:
					loader.write("\n")
					loader.write('start '+launcher1_dir)
			if x==2:
				if launcher2_dir=="":
					fixer2 = input("Error in launcher "+text+" Please add the directory here : ")
					launcher2_dir=fixer2
					loader.write("\n")
					loader.write('start '+launcher2_dir)
				else:
					loader.write("\n")
					loader.write('start '+launcher2_dir)
			if x==3:
				if launcher3_dir=="":
					fixer3 = input("Error in launcher "+text+" Please add the directory here : ")
					launcher3_dir=fixer3
					loader.write("\n")
					loader.write('start '+launcher3_dir)
				else:
					loader.write("\n")
					loader.write('start '+launcher3_dir)
			if x==4:
				if launcher4_dir=="":
					fixer4 = input("Error in launcher "+text+" Please add the directory here : ")
					launcher4_dir=fixer4
					loader.write("\n")
					loader.write('start '+launcher4_dir)
				else:
					loader.write("\n")
					loader.write('start '+launcher4_dir)
			if x==5:
				if launcher5_dir=="":
					fixer5 = input("Error in launcher "+text+" Please add the directory here : ")
					launcher5_dir=fixer5
					loader.write("\n")
					loader.write('start '+launcher5_dir)
				else:
					loader.write("\n")
					loader.write('start '+launcher5_dir)
			if x==6:
				if launcher6_dir=="":
					fixer6 = input("Error in launcher "+text+" Please add the directory here : ")
					launcher6_dir=fixer6
					loader.write("\n")
					loader.write('start '+launcher6_dir)
				else:
					loader.write("\n")
					loader.write('start '+launcher6_dir)
			if x==7:
				if launcher7_dir=="":
					fixer7 = input("Error in launcher "+text+" Please add the directory here : ")
					launcher7_dir=fixer7
					loader.write("\n")
					loader.write('start '+launcher7_dir)
				else:
					loader.write("\n")
					loader.write('start '+launcher7_dir)
			if x==8:
				if launcher8_dir=="":
					fixer8 = input("Error in launcher "+text+" Please add the directory here : ")
					launcher8_dir=fixer8
					loader.write("\n")
					loader.write('start '+launcher8_dir)
				else:
					loader.write("\n")
					loader.write('start '+launcher8_dir)
			if x==9:
				if launcher9_dir=="":
					fixer9 = input("Error in launcher "+text+" Please add the directory here : ")
					launcher9_dir=fixer9
					loader.write("\n")
					loader.write('start '+launcher9_dir)
				else:
					loader.write("\n")
					loader.write('start '+launcher9_dir)
			if x==10:
				if launcher10_dir=="":
					fixer10 = input('Error in launcher '+text+' Please add the directory here : ')
					launcher10_dir=fixer10
					loader.write("\n")
					loader.write('start '+launcher10_dir)
				else:
					loader.write("\n")
					loader.write('start '+launcher10_dir)
	else:
		print('A lot of Apps!')
		
def Step2(dirc,NBApps1,launcher1_dir,launcher2_dir,launcher3_dir,launcher4_dir,launcher5_dir,launcher6_dir,launcher7_dir,launcher8_dir,launcher9_dir,launcher10_dir):
	# ~ global launcher1_dir
	# ~ global launcher2_dir
	# ~ global launcher3_dir
	# ~ global launcher4_dir
	# ~ global launcher5_dir
	# ~ global launcher6_dir
	# ~ global launcher7_dir
	# ~ global launcher8_dir
	# ~ global launcher9_dir
	# ~ global launcher10_dir
	test1 = int(NBApps1)
	test2 = test1+1
	if NBApps1 <= 10:
		print(dirc)
		loader = open(dirc+'\loader.bat','w')
		loader.write('@echo off')
		for x in range (1,test2):
			text = str(x)
			if x==1:
				if launcher1_dir=="":
					fixer1 = input("Error in launcher "+text+" Please add the directory here : ")
					launcher1_dir=fixer1
					loader.write("\n")
					loader.write('start '+launcher1_dir)
				else:
					loader.write("\n")
					loader.write('start '+launcher1_dir)
			if x==2:
				if launcher2_dir=="":
					fixer2 = input("Error in launcher "+text+" Please add the directory here : ")
					launcher2_dir=fixer2
					loader.write("\n")
					loader.write('start '+launcher2_dir)
				else:
					loader.write("\n")
					loader.write('start '+launcher2_dir)
			if x==3:
				if launcher3_dir=="":
					fixer3 = input("Error in launcher "+text+" Please add the directory here : ")
					launcher3_dir=fixer3
					loader.write("\n")
					loader.write('start '+launcher3_dir)
				else:
					loader.write("\n")
					loader.write('start '+launcher3_dir)
			if x==4:
				if launcher4_dir=="":
					fixer4 = input("Error in launcher "+text+" Please add the directory here : ")
					launcher4_dir=fixer4
					loader.write("\n")
					loader.write('start '+launcher4_dir)
				else:
					loader.write("\n")
					loader.write('start '+launcher4_dir)
			if x==5:
				if launcher5_dir=="":
					fixer5 = input("Error in launcher "+text+" Please add the directory here : ")
					launcher5_dir=fixer5
					loader.write("\n")
					loader.write('start '+launcher5_dir)
				else:
					loader.write("\n")
					loader.write('start '+launcher5_dir)
			if x==6:
				if launcher6_dir=="":
					fixer6 = input("Error in launcher "+text+" Please add the directory here : ")
					launcher6_dir=fixer6
					loader.write("\n")
					loader.write('start '+launcher6_dir)
				else:
					loader.write("\n")
					loader.write('start '+launcher6_dir)
			if x==7:
				if launcher7_dir=="":
					fixer7 = input("Error in launcher "+text+" Please add the directory here : ")
					launcher7_dir=fixer7
					loader.write("\n")
					loader.write('start '+launcher7_dir)
				else:
					loader.write("\n")
					loader.write('start '+launcher7_dir)
			if x==8:
				if launcher8_dir=="":
					fixer8 = input("Error in launcher "+text+" Please add the directory here : ")
					launcher8_dir=fixer8
					loader.write("\n")
					loader.write('start '+launcher8_dir)
				else:
					loader.write("\n")
					loader.write('start '+launcher8_dir)
			if x==9:
				if launcher9_dir=="":
					fixer9 = input("Error in launcher "+text+" Please add the directory here : ")
					launcher9_dir=fixer9
					loader.write("\n")
					loader.write('start '+launcher9_dir)
				else:
					loader.write("\n")
					loader.write('start '+launcher9_dir)
			if x==10:
				if launcher10_dir=="":
					fixer10 = input('Error in launcher '+text+' Please add the directory here : ')
					launcher10_dir=fixer10
					loader.write("\n")
					loader.write('start '+launcher10_dir)
				else:
					loader.write("\n")
					loader.write('start '+launcher10_dir)
	else:
		print('A lot of Apps!')
