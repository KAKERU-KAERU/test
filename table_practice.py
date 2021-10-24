import pandas as pd
from selenium import webdriver
import time
import matplotlib.pyplot as plt
from datetime import datetime

browser = webdriver.Chrome(executable_path=r'C:\Users\mizun\OneDrive\MyPythonProject\Mypandas\chromedriver.exe')
browser.implicitly_wait(3)
browser.get("https://nikkei225jp.com/fx/")

data=[]

while True:
    datalist={}
    time.sleep(5)
    rate=browser.find_element_by_xpath("/html/body/div[1]/div[8]/div[2]/table/tbody/tr[1]/td/div[2]/p").text
    print(rate)

    dt=datetime.now()
    Day=dt.day
    Hour=dt.hour
    Minutes=dt.minute
    Second=dt.second

    datalist['Time']=(f'{Day}.{Hour}.{Second}.{Minutes}.{Second}')
    datalist['RATE']=rate
    print(datalist)
    data.append(datalist)

    df=pd.DataFrame(data)
    df.to_csv('ex1.csv',index=False)

    df = pd.read_csv('ex1.csv', names=['Time', 'RATE'])
    plt.plot(df['RATE'],marker="o")
    plt.pause(0.1)