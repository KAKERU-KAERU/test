from PIL import ImageGrab
from selenium import webdriver
import time 

url='https://www.youtube.com/watch?v=JHHpQFZYBZQ'
driver = webdriver.Chrome(executable_path=r'C:\Users\mizun\OneDrive\MyPythonProject\Mypandas\chromedriver.exe')
driver.get(url)
time.sleep(3)
driver.maximize_window()
time.sleep(4)
driver.find_element_by_class_name("ytp-fullscreen-button").click()
time.sleep(15)                  
# full screen
ImageGrab.grab().save("ex.png")
driver.close()