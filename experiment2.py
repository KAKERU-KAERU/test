import requests
import datetime
import pytz
from bs4 import BeautifulSoup
import pandas as pd

TOKEN='NsqAux4yztBtnfrkmG68CI6gg5B6zcxNFHwhlT5GEPB'
api_url='https://notify-api.line.me/api/notify'

time=datetime.datetime.now(pytz.timezone('Asia/Tokyo'))
time=time.strftime('%m/%d/%Y')

#TEXT 
##################################################################################

##################################################################################
text='TEST'

send_contents=str((time)+'\n'+text)

TOKEN_dic={'Authorization':'Bearer'+' '+TOKEN}#SPACE!!
send_dic={'message':send_contents}
print(TOKEN_dic)
print(send_dic)

image_file=r'image_folder\KIJIMADAIRA.jpgidou.jpg'
binary=open(image_file,mode='rb')
image_dic={'imageFile':binary}

requests.post(api_url,headers=TOKEN_dic,data=send_dic,files=image_dic)