from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

Path = '/Users/macbook/Desktop/projects/Github_Repositories/Trainings/Python_Projects-main/selenium_projects/chromedriver'
driver = webdriver.Chrome(Path)

# Go to Website
driver.get('https://orteil.dashnet.org/cookieclicker/')

# To be Sure to Load Website
driver.implicitly_wait(5)

cookie = driver.find_element(By.ID, 'bigCookie')
cookie_count = driver.find_element(By.ID, 'cookies')
#items = [driver.find_element(By.ID, 'productPrice' + str(i)) for i in range(1,-1,-1)]
language = driver.find_element(By.ID, 'langSelect-EN')

'''
# Language Click
actions.click(language)
actions.perform()
driver.implicitly_wait(10)
'''
time.sleep(7)
driver.implicitly_wait(10)
# Cookie Click for 15 Times
actions = ActionChains(driver)
#click_action.move_to_element(cookie)
for i in range(15):
    actions.click(cookie)
    actions.perform() # No perfom no action
print('code Runned')
time.sleep(15)
driver.quit()