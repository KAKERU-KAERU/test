import requests
import datetime
import pytz
from selenium import webdriver
import pandas as pd


TOKEN='AMYpX1Qzt7wAIWL69NthSNYS9OQu60YNp5mHcqffOwC'
api_url='https://notify-api.line.me/api/notify'

time=datetime.datetime.now(pytz.timezone('Asia/Tokyo'))
time=time.strftime('%m/%d/%Y')
#######################################################

#######################################################
pdf='https://www.hakubaescal.com/winter/common/pdf/gelande/gelandemap2021.pdf'
text=f"\nMAP\n{pdf}"


send_contents=str((time)+'\n'+text)

TOKEN_dic={'Authorization':'Bearer'+' '+TOKEN}#SPACE!!
send_dic={'message':send_contents}
print(TOKEN_dic)
print(send_dic)

image_file=r'png_image\cat.jpg'
binary=open(image_file,mode='rb')
image_dic={'imageFile':binary}

requests.post(api_url,headers=TOKEN_dic,data=send_dic,files=image_dic)