import requests
from lxml import etree

url = "http://spiderbuf.cn/s01/"
html = requests.get(url).text

root = etree.HTML(html)
trs = root.xpath('//tr')
f = open("data01.txt","w",encoding="utf-8")
for tr in trs:
    tds = tr.xpath('./td')
    s = ''
    for td in tds:
        s = s + str(td.text) + '|'
    print(s)
    if s != '':
        f.write(s + '\n')
f.close()
