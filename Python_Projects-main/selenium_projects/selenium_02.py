import datetime

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 1 - chromedriver run
Path = '/Users/macbook/Desktop/projects/Github_Repositories/Python_Projects/selenium_projects/chromedriver'
driver = webdriver.Chrome(Path)

# Go to Website
driver.get('https://www.techwithtim.net/')
print(driver.title)

search = driver.find_element(By.NAME, "s")

# Write test to search label
search.send_keys('test')
search.send_keys(Keys.RETURN)

# Page Source
print(driver.page_source)

# Find Element
# Explicit wait methodu kullanildi calisirken hata olusmasin diye
try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'main'))
    )
    print(main.text)
    print(50*'*')
    articles = main.find_elements(By.TAG_NAME, 'article')
    for article in articles:
        header = article.find_element(By.CLASS_NAME, 'entry-summary')
        print(header.text)
    print('Try calisti')
except:
    print('Except Calisti')
    driver.quit()

driver.quit()

