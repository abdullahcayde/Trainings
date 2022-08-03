import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

Path = '/Users/macbook/chromedriver'
driver = webdriver.Chrome(Path)

driver.get('https://demoqa.com/selectable')
driver.implicitly_wait(5)

one = driver.find_element(By.XPATH, '//*[@id="verticalListContainer"]/li[1]')
two = driver.find_element(By.XPATH, '//*[@id="verticalListContainer"]/li[2]')
three = driver.find_element(By.XPATH, '//*[@id="verticalListContainer"]/li[3]')
four =  driver.find_element(By.XPATH, '//*[@id="verticalListContainer"]/li[4]')

actions = ActionChains(driver)
#actions.click(one)
#actions.click(two)
#actions.click(three)
#actions.click(four)

for click in range(5):
    actions.click(one)
    actions.perform()
    time.sleep(0.5)
    print('click.')

#actions.perform()

time.sleep(10)
driver.quit()