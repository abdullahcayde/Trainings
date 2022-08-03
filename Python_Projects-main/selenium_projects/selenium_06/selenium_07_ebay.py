import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd

'''
Title : Web Scrapping by Selenium 
Project Purpose: From Ebay Klein-Anzeige scrap data for Honda Jazz Automatic Cars 

1 - Create Driver
2 - Go to Website
3 - Create ActionChain Object
    3.1 - Click Banned Accept
    3.2 - Click Search-Ort and write 'Rietberg'
    3.3 - Click Search-Kategories and write 'honda jazz automatik'
    3.4 - Click Ganzort 30km and Press Enter
    3.5 - Click Autos Link
    3.6 - Write min-max Preis and press Enter
4 - Take Title and Price from Page
    4.1 - Create Lists 
    4.2 - Create DataFrame
    4.3 - Print and Save DataFrame
'''


print('---------------------- Part 1 Ebay ----------------------')
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
driver.get('https://www.ebay-kleinanzeigen.de/')
driver.implicitly_wait(10)

#  3 - ActionChain Object created
# 3.1 -
actions = ActionChains(driver)
akzeptieren = driver.find_element(By.ID, 'gdpr-banner-accept')
actions.click(akzeptieren).perform()
driver.implicitly_wait(10)

# 3.2 -
search_bar_ort =  driver.find_element(By.ID, 'site-search-area')
actions.click(search_bar_ort).perform()
actions.send_keys_to_element(search_bar_ort, ort_).perform()
driver.implicitly_wait(10)

# 3.3 -
search_bar_autos = driver.find_element(By.ID, 'site-search-query')
actions.click(search_bar_autos).perform()
actions.send_keys_to_element(search_bar_autos, model_).perform()
driver.implicitly_wait(10)

# 3.4 -
search_bar_GanzerOrt =  driver.find_element(By.ID, 'site-search-distance-inpt')
actions.click(search_bar_GanzerOrt).perform()
search_bar_30km = driver.find_element(By.XPATH, '/html/body/header/section[2]/div/div/div[1]/div/form/div/div[2]/div/div[2]/div/ul/li[5]')
actions.click(search_bar_30km).perform()
actions.key_down(Keys.ENTER).perform()
driver.implicitly_wait(10)
sleep(1)

# 3.5 -
autos = driver.find_element(By.LINK_TEXT, 'Autos')
actions.click(autos).perform()
driver.implicitly_wait(10)
sleep(1)

# 3.6 -
preis_min = driver.find_element(By.ID, 'srchrslt-brwse-price-min')
actions.click(preis_min).perform()
actions.send_keys_to_element(preis_min, price_MIN).perform()
preis_max = driver.find_element(By.ID, 'srchrslt-brwse-price-max')
actions.click(preis_max).perform()
actions.send_keys_to_element(preis_max, price_MAX).perform()
driver.implicitly_wait(8)
actions.key_down(Keys.ENTER).perform()
sleep(1)

# Headers
header = driver.find_elements(By.CLASS_NAME, 'ellipsis')
preis = driver.find_elements(By.CLASS_NAME, 'aditem-main--middle--price')


# 4 -  Headers List
# 4.1 -
header_list = list()
header_list = [title.text for title in header][1:]
print(header_list)
preis_list = list()
preis_list = [p.text for p in preis][1:]
print(preis_list)

# 4.2 - DataFrame df
d = {'Title':header_list, 'Price':preis_list}
df = pd.DataFrame(d)
print(df)

# 4.3 - Save DataFrame
df.to_csv('ebay07_jazz_auto.csv')




# Finally Quit
time.sleep(15)
print('Code Runned Without Problem')
driver.quit()

