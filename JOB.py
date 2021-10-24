import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
from selenium.webdriver.chrome.options import Options
from selenium import webdriver


wordlist={'Python','スクレイピング',}#TYPE the KEYWORD
options = Options()
options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
options.add_argument('--headless')
driver = webdriver.Chrome(chrome_options=options,executable_path=r'C:\Users\mizun\OneDrive\MyPythonProject\Mypandas\chromedriver.exe')
page_width = 2729
page_height = 1542
data=[]
for Key in wordlist:
    URL1=f'https://crowdworks.jp/public/jobs/search?search%5Bkeywords%5D={Key}&keep_search_criteria=true&order=-popular&hide_expired=true'
    R1=requests.get(URL1)
    SOUP1=BeautifulSoup(R1.content,'html.parser')
    NUM1=SOUP1.find('p',attrs={'class':'result_count'})
    NUM1=NUM1.find('span').text
    NUM1=int(NUM1.replace(',',""))
    NUM1=int(NUM1/50)
    n1=NUM1+1
    

    for i in range(1,n1):

        Url1=f'https://crowdworks.jp/public/jobs/search?hide_expired=true&keep_search_criteria=true&order=-popular&page={i}&search%5Bkeywords%5D={Key}'
        r1=requests.get(Url1)
        soup1=BeautifulSoup(r1.content,'html.parser')
        elements1=soup1.find_all("div",attrs={"class":"item job_item"})


        for element1 in elements1:

            datalist1={}

            Content1=element1.find("a").text
            
            reward1=element1.find("b",attrs={"class":"amount"}).text
            page_width = 2729
            page_height = 1542
            url1=element1.find("a").attrs['href']
            #driver.get(url1)
            #driver.set_window_size(page_width, page_height)
            #driver.find_element_by_class_name("cw-button cw-button_highlight cw-button_block cw-button_lg").click
            datalist1["内容"]=Content1.replace('\t','')
            datalist1["REWARD"]=reward1.replace('\t','')
            datalist1["URL"]=f'https://crowdworks.jp/{url1}'.replace('\t','')

            data.append(datalist1)
        df=pd.DataFrame(data)
        df.to_csv('job.csv',header=True,index=False,mode='a',encoding='utf-8')
        time.sleep(1)