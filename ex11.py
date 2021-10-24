from bs4 import BeautifulSoup
import requests
import pandas as pd


url='http://snownet.jp/search/?pref=16'
r=requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')

r=requests.get(url)

soup = BeautifulSoup(r.content, 'html.parser')

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
    datum['SCORE']= eval_num
    data.append(datum)

    df=pd.DataFrame(data)
    print(df)
    df.to_csv('p1.csv')