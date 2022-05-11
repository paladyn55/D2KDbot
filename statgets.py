from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(options=chrome_options)
import warnings
warnings.filterwarnings('ignore')
from selenium.webdriver.common.by import By
import csv
import time
from selenium.webdriver.support.relative_locator import locate_with
from webdriver_manager.chrome import ChromeDriverManager
#----------------------------------------------------------------
t_xp = '/html/body/div[1]/div[2]/div[2]/div/main/div[3]/div[3]/div[1]/div[2]/div[2]/div[1]/div/div[1]/div[3]/div/div[1]/span[2]'
c_xp = '/html/body/div[1]/div[2]/div[2]/div/main/div[3]/div[3]/div[1]/div[2]/div[2]/div[3]/div/div[1]/div[1]/div/div[1]/span[2]'
v_xp = '/html/body/div[1]/div[2]/div[2]/div/main/div[3]/div[3]/div[1]/div[2]/div[2]/div[3]/div/div[1]/div[1]/div/div[1]/span[2]'
s_xp = '/html/body/app-root/div/div[2]/app-report/div[1]/div[2]/div/div[1]/app-player/div/div/div/div/div[1]/app-player-main-stats/div/div[2]/div/div[4]/div/div[1]'
n_xp = '/html/body/div[1]/div[2]/div[2]/div/main/div[3]/div[1]/div[2]/div[2]/div[2]/span/span[1]'
#id = closeIconHit
#----------------------------------------------------------------
def hasxpath(xpath):
    try: 
        driver.find_element_by_xpath(xpath)
        return True
    except:
        return False
def stat_check(url):
	global t_xp
	global c_xp
	global v_xp
	global s_xp
	print("1")
	driver.get(url)
	print("2")
	time.sleep(5)
	print(str(hasxpath(t_xp)))
	while True:
		if hasxpath(n_xp) == True:
			break
		else:
			time.sleep(1)
			print("/")
	print("3")
	cl_ad = driver.find_element(By.ID, 'closeIconHit')
	cl_ad.click()
	print("4")
	tkd = driver.find_element(By.XPATH, t_xp).text
	#tkd = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div/main/div[2]/div[3]/div[1]/div[2]/div[2]/div[1]/div/div[1]/div[3]/div/div[1]/span[2]').text
	print(tkd)
	ckd = driver.find_element(By.XPATH, c_xp).text
	print(ckd)
	vkd = driver.find_element(By.XPATH, v_xp).text
	print(vkd)
	url_n = url[52:71]
	url_n = 'https://trials.report/report/2/' + url_n
	driver.get(url_n)

	#WebDriverWait(driver, timeout = 45).until(lambda d: d.find_element_by_xpath("/html/body/app-root/div/div[2]/app-report/div[1]/div[2]/div/div[1]/app-player/div/div/app-player-header/div/div[1]/div[2]/div[1]/h2"))
	print("1")
	time.sleep(25)
	print("2")
	skd = driver.find_element(By.XPATH, s_xp).text
	kdarr = [skd, tkd, ckd, vkd]
	print(kdarr)
	return kdarr