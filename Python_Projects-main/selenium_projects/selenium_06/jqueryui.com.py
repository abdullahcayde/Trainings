import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

'''
print('---------------- Bolum 1 -----------------------------------')
Path = '/Users/macbook/chromedriver'
driver = webdriver.Chrome(Path)

driver.get('https://jqueryui.com/')
driver.implicitly_wait(5)

selectable = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[2]/aside[1]/ul/li[4]/a')

# Click Selectable
actions = ActionChains(driver)
actions.click(selectable)

actions.perform()

print('selectable Runned')


time.sleep(3)
driver.quit()
'''
'''
print('--------------------- Bolum 2 ----------------------')

Path = '/Users/macbook/chromedriver'
driver = webdriver.Chrome(Path)

driver.get('https://jqueryui.com/selectable')
driver.implicitly_wait(5)

one = driver.find_element(By.XPATH, '/html/body/ol/li[1]')
two = driver.find_element(By.XPATH, '//*[@id="selectable"]/li[2]')
three = driver.find_element(By.XPATH, '//*[@id="selectable"]/li[3]')

actions = ActionChains(driver)
actions.key_down(Keys.CONTROL)
actions.click(one)
actions.click(two)
actions.click(three)

actions.perform()

time.sleep(3)
driver.quit()
'''
'''
print('--------------------- Bolum 3 --------')

Path = '/Users/macbook/chromedriver'
driver = webdriver.Chrome(Path)

driver.get('https://jqueryui.com/accordion')
driver.implicitly_wait(5)

sortable = driver.find_element(By.LINK_TEXT, 'Sortable')
no_auto_hight = driver.find_element(By.LINK_TEXT, 'No auto height')
#section2 = driver.find_element(By.XPATH, '//*[@id="ui-id-3"]')

actions = ActionChains(driver)
actions.click(sortable)
actions.click(no_auto_hight)
actions.perform()

time.sleep(4)
driver.quit()
'''
