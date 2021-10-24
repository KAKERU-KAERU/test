import pathlib
import requests
import datetime
import pytz
from bs4 import BeautifulSoup
import os
import time
import pandas as pd
import time

TOKEN='3zD7zecDM4g7wGO7nQFxh9R0Rs3Ssp55bhuGalIVE7X'
def S1():
    global TOKEN
    TOKEN='3zD7zecDM4g7wGO7nQFxh9R0Rs3Ssp55bhuGalIVE7X'
    api_url='https://notify-api.line.me/api/notify'

    Time=datetime.datetime.now(pytz.timezone('Asia/Tokyo'))
    Time=time.strftime('%h/%d/%Y  %H:%M')

    h_filename=r'C:\Users\mizun\OneDrive\MyPythonProject\image_folder'


    url1=f'http://www.pal.kijimadaira.jp/~futa.net/livecamera_ski.html'#URL of the page 
    r1=requests.get(url1)
    soup1 = BeautifulSoup(r1.content, 'html.parser')

    img = soup1.find('p')
    img=img.find('img')
    img_url=img.get('src')
    print(img_url)
    image=requests.get(img_url)

    filename  = h_filename + '\KIJIMADAIRA.jpg'

    with open(filename + img_url.split('/')[-1], 'wb') as f:
        f.write(image.content)


    #TEXT 
    ##################################################################################
    url='https://surfsnow.jp/search/list/spl_snow.php?key=%E6%9C%A8%E5%B3%B6%E5%B9%B3'

    r=requests.get(url)
    soup=BeautifulSoup(r.text,'html.parser')

    elements=soup.find('table',attrs={'class':'section_weather'})
    elements=elements.find_all('tr')

    title_url=soup.find('div',attrs={'class':'list_result'})
    title_url=title_url.find('a').get('href')

    data1=[]
    for element in elements:
        datalist={}
        element_name=element.find('th').text
        element_name=element_name.replace('\t','')
        
        try:
            element_val=element.find('td')=={}
            element_val='NONE'
        except:
            element_val=element.find('td').text
            
            
        datalist['element']=element_name
        datalist['value']=element_val
        
        data1.append(datalist)
    del data1[0]


    index = ['','','','']
    df=pd.DataFrame(data=data1,index=index)
    df.rename(columns={'element':''},inplace=True)
    df.rename(columns={'value':''},inplace=True)


    text={f"\n\n木島平スキー場\n\n{Time}\n{df}\n{title_url}"}
    ##################################################################################

    send_contents=text

    TOKEN_dic={'Authorization':'Bearer'+' '+TOKEN}#SPACE!!
    send_dic={'message':send_contents}
    print(TOKEN_dic)
    print(send_dic)

    image_file=r'image_folder\KIJIMADAIRA.jpgidou.jpg'#filename
    binary=open(image_file,mode='rb')
    image_dic={'imageFile':binary}
    requests.post(api_url,headers=TOKEN_dic,data=send_dic,files=image_dic)
    binary.close()

    fp=pathlib.Path(image_file)
    print(fp)

    os.remove(fp)