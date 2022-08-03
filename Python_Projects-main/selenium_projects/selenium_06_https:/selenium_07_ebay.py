import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd

print('------------------ Bolum 1 Ebay - Search Button--------')
def sleep(x):
    time.sleep(x)

Path = '/Users/macbook/chromedriver'
driver = webdriver.Chrome(Path)

driver.get('https://www.ebay-kleinanzeigen.de/')
driver.implicitly_wait(5)

actions = ActionChains(driver)
akzeptieren = driver.find_element(By.ID, 'gdpr-banner-accept')
actions.click(akzeptieren).perform()
driver.implicitly_wait(8)

autos_Rad_Boot = driver.find_element(By.LINK_TEXT, 'Auto, Rad & Boot')
actions.click(autos_Rad_Boot).perform()
driver.implicitly_wait(10)
sleep(1)

autos = driver.find_element(By.LINK_TEXT, 'Autos')
actions.click(autos).perform()
driver.implicitly_wait(8)
sleep(2)

search_bar_autos = driver.find_element(By.ID, 'site-search-query')
actions.click(search_bar_autos).perform()
actions.send_keys_to_element(search_bar_autos, 'honda jazz automatik').perform()
#actions.key_down(Keys.ENTER).perform()
driver.implicitly_wait(8)
sleep(1)


search_bar_ort =  driver.find_element(By.ID, 'site-search-area')
actions.click(search_bar_ort).perform()
actions.send_keys_to_element(search_bar_ort, 'Rietberg').perform()
#actions.key_down(Keys.ENTER).perform()
driver.implicitly_wait(8)


search_bar_GanzerOrt =  driver.find_element(By.ID, 'site-search-distance-inpt')
actions.click(search_bar_GanzerOrt).perform()
search_bar_30km = driver.find_element(By.XPATH, '/html/body/header/section[2]/div/div/div[1]/div/form/div/div[2]/div/div[2]/div/ul/li[5]')
actions.click(search_bar_30km).perform()
actions.key_down(Keys.ENTER).perform()
driver.implicitly_wait(8)
sleep(2)

preis_min = driver.find_element(By.ID, 'srchrslt-brwse-price-min')
actions.click(preis_min).perform()
actions.send_keys_to_element(preis_min, '2000').perform()
preis_max = driver.find_element(By.ID, 'srchrslt-brwse-price-max')
actions.click(preis_max).perform()
actions.send_keys_to_element(preis_max, '7000').perform()
driver.implicitly_wait(8)
actions.key_down(Keys.ENTER).perform()
sleep(2)


# Headers
header = driver.find_elements(By.CLASS_NAME, 'ellipsis')
#year = driver.find_elements(By.CLASS_NAME, 'simpletag tag-small')
#preis = driver.find_elements(By.CLASS_NAME, 'aditem-main--middle--price')

for title in header:
    print(title.text)
# Headers List
header_list = [title.text for title in header][1:]
print(header_list)

# Header df
header_list2 = list()

for i in range(len(header_list2)):
    title[i] = (title[i].text).strip("\n").strip()

df = pd.DataFrame(header_list2,columns = ["Title"])
print(df)

#close_einloggen = driver.find_element(By.XPATH, '/html/body/header/section[1]/section/div/div/a')
#actions.click(close_einloggen).perform()

time.sleep(15)
print('Code Runned Without Problem')
driver.quit()

