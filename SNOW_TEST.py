import pathlib
import requests
import datetime
import pytz
from bs4 import BeautifulSoup
import os
import time
import pandas as pd
import time

def SNOW():
    
    TOKEN='3zD7zecDM4g7wGO7nQFxh9R0Rs3Ssp55bhuGalIVE7X'
    api_url='https://notify-api.line.me/api/notify'

    Time=datetime.datetime.now(pytz.timezone('Asia/Tokyo'))
    Time=time.strftime('%h/%d/%Y  %H:%M')

    h_filename=r'C:\Users\mizun\OneDrive\MyPythonProject\image_folder'

    elements=[
    ('http://www.vill.kijimadaira.lg.jp/cam/idou.jpg','木島平スキー場'),
    ('https://iizunaresort.com/livecam/0000.jpg?000000','いいづなリゾートスキー場'),
    ('http://zaochuoropeway.co.jp/livecam/livecam.jpg','蔵王温泉スキー場'),
    ('https://www.ryuoo.com/img_cam/cam4/img.jpg','竜王スキーパーク'),
    ('http://www.yokoteyama.com/live/image4.jpg','横手山・渋峠スキー場'),
    ('https://live-media.monitorbox.jp/media/88/image/current.jpg','苗場スキー場'),
    ('http://www.iiji3so.com/today/maiko.jpg','舞子スノーリゾート'),
    ('https://nozawaski.sakura.ne.jp/livecam/uenotaira.jpg','野沢温泉スキー場'),
    ('https://livecam-web.vill.otari.nagano.jp/pics/recent/tuganomori.jpg','栂池高原スキー場'),
    ('https://livecam-web.vill.otari.nagano.jp/pics/recent/cortinaL.jpg','白馬コルチナスキー場'),
    ('http://yachiho-kogen.com/ski/webcam_2/image.jpg','八千穂高原スキー場'),
    ('https://live-media.monitorbox.jp/media/90/image/current.jpg','かぐらスキー場')
    ]
    
    for (image_url,Key) in elements:

        image=requests.get(image_url)

        filename  = h_filename + '\SNOW.jpg'

        with open(filename ,'wb') as f:
            f.write(image.content)

        print(Key)
        print(image_url)

        #TEXT 
        ##################################################################################

        url=f'https://surfsnow.jp/search/list/spl_snow.php?key={Key}'

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

        text={f"\n\n{Key}\n\n{Time}\n{df}\n{title_url}"}
        ##################################################################################

        send_contents=text

        TOKEN_dic={'Authorization':'Bearer'+' '+TOKEN}#SPACE!!
        send_dic={'message':send_contents}
        print(TOKEN_dic)
        print(send_dic)

        image_file=filename
        binary=open(image_file,mode='rb')
        image_dic={'imageFile':binary}
        requests.post(api_url,headers=TOKEN_dic,data=send_dic,files=image_dic)
        binary.close()

        fp=pathlib.Path(image_file)
        print(fp)

        os.remove(fp)

    url1=f'https://www.vill.hakuba.nagano.jp/live_camera/1257/'#URL of the page 
    r1=requests.get(url1)
    soup1 = BeautifulSoup(r1.text, 'html.parser')
    img = soup1.find('div',attrs={'class':'inEL'})
    img=img.find('img')
    img_url=img.get('src')

    img_url=f'https://www.vill.hakuba.nagano.jp{img_url}'
    print(img_url)
    image=requests.get(img_url)

    filename  = h_filename + '\HAKUBA.jpg'

    with open(filename + img_url.split('/')[-1], 'wb') as f:
        f.write(image.content)
        
    #TEXT 
    ##################################################################################
    url='https://surfsnow.jp/search/list/spl_snow.php?key=%E7%99%BD%E9%A6%AC%E4%BA%94%E7%AB%9C'

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

    text={f"\n\nエイブル白馬五竜\n\n{Time}\n{df}\n{title_url}"}
    ##################################################################################
    send_contents=text

    TOKEN_dic={'Authorization':'Bearer'+' '+TOKEN}#SPACE!!
    send_dic={'message':send_contents}
    print(TOKEN_dic)
    print(send_dic)

    image_file=filename + img_url.split('/')[-1]#filename
    binary=open(image_file,mode='rb')
    image_dic={'imageFile':binary}

    requests.post(api_url,headers=TOKEN_dic,data=send_dic,files=image_dic)
    binary.close()
    fp=pathlib.Path(image_file)
    print(fp)
    fp.unlink()

SNOW()