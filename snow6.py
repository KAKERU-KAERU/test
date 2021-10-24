import requests
import datetime
import pytz
from bs4 import BeautifulSoup
import pandas as pd
import pathlib
import os
import time
TOKEN='3zD7zecDM4g7wGO7nQFxh9R0Rs3Ssp55bhuGalIVE7X'
def S6():
    global TOKEN
    api_url='https://notify-api.line.me/api/notify'

    Time=datetime.datetime.now(pytz.timezone('Asia/Tokyo'))
    Time=Time.strftime('%h/%d/%Y  %H:%M')

    h_filename=r'C:\Users\mizun\OneDrive\MyPythonProject\image_folder'

    img_url=f'http://www.yokoteyama.com/live/image4.jpg'#URL of the page 

    image=requests.get(img_url)

    filename  = h_filename + '\\img.jpg'
    print(filename)

    with open(filename, 'wb') as f:
        f.write(image.content)
        
    #TEXT 
    ##################################################################################
    url='https://surfsnow.jp/search/list/spl_snow.php?key=%E6%A8%AA%E6%89%8B%E5%B1%B1'

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

    text={f"\n\n横手山スキー場\n\n{Time}\n{df}\n{title_url}"}
    ##################################################################################

    send_contents=text

    TOKEN_dic={'Authorization':'Bearer'+' '+TOKEN}#SPACE!!
    send_dic={'message':send_contents}
    print(TOKEN_dic)
    print(send_dic)

    binary=open(filename,mode='rb')
    image_dic={'imageFile':binary}

    requests.post(api_url,headers=TOKEN_dic,data=send_dic,files=image_dic)
    binary.close()
    fp=pathlib.Path(filename)
    print(fp)
    fp.unlink()