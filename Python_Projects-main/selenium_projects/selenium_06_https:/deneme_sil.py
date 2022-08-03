import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd


print('---------------------- Part 3 Ebay ----------------------')
def sleep(x):
    time.sleep(x)
def wait(x):
    driver.implicitly_wait(x)
model_ = 'honda jazz automatik'
ort_ = 'Rietberg'
price_MIN = '2000'
price_MAX = '7000'

#  1 - Create Driver
Path = '/Users/macbook/chromedriver'
driver = webdriver.Chrome(Path)

#  2 - Go to Website
driver.get('https://www.ebay-kleinanzeigen.de/s-autos/rietberg/preis:2000:7000/honda-jazz-automatik/k0c216l1363r30')
wait(10)
sleep(1.5)

#  3 - ActionChain Object created
# 3.1 -
actions = ActionChains(driver)
akzeptieren = driver.find_element(By.ID, 'gdpr-banner-accept')
actions.click(akzeptieren).perform()
driver.implicitly_wait(10)
sleep(1)
'''
# Headers, Price, Descrition
header = driver.find_elements(By.CLASS_NAME, 'ellipsis')
description_middle = driver.find_elements(By.CLASS_NAME, 'aditem-main--middle--description')
preis = driver.find_elements(By.CLASS_NAME, 'aditem-main--middle--price')


# 4 -  Headers List
# 4.1 -
header_list = list()
header_list = [title.text for title in header][1:]
print(header_list)
preis_list = list()
preis_list = [p.text for p in preis][1:]
print(preis_list)
description_middle_list = list()
description_middle_list = [des.text for des in description_middle][1:]


# 4.2 - DataFrame df
d = {'Title':header_list, 'Price':preis_list, 'Description':description_middle_list}
df = pd.DataFrame(d)
print(df)


# 4.3 - Save DataFrame
df.to_csv('.csv')
'''
bottom_2_text = driver.find_elements(By.CLASS_NAME, 'text-module-end')
bottom_2_text_list = list()
bottom_2_text_list = [des.text for des in bottom_2_text]
print(bottom_2_text_list)

top_text = driver.find_elements(By.CLASS_NAME, 'aditem-main--top--left')
top_text_list = [des.text for des in top_text]
print(top_text_list)

print('Code Runned No Problem')
sleep(4)
driver.quit()