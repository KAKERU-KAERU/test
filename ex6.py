from datetime import datetime
import requests
from bs4  import BeautifulSoup
from selenium import webdriver
import pandas as pd
import time

browser=webdriver.Chrome(executable_path=r'C:\Users\mizun\OneDrive\MyPythonProject\Mypandas\chromedriver.exe')#Chorme driver

for i in range (0,6):
  
    URL='https://fortune.yahoo.co.jp/omikuji/index.html'#URL
    browser.get(URL)
    time.sleep(3)

    button=browser.find_element_by_xpath('//*[@id="ftnstart"]/table[3]/tbody/tr[3]/td/form/center/input')#xpath
    button.click()

    result=browser.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div/div[2]/div[1]/div/div[3]/table[2]/tbody/tr/td/table[2]/tbody/tr/td')#xpath
    result.click()

    data={
        'DATE':[datetime.now()],
        'result of omikuji':[result.text]
        }

    df=pd.DataFrame(data)

    df.to_csv(r'omikuji.csv',mode='a')#csv file

input()