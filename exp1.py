from pandas.core.indexes.base import Index
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time 
from selenium.webdriver.common.action_chains import ActionChains

data=[]
url="https://ja.aliexpress.com/"

options=Options()

browser=webdriver.Chrome(executable_path=r'C:\Users\mizun\OneDrive\MyPythonProject\Mypandas\chromedriver.exe')
browser.maximize_window()
browser.implicitly_wait(3)

browser.get(url)
time.sleep(3)
print('access complete')
    
actions = ActionChains(browser)


def scrape():
    data=[]                                                
    actions.move_to_element(browser.find_element_by_xpath('//*[@id="home-firstscreen"]/div/div/div[2]/div/div/div[2]/dl[1]/dt/span/a' )).perform()
    for (i,j,k) in (10, 1,1),(2, 2,1),(5, 1,2),(5, 2,2),(6, 1,3),(6, 2,3):
        
        for I in range(1,i+1):
            datalist={}
            name=browser.find_element_by_xpath(f'//*[@id="home-firstscreen"]/div/div/div[2]/div/div/div[2]/dl[1]/dd/div/div[1]/div[{k}]/dl[{j}]/dd/a[{I}]').text
            url1=browser.find_element_by_xpath(f'//*[@id="home-firstscreen"]/div/div/div[2]/div/div/div[2]/dl[1]/dd/div/div[1]/div[{k}]/dl[{j}]/dd/a[{I}]').get_attribute('href')
            datalist['TAG']=name
            datalist['URL']=url1
            data.append(datalist)
    df=pd.DataFrame(data)
    df.to_csv('p1.csv',index=False,mode='a')
    print(df)

    browser.close()
    
if browser.find_elements_by_xpath('/html/body/div[4]/div/div/img[2]')==[]:
    scrape()

else:
    browser.find_element_by_xpath('/html/body/div[4]/div/div/img[2]').click()
    scrape()    

