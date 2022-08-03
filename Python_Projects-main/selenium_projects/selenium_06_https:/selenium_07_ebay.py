import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

print('------------------ Bolum 1 Ebay - Search Button--------')
Path = '/Users/macbook/chromedriver'
driver = webdriver.Chrome(Path)

driver.get('https://www.ebay-kleinanzeigen.de/')
driver.implicitly_wait(5)

actions = ActionChains(driver)
akzeptieren = driver.find_element(By.ID, 'gdpr-banner-accept')
actions.click(akzeptieren).perform()

autos_Rad_Boot = driver.find_element(By.LINK_TEXT, 'Auto, Rad & Boot')
actions.click(autos_Rad_Boot).perform()
driver.implicitly_wait(8)
time.sleep(4)

autos = driver.find_element(By.LINK_TEXT, 'Autos')
actions.click(autos).perform()
driver.implicitly_wait(8)
time.sleep(4)

search_bar_autos = driver.find_element(By.ID, 'site-search-query')
actions.click(search_bar_autos).perform()
actions.send_keys_to_element(search_bar_autos, 'honda jazz automatik').perform()
actions.key_down(Keys.ENTER).perform()
driver.implicitly_wait(5)
time.sleep(3)

time.sleep(5)
print('Code Runned Without Problem')
driver.quit()