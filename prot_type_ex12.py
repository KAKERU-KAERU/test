from bs4 import BeautifulSoup
import requests
import pandas as pd 
import re
import time

for i in range(1,7):

    url=f''#URL of the page 
    r=requests.get(url, verify=False)
    soup = BeautifulSoup(r.content, 'html.parser')
    print(r.status_code)

    data = []

    spots = soup.find_all('div',attrs={'class':'detailMain'})
    for spot in spots:
        spot_name = spot.find('h2')
        spot_name = spot_name.text
            
        eval_num = spot.find('dl',attrs={'class':'review'})
        eval_num=eval_num.text

        categoryItems = spot.find('table', attrs={'class':'type1'})
        categoryItems = categoryItems.find_all('tr')

        details = {}

        for categoryItem in categoryItems:
            category = categoryItem.th.text
            category=category.strip()
                
            rank = categoryItem.td.text
                
            rank=rank.strip()
            rank=rank.replace('\t','')
            
            details[category] = rank

        datum = details
        datum['PLACE'] = spot_name
        datum['SCORE']=eval_num
        data.append(datum)

        df=pd.DataFrame(data)
        df=df[['PLACE','SCORE','アクセス','営業時間','コース数']]
        time.sleep(5)
        
    df.to_csv(r'p1.csv', mode='a', header=False)#path of the csvfile

print(df)