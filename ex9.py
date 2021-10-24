from bs4 import BeautifulSoup
from numpy import False_
from pandas.core.indexes.base import Index
import requests
import pandas as pd

url='http://snownet.jp/search/?pref=16'
r=requests.get(url)

soup = BeautifulSoup(r.content, 'html.parser')

data = []

spots = soup.find_all('div',attrs={'class':'detailMain'})
for spot in spots:
    spot_name = spot.find('div', attrs={'class':'lineBtm'})
    
    spot_name = spot_name.text
    

    eval_num = spot.find('dd',attrs={'class':'star_star4'})
    

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
    print(data)

df=pd.DataFrame(data)
print(df)
df.to_csv('p1.csv')