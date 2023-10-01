import requests
from lxml import etree

url = "http://spiderbuf.cn/s02/"
myheaders = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36'
}

html = requests.get(url, headers=myheaders).text

root = etree.HTML(html)
trs = root.xpath('//tr')
f = open("data02.txt","w",encoding="utf-8")
for tr in trs:
    tds = tr.xpath('./td')
    s = ''
    for td in tds:
        s = s + str(td.text) + '|'
    print(s)
    if s != '':
        f.write(s + '\n')
f.close()