#! /usr/bin/python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchWindowException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.chrome.options import Options
from os import system
import os
import time
RunOS = 0

if RunOS==0:
	hidechrome=0
	execute=0
	import undetected_chromedriver as us
else:
	hidechrome=1
	execute=1
	import undetected_chromedriver as us
opt = Options()
opt.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
if hidechrome==1:
	opt.add_argument("--headless")
	opt.add_argument("--disable-dev-shm-usage")
	opt.add_argument("--no-sandbox")
opt.add_experimental_option("prefs", { \
"profile.default_content_setting_values.media_stream_mic": 2, 
"profile.default_content_setting_values.media_stream_camera": 2,
"profile.default_content_setting_values.geolocation": 2,
"profile.default_content_setting_values.notifications": 2 })
server='Main number'
text=(server +' has been extended!')

restartstart = 0
found_connection = 0
found_account = 0
found_obs = 0
found_obs2 = 0
failed_login = 0
failed_account = 0
found_somethingweird = 0

class textnowserver:
	
	def __init__(self,email,password,number,text):
		self.email=email
		self.password=password
		self.number=number
		self.text=text
		if execute==1:
			self.driver=us.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=opt)
		elif execute==0:
			self.driver=us.Chrome(options=opt)
	def websitepage(self):
		global restartstart
		print('Checking driver...')
		driver=self.driver
		first_page='https://www.textnow.com/login'
		try:
			driver.get(first_page)
			print('******IS DETECTABLE?******')
			print(driver.execute_script('return navigator.webdriver'))
		except Exception:
			restartstart = 1
		else:
			print('Driver is found!')

	def checkconnection(self):
		driver=self.driver
		global found_connection
		print('\033[1;33;40mChecking Connection...Please wait\033[0m')
		try:
			driver.find_element_by_xpath('//span[@jsselect="heading"]')
		except  NoSuchElementException:
			print('\033[1;32;40mConnection Was Found!\033[0m')
			found_connection = 1
		except StaleElementReferenceException:
			found_connection = 0
		except ElementClickInterceptedException:
			found_connection = 0
		else:
			print('\033[1;31;40mNo Connection Was Found!\033[0m')
			found_connection =0
			
	def reload(self):
		driver=self.driver
		first_page='https://www.textnow.com/login'
		driver.get(first_page)
		time.sleep(1)
		
	def login(self,email,password):
		driver=self.driver
		global failed_login
		try:
			email_b=driver.find_element_by_xpath('//input[@name="username"]')
			pass_b=driver.find_element_by_xpath('//input[@name="password"]')
		except Exception:
			failed_login = 1
		else:
			failed_login = 0
			email_b.click()
			email_b.send_keys(email)
			time.sleep(0.25)
			pass_b.click()
			pass_b.send_keys(password)
			pass_b.send_keys(Keys.RETURN)

	def accountcheck(self):
		global found_account
		global failed_account
		print('\033[1;33;40mChecking if account is valid , Please wait...\033[0m')
		time.sleep(5)
		driver=self.driver
		try:
			driver.find_element_by_xpath('//span[@class="uikit-text uikit-text--micro uikit-text--danger"]')
		except  NoSuchElementException:
			print('\033[1;32;40mAccount Exists!\033[0m')
			found_account = 1
		except StaleElementReferenceException:
			found_account = 0
		except ElementClickInterceptedException:
			found_account = 0 
		else:
			found_account = 0
			failed_account = failed_account+1
			print('\033[1;33;40mAccount Does Not Exists! , Retrying...\033[0m')

	def accountcheck2(self):
		global found_account
		global failed_account
		print('\033[1;33;40mChecking if account is valid , Please wait...\033[0m')
		time.sleep(2)
		driver=self.driver
		try:
			driver.find_element_by_xpath('//span[@class="uikit-text uikit-text--micro uikit-text--danger"]')
		except  NoSuchElementException:
			print('\033[1;32;40mAccount Exists!\033[0m')
			found_account = 1
		except StaleElementReferenceException:
			found_account = 0
		except ElementClickInterceptedException:
			found_account = 0 
		else:
			found_account = 0
			failed_account = failed_account+1
			print('\033[1;31;40mAccount Does Not Exists! , Exiting...\033[0m')
			exit()
#                                                      #                                                      #                       STAGE2                             #                                                                   #                                                     #


	def obsremove(self):
		global found_obs
		print('\033[1;33;40mChecking if there is any obs..\033[0m')
		try:
			driver=self.driver
			closedis=driver.find_element_by_xpath('//div[@class="button js-dismissButton"]')
		except  NoSuchElementException:
			print('\033[1;32;40mNo Obs Found!\033[0m')
			found_obs = 0
		except StaleElementReferenceException:
			found_obs = 0
		except ElementClickInterceptedException:
			found_obs = 0 
		else:
			found_obs = 1
			closedis.click()
			print('\033[1;32;40mObs Found And Handled!\033[0m')
			
	def obsremove2(self):
		driver=self.driver
		try:
			driver.find_element_by_xpath('//img[@class="area-code-selection"]')
		except  NoSuchElementException:
			print('Error unable to fix!')
			found_obs2 = 0
		except StaleElementReferenceException:
			found_obs2 = 0
		except ElementClickInterceptedException:
			found_obs2 = 0 
		else:
			found_obs2 = 1
			print('You need to set up the account manually!')
			exit()

	def sendtxt(self,txt,number):
		driver=self.driver
		global found_somethingweird
		try:
			clickeventone=driver.find_element_by_xpath('//button[@id="newText"]')
		except  NoSuchElementException:
			print('...')
			found_somethingweird = 1
		else:
			found_somethingweird = 0
			clickeventone.click()
			time.sleep(0.5)
			clickeventtwo=driver.find_element_by_xpath('//input[@type="text"]')
			clickeventtwo.click()
			clickeventtwo.send_keys(number)
			clickeventtwo.send_keys(Keys.RETURN)
			time.sleep(0.5)
			clickeventthree=driver.find_element_by_xpath('//textarea[@id="text-input"]')
			clickeventthree.click()
			time.sleep(0.25)
			clickeventthree.click()
			clickeventthree.send_keys(text)
			clickeventthree.send_keys(Keys.RETURN)
			time.sleep(1)
	def closeall(self):
		time.sleep(5)
		driver=self.driver
		driver.close()
		
	def done(self):
		print(server + ' Has Finished! :D')
		print('')
		exit()
		
	def getmessage(self):
		driver=self.driver
		driver.get('https://www.textnow.com/messaging')

if __name__=="__main__":
	print('')
	email='iosjailbreak541@gmail.com'
	password='password1234'
	print('Account email is : '+email)
	print('Account password is : '+password)
	print('============================================')
	print('Server : ')
	number='921212323123213'
	textnow=textnowserver(email,password,number,text)
	textnow.websitepage()
	if restartstart ==1:
		textnow=textnowserver(email,password,number,text)
		textnow.websitepage()
	else:
		textnow.checkconnection()
		while found_connection == 0:
			textnow.reload()
			textnow.checkconnection()
		if found_connection == 1:
			textnow.login(email,password)
			textnow.accountcheck()
			if found_account == 1:
				time.sleep(14)
				textnow.obsremove()
				if found_obs == 1:
					time.sleep(0.5)
					textnow.sendtxt(text,number)
					textnow.closeall()
					textnow.done()
				if found_obs ==0:
					textnow.obsremove2()
					if found_obs2 ==0:
						textnow.getmessage()
						time.sleep(16)
						textnow.obsremove()
						if found_obs == 1:
							time.sleep(0.5)
							textnow.sendtxt(text,number)
							textnow.closeall()
							textnow.done()
			if failed_account == 1:
				textnow.closeall()
				time.sleep(1)
				textnow=textnowserver(email,password,number,text)
				textnow.websitepage()
				if restartstart  ==1:
					textnow=textnowserver(email,password,number,text)
					textnow.websitepage()
				else:
					textnow.checkconnection()
					while found_connection == 0:
						textnow.reload()
						textnow.checkconnection()
					if found_connection == 1:
						textnow.login(email,password)
						textnow.accountcheck2()
						if found_account == 1:
							time.sleep(14)
							textnow.obsremove()
							if found_obs == 1:
								time.sleep(0.5)
								textnow.sendtxt(text,number)
								textnow.closeall()
								textnow.done()
							if found_obs ==0:
								textnow.obsremove2()
								if found_obs2 ==0:
									textnow.getmessage()
									time.sleep(16)
									textnow.obsremove()
									if found_obs == 1:
										time.sleep(0.5)
										textnow.sendtxt(text,number)
										textnow.closeall()
										textnow.done()


