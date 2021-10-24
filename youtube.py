from selenium import webdriver
import time 
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

CHROME_BIN = "/usr/bin/chromium-browser"
CHROME_DRIVER = os.path.expanduser(r'C:\Users\mizun\OneDrive\MyPythonProject\Mypandas\chromedriver')

options = Options()
#options.binary_location = CHROME_BIN
options.add_argument('--headless')
options.add_argument('--window-size=1280,3000')
driver = webdriver.Chrome(CHROME_DRIVER, chrome_options=options)
url='https://www.youtube.com/watch?v=JHHpQFZYBZQ&embedded=tru'
driver.get(url)
time.sleep(3)
driver.maximize_window()
time.sleep(3)
driver.find_element_by_class_name('ytp-fullscreen-button').click()
time.sleep(6)                  
# full screen
driver.save_screenshot(r'C:\Users\mizun\OneDrive\MyPythonProject\image_folder\SNOWAD.png')
driver.quit()