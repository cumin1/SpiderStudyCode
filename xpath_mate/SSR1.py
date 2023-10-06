import requests
from lxml import etree
import re

url = "https://ssr1.scrape.center"
html = requests.get(url).text


root = etree.HTML(html)

xpath = "//img/@src"
imgs = root.xpath(xpath)

i = 1
for imgPlace in imgs:
    if re.match("^h.*", str(imgPlace)):
        print(imgPlace)
        response = requests.get(imgPlace)
        print(response.content)
        # 将图片内容保存到本地文件
        with open("../data/imgdata/SSR1_{}.jpg".format(i), "wb") as f:
            f.write(response.content)
            print("图片已保存")
        i += 1

