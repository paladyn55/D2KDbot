from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
options = Options()
#options.headless = True
import os
driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), service_log_path=os.devnull, options=options)
from selenium.webdriver.common.by import By
def run():
	name_xp = '/html/body/div[1]/div[2]/div[2]/div/main/div[2]/div[1]/div[2]/div[2]/div[2]/span/span[1]'
	num_xp = '/html/body/div[1]/div[2]/div[2]/div/main/div[2]/div[1]/div[2]/div[2]/div[2]/span/span[2]'
	names = (open('DiscName.txt', 'r')).readlines()
	nums = (open('D2Tpage.txt', 'r')).readlines()
	
	usr_arr = []
	for i in range(len(names)):
		temp = []
		temp.append(names[i].strip('\n'))
		temp.append(nums[i].strip('\n'))
		usr_arr.append(temp)
		print(temp)
	print(usr_arr)
	for usr in usr_arr:
		url_DTR = "https://destinytracker.com/destiny-2/profile/bungie/" + usr[1] + "/overview"
		driver.get(url_DTR)
		b_name = (driver.find_element(By.XPATH, name_xp).text)
		b_num = (driver.find_element(By.XPATH, num_xp).text)
		usr.append(b_name)
		usr.append(b_num)
		temp =str(f'{str(usr[0])} {str(usr[1])} {str(usr[2])} {str(usr[3])}\n')
		print(temp)
		f = open('new.txt', 'a')
		f.write(str(temp))
		f.close()
	print(usr_arr)
	