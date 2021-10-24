from bs4 import BeautifulSoup
import requests
import pandas as pd

url='https://tonari-it.com'
query='Python　初心者'
paramas={'s':query}
r=requests.get(url)
r.raise_for_status()

soup=BeautifulSoup(r.text,'html.parser')
h2s=soup.find_all('h2')
anchors=soup.find_all('a',attrs={'class':'entry-card-wrap a-wrap border-element cf'})

values=[]
for h2,anchor in zip(h2s,anchors):
    values.append([h2.text,anchor.attrs['href']])

filename=r'scraping_practice01.xlsx'
df=pd.DataFrame(values,columns=['title','URL'])
df.index=df.index+1
df.to_excel(filename)
print(df)