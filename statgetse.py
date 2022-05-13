from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
import warnings
warnings.filterwarnings('ignore')
from selenium.webdriver.common.by import By
import time
#----------------------------------------------------------------
t_xp = '//*[@id="app"]/div[2]/div[2]/div/main/div[2]/div[3]/div[1]/div[2]/div[2]/div[1]/div/div[1]/div[3]/div/div[1]/span[2]'
c_xp = '//*[@id="app"]/div[2]/div[2]/div/main/div[2]/div[3]/div[1]/div[2]/div[2]/div[2]/div/div[1]/div[1]/div/div[1]/span[2]'
v_xp = '/html/body/div[1]/div[2]/div[2]/div/main/div[2]/div[3]/div[1]/div[2]/div[2]/div[3]/div/div[1]/div[1]/div/div[1]/span[2]'
s_xp = '/html/body/app-root/div/div[2]/app-report/div[1]/div[2]/div/div[1]/app-player/div/div/div/div/div[1]/app-player-main-stats/div/div[2]/div/div[4]/div/div[1]'
# xpaths keep changing, if bot is broken, update xpaths
#----------------------------------------------------------------
def stat_check(url):
	global t_xp
	global c_xp
	global v_xp
	global s_xp
	url_DTR = "https://destinytracker.com/destiny-2/profile/bungie/" + url + "/overview"
	driver.get(url_DTR)
	time.sleep(2)
	tkd = driver.find_element(By.XPATH, t_xp).text
	#tkd = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div/main/div[2]/div[3]/div[1]/div[2]/div[2]/div[1]/div/div[1]/div[3]/div/div[1]/span[2]').text
	print(tkd)
	ckd = driver.find_element(By.XPATH, c_xp).text
	print(ckd)
	vkd = driver.find_element(By.XPATH, v_xp).text
	print(vkd)
	#xpaths consistently working on replit now
	#trials report does crash occasionally
	#paladyn stats should be 1.37, 1.12, 1.56, 1.62 (can change slightly but should be roughly that)
	url_TR = 'https://trials.report/report/2/' + url
	#maybe try requests instead of selenium for s KD
	driver.get(url_TR)
	time.sleep(10)
	skd = driver.find_element(By.XPATH, s_xp).text
	kdarr = [skd, tkd, ckd, vkd]
	print(kdarr)
	return kdarr