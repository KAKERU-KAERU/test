from selenium import webdriver
import time
import pandas as pd

USER='6221099'#USERNAME
PASS='Starwars0510!'#PASSWORD

browser=webdriver.Chrome(executable_path=r'C:\Users\mizun\OneDrive\MyPythonProject\Mypandas\chromedriver.exe')
browser.implicitly_wait(3)

url_login="https://letus.ed.tus.ac.jp/"#URL of login page
browser.get(url_login)
time.sleep(3)
print('access complete')

element=browser.find_element_by_id('login_username')#id
element.clear()
element.send_keys(USER)
element=browser.find_element_by_id('login_password')#id
element.clear()
element.send_keys(PASS)
print('fill in complete')

browser_from=browser.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/section/aside/section[1]/div/div/form/div[4]/input')#use the xpath
time.sleep(1)
browser_from.click()
print('login complete')

browser_from=browser.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/section/aside/section[4]/div/div/ul/li[9]/div/a')#use the fullxpath
time.sleep(1)
browser_from.click()
print('went to the mecanics page')

browser_from=browser.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[1]/section/div/div/ul/li[1]/div[3]/ul/li[3]/div/div/div[2]/div/a/span')#use the fullxpath
time.sleep(1)
browser_from.click()
print('download the pdf files')

input()