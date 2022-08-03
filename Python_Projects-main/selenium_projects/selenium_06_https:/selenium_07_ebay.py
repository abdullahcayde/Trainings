import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

print('------------------ Bolum 1 Ebay - Search Button--------')
Path = '/Users/macbook/chromedriver'
driver = webdriver.Chrome(Path)

driver.get('https://tr.wikipedia.org/wiki/Anasayfa')
driver.implicitly_wait(5)