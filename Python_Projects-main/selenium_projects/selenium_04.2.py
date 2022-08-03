from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

Path = '/Users/macbook/chromedriver'
driver = webdriver.Chrome(Path)

# Go to Website
driver.get('https://orteil.dashnet.org/cookieclicker/')

# To be Sure to Load Website
driver.implicitly_wait(8)
time.sleep(5)
print('Code Runned First')
cookie = driver.find_element(By.ID, 'bigCookie')
cookie_count = driver.find_element(By.ID, 'cookies')
#items = [driver.find_element(By.ID, 'productPrice' + str(i)) for i in range(1,-1,-1)]
language = driver.find_element(By.ID, 'langSelect-EN')

actions = ActionChains(driver)
actions.click(cookie)
actions.perform()

driver.implicitly_wait(15)

print('Code Runned End')

time.sleep(20)
driver.quit()
