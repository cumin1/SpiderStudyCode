import requests
from lxml import etree

url = "http://spiderbuf.cn/e02/list"
myheaders = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.203',
    'Cookie' : 'admin=789e9241f1fbdb5753a9b6a821e3d6f2'
}
payload = {'username':'admin','password':'123456'}

html = requests.post(url, headers=myheaders,data=payload).text
print(html)
root = etree.HTML(html)
trs = root.xpath('//tr')
f = open("datae02.txt","w",encoding="utf-8")
for tr in trs:
    tds = tr.xpath('./td')
    s = ''
    for td in tds:
        s = s + str(td.text) + '|'
    print(s)
    if s != '':
        f.write(s + '\n')
f.close()