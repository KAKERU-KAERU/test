from bs4 import BeautifulSoup
import requests
import pandas as pd

url='https://www.billboard.com/charts/hot-100'
r=requests.get(url)

soup = BeautifulSoup(r.text, 'html.parser')

data=[]

elements=soup.find_all('span',attrs={'class':'chart-element__information'})

for element in elements:

    name=element.find('span',attrs={'class':'chart-element__information__song text--truncate color--primary'})
    name=name.text
    
    artist=element.find('span',attrs={'class':'chart-element__information__artist text--truncate color--secondary'})
    artist=artist.text

    datalist={}
    
    datalist['SONG']=name
    datalist['ARTIST']=artist

    data.append(datalist)

df=pd.DataFrame(data)
df.to_csv('music.csv',index=False)
print(df.columns)