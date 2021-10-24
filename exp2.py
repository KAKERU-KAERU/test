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
    #(amount of elements,row,line)
    range_list=[[(10,1,1),(2,2,1),(5,1,2),(5,2,2),(6,1,3),(6,2,3)],
    [(6,1,1),(6,2,1),(7,1,2),(5,2,2),(9,1,3),(3,2,3)],
    [(6,1,1),(6,2,1),(6,1,2),(6,2,2),(4,1,3),(3,2,3),(3,3,3)], 
    [(5,1,1),(6,2,1),(6,1,2),(5,2,2),(7,1,3),(5,2,3)],
    [(6,1,1),(5,2,1),(6,1,2),(5,2,2),(6,1,3),(4,2,3)],
    [(8,1,1),(3,2,1),(5,1,2),(5,2,2),(8,1,3),(3,2,3)],
    [(4,1,1),(3,2,1),(4,3,1),(3,1,2),(3,2,2),(3,3,2),(2,4,2),(4,1,3),(4,2,3),(4,3,3)],
    [(6,1,1),(6,2,1),(5,1,2),(5,2,2),(6,1,3),(6,2,3)],
    [(7,1,1),(8,2,1),(5,1,2),(5,2,2),(3,3,2),(2,1,3),(2,2,3),(7,3,3)],
    [(6,1,1),(6,2,1),(6,1,2),(6,2,2),(6,1,3),(6,2,3)],
    [(4,1,1),(4,2,1),(4,3,1),(4,1,2),(4,2,2),(4,3,2),(4,1,3),(3,2,3),(1,3,3),(3,4,3)],
    [(8,1,1),(5,2,1),(10,1,2),(3,2,2),(8,1,3),(5,2,3)],
    [(0,1,1),(6,2,1),(5,1,2),(5,2,2),(6,1,3),(5,2,3)]]


    #(a,dl,div)                                    
    for L in range(1,14):                                        
        actions.move_to_element(browser.find_element_by_xpath(f'//*[@id="home-firstscreen"]/div/div/div[2]/div/div/div[2]/dl[{L}]/dt/span')).perform()
        for (i,j,k) in range_list[L-1]:
            print(i,j,k)
            for I in range(1,i+1):
                datalist={}
                name=browser.find_element_by_xpath(f'//*[@id="home-firstscreen"]/div/div/div[2]/div/div/div[2]/dl[{L}]/dd/div/div[1]/div[{k}]/dl[{j}]/dd/a[{I}]').text
                url1=browser.find_element_by_xpath(f'//*[@id="home-firstscreen"]/div/div/div[2]/div/div/div[2]/dl[{L}]/dd/div/div[1]/div[{k}]/dl[{j}]/dd/a[{I}]').get_attribute('href')
                datalist['TAG']=name 
                datalist['URL']=url1                 
                data.append(datalist)
    df=pd.DataFrame(data)
    df.to_csv('p1.csv',index=False,header=True,mode='a')
    print(df)

        
if browser.find_elements_by_xpath('/html/body/div[7]/div/div/img[2]')==[]:
    scrape()

else:
    browser.find_element_by_xpath('/html/body/div[7]/div/div/img[2]').click()
    scrape()    
