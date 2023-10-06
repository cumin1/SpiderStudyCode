import requests
from lxml import etree
import re

def get_pages(url,xpath):
    html = requests.get(url).text
    root = etree.HTML(html)
    result_lists = root.xpath(xpath)
    result = result_lists[0].xpath("string(.)")
    result = re.findall(r'\d+', result)
    return result[0]


header_list = []
score_list = []

pages = get_pages("https://ssr1.scrape.center","//span[@class='el-pagination__total']")

for account in range(1,int(pages) + 1):
    url = "https://ssr1.scrape.center/page/{}".format(account)
    html = requests.get(url).text
    root = etree.HTML(html)


    header_ori_xpath = "//div[@class='p-h el-col el-col-24 el-col-xs-9 el-col-sm-13 el-col-md-16']"
    header_xpath = "/a[@class='name']"
    score_ori_xpath = "//div[@class='el-col el-col-24 el-col-xs-5 el-col-sm-5 el-col-md-4']"
    score_xpath = "/p[@class='score m-t-md m-b-n-sm']"

    headers = root.xpath(header_ori_xpath+header_xpath)
    scores = root.xpath(score_ori_xpath+score_xpath)

    for header in headers:
        text = header.xpath("string(.)").replace(" ", "").replace("\n", "").replace("\t", "")
        header_list.append(text)

    for score in scores:
        text = score.xpath("string(.)").replace(" ", "").replace("\n", "").replace("\t", "")
        score_list.append(text)

    print(header_list)
    print(score_list)

    for i in range(header_list.__len__()):
        with open("../data/SSR1_1.txt","a+",encoding="utf-8") as f:
            data = f"""{header_list[i]} | {score_list[i]} \n"""
            f.write(data)



