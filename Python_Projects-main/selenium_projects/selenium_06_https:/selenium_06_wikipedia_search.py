import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

print('------------------ Bolum 1 Wikipedia - Search Button--------')
Path = '/Users/macbook/chromedriver'
driver = webdriver.Chrome(Path)

driver.get('https://tr.wikipedia.org/wiki/Anasayfa')
driver.implicitly_wait(5)

search_bar = driver.find_element(By.NAME, 'search')

# Write 'Data Science' into Search Bar
actions =ActionChains(driver)
actions.click(search_bar).perform()
actions.send_keys_to_element(search_bar, 'Data Science').perform()
driver.implicitly_wait(5)

# Click search button (small part right side)
actions =ActionChains(driver)
search_bar_button = driver.find_element(By.XPATH, '//*[@id="searchform"]/div/button')
actions.click(search_bar_button).perform()
driver.implicitly_wait(5)

# Titles Finded
heading = driver.find_elements(By.CLASS_NAME, 'mw-search-result-heading')
print(heading)
for i in heading:
    print(i.text)

# Go to 'Veri Bilimi' Title
actions =ActionChains(driver)
veri_bilimi = driver.find_element(By.LINK_TEXT, 'Veri bilimi')
actions.click(veri_bilimi).perform()
time.sleep(5)

driver.quit()