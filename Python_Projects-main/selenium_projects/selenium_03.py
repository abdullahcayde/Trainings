from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

Path = '/Users/macbook/Desktop/projects/Github_Repositories/Trainings/Python_Projects-main/selenium_projects/chromedriver'
driver = webdriver.Chrome(Path)

# Go to Website
driver.get('https://www.techwithtim.net/')

# Click Python Course
link = driver.find_element(By.LINK_TEXT, "Python Programming")
link.click()

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, 'Beginner Python Tutorials'))
    )
    element.click()

    get_started = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'sow-button-19310003'))
    )
    get_started.click()
    print('TRY calisti')

    driver.back()
    driver.back()
    driver.back()

    driver.forward()
    driver.forward()
    print('TRY-End calisti')
except:
    print('Except Calisti')
    driver.quit()

#driver.quit()