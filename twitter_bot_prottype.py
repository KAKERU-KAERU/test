import pytz
import tweepy
import random
from bs4 import BeautifulSoup
import requests
import time
import pandas as pd
import os
import pathlib
import datetime
def main():

    keyword='スノーボード'
    CONSUMER_KEY='kfxKzlDoxbxxkxApgCNzPmK0S'
    CONSUMER_SECRET='Jr0NwOsvmPvFKrLtRBoSM1kqt7VdlhTwxklbBsqpKC95iG8vc5'
    ACCESS_TOKEN_KEY='1431851105370005504-nHyCabVTlypmd1iH5YEzpnjWdqPbkd'
    ACCESS_TOKEN_SECRET='XWk9JdsthTM4YRsvGDoD0XLcZMoLkrrWVNNmZ6YlOf6CS'
    authenticator=tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
    authenticator.set_access_token(ACCESS_TOKEN_KEY,ACCESS_TOKEN_SECRET)

    api=tweepy.API(authenticator,wait_on_rate_limit=True)
    my_user_id = api.me().id_str


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
    ('https://live-media.monitorbox.jp/media/90/image/current.jpg','かぐらスキー場'),
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
        time.sleep(1)
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

        ##############################################################################

        image_file=filename

        fp=pathlib.Path(image_file)
        print(fp)
        api.update_with_media(filename=filename,status=f"\n\n{Key}\n\n{Time}\n{df}\n\n{title_url}") # the contents of tweet
        os.remove(fp)

 
    # フォロー
    do(api,"FOLLOW",keyword)
 
    # リフォロー
    reFollow(api,my_user_id)

# タイムライン検索
def do(api,action,keyword,maxReq=5,maxTimeLine=20):

    for q in keyword:
        
        cnt = 0
        actCnt = random.randint(1,maxReq)          
        search_results = api.search(q=q, count=maxTimeLine)
        
        for result in search_results:
 
            tweet_id = result.id
            user_id  = result.user._json['id']
 
            try:
                if cnt < actCnt:
                    if action == "GOOD" : api.create_favorite(tweet_id)
                    if action == "RETWEET" : api.retweet(tweet_id)
                    if action == "FOLLOW" : api.create_friendship(user_id)
 
                else:
                    break
 
                cnt = cnt + 1
 
            except Exception as e:
                print(e)
 
 
# フォロー返し
def reFollow(api,my_user_id,maxReq=3):
 
    cnt = 0
 
    #フォロワー数とフォロー数を格納するリストを用意
    follower_list = []
    friend_list = []
    
    #ユーザ情報からフォロワー数を取得、格納
    follower_list = api.followers_ids(my_user_id)

    #ユーザ情報からフォロー数を取得、格納
    friend_list = api.friends_ids(my_user_id)
 
    result_list = list(set(follower_list) - set(friend_list))
 
    for user_id in result_list:
 
        cnt = cnt + 1
        print(user_id)
 
        try:
            if cnt < maxReq : api.create_friendship(user_id)
        except Exception as e:
            print(e)
 
 
if __name__ == "__main__":
    main()