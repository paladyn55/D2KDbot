from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager
driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
import warnings
warnings.filterwarnings('ignore')
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.relative_locator import locate_with
#----------------------------------------------------------------
t_xp = '//*[@id="app"]/div[2]/div[2]/div/main/div[2]/div[3]/div[1]/div[2]/div[2]/div[1]/div/div[1]/div[3]/div/div[1]/span[2]'
c_xp = '//*[@id="app"]/div[2]/div[2]/div/main/div[2]/div[3]/div[1]/div[2]/div[2]/div[2]/div/div[1]/div[1]/div/div[1]/span[2]'
v_xp = '//*[@id="app"]/div[2]/div[2]/div/main/div[2]/div[3]/div[1]/div[2]/div[2]/div[3]/div/div[1]/div[1]/div/div[1]/span[2]'
s_xp = '//*[@id="swiperContainer"]/div/div[1]/app-player/div/div/div/div/div[1]/app-player-main-stats/div/div[2]/div/div[4]/div/div[1]'
#s_xp = /html/body/app-root/div/div/app-report/div[1]/div[2]/div/div[1]/app-player/div/div/div/div/div[1]/app-player-main-stats/div/div[2]/div/div[4]/div/div[1]
#id = closeIconHit
# xpaths keep changing, bot is broken, update xpaths
#try using relative xpaths (below name kd)
#----------------------------------------------------------------
def stat_check(url):
	global t_xp
	global c_xp
	global v_xp
	global s_xp
	driver.get(url)
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
	url_n = url[52:71]
	url_n = 'https://trials.report/report/2/' + url_n
	#maybe try requests instead of selenium for s KD
	driver.get(url_n)
	time.sleep(25)
	skd = driver.find_element(By.XPATH, s_xp).text
	kdarr = [skd, tkd, ckd, vkd]
	print(kdarr)
	return kdarr