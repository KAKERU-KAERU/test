import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
options.add_argument('--headless')
driver = webdriver.Chrome(chrome_options=options,executable_path=r'C:\Users\mizun\OneDrive\MyPythonProject\Mypandas\chromedriver.exe')
url='https://www.youtube.com/watch?v=DG6BJJj3e7w'
varurl = url.replace("watch?v=", "embed/")
driver.get(varurl)
time.sleep(3)
driver.set_window_size(1920, 1080)
time.sleep(3)
driver.find_element_by_class_name('ytp-large-play-button').click()
driver.find_element_by_class_name('ytp-fullscreen-button').click()
time.sleep(20)
driver.save_screenshot(r'C:\Users\mizun\OneDrive\MyPythonProject\image_folder\SNOWAD.png')