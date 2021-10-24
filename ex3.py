import requests

url='https://www.hasco.co.jp/jonessnowboards/'
r=requests.get(url)
print(r.status_code)
r.raise_for_status()

url='https://www.hasco.co.jp/jonessnowboards/_notexsist'
r=requests.get(url)
print(r.status_code)
r.raise_for_status()