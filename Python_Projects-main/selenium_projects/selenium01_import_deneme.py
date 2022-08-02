from selenium import webdriver
import time

# 1- Calistirmak icin chromedriver indirdik
driver_path = '/Users/macbook/Desktop/chromedriver'

browser = webdriver.Chrome(driver_path)

# 2- Su sayfaya git
browser.get('https://www.sinanerdinc.com')
time.sleep(3)

# 3 - Site Basligi yazdir
print('Site Basiligi :', browser.title)
browser.refresh()

browser.save_screenshot('/Users/macbook/Desktop/selenium_projects/test.png')
browser.maximize_window()
browser.

# 4 - Site icinde sayfa ac
browser.get('https://www.sinanerdinc.com/python')
#browser.set_window_size(800,600)
time.sleep(3)

# 5-  Eski sayfaya don
browser.back()

# 6- 4 Saniye bekler ver kapanir
time.sleep(3)
browser.quit()

