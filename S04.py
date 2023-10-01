import requests
from lxml import etree

ori_url = "http://spiderbuf.cn/s04/?pageno=%d"
myheaders = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36'
}

for i in range(1, 6):
    url = ori_url % i
    html = requests.get(url, headers=myheaders).text
    print(html)

    root = etree.HTML(html)
    trs = root.xpath('//tr')
    f = open("data04_%d.txt" % i, "w", encoding="utf-8")
    for tr in trs:
        tds = tr.xpath('./td')
        s = ''
        for td in tds:
            s = s + str(td.xpath('string(.)')) + '|'  # 不管标签之中有多少个标签 都可以把内部的文本内容取出来
        print(s)
        if s != '':
            f.write(s + '\n')
    f.close()
