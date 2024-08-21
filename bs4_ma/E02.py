import requests
from bs4 import BeautifulSoup

url = "http://spiderbuf.cn/playground/e02/list"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.203',
    'Cookie':'admin=c1aadc76462864c78a581ddce4bdc9f6'
}
payload = {
    'username':'admin',
    'password':'123456'
           }

response = requests.get(url,headers=headers,data=payload)
soup = BeautifulSoup(response.text,"html.parser")

print(response.text)