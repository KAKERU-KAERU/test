from selenium import webdriver
import pytz
import datetime
import time 
from selenium.webdriver.chrome.options import Options
import requests

TOKEN='AMYpX1Qzt7wAIWL69NthSNYS9OQu60YNp5mHcqffOwC'
api_url='https://notify-api.line.me/api/notify'

Time=datetime.datetime.now(pytz.timezone('Asia/Tokyo'))
Time=time.strftime('%h/%d/%Y  %H:%M')

options = Options()
options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
options.add_argument('--headless')
driver = webdriver.Chrome(chrome_options=options, executable_path=r'C:\Users\mizun\OneDrive\MyPythonProject\Mypandas\chromedriver.exe')

Key='Air Pods Pro'
price=30000
url='https://www.amazon.co.jp/Apple-%E3%82%A2%E3%83%83%E3%83%97%E3%83%AB-MWP22J-A-AirPods/dp/B07ZPS4FSW/ref=sr_1_1?adgrpid=121418466208&dchild=1&hvadid=492492587925&hvdev=c&hvqmt=e&hvtargid=kwd-899080190815&hydadcr=14996_10904232&jp-ad-ap=0&keywords=airpods+pro+amazon&qid=1632488268&sr=8-1'

driver.get(url)
driver.implicitly_wait(5)
element=driver.find_element_by_id('priceblock_ourprice').text
driver.quit()
element=element.replace('￥','')
element=element.replace(',','')
element=int(element)

if element < price:
    print(element)

    text={f"\n\n{Key}\n\n{element}円\n\n{Time}\n\n{url}"}
    send_contents=text
    TOKEN_dic={'Authorization':'Bearer'+' '+TOKEN}#SPACE!!
    send_dic={'message':send_contents}
    print(TOKEN_dic)
    print(send_dic)
    requests.post(api_url,headers=TOKEN_dic,data=send_dic)
    time.sleep(3)

else:
    pass