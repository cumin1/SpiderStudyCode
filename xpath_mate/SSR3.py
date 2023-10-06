import requests


url = "https://spa1.scrape.center/api/movie/?limit=10&offset=0" # 该请求是后端服务器的接口
response = requests.get(url)
if response.status_code == 200:
    print("爬取成功")
    html = response.text
    print(html)
    with open("../data/SSR3.txt","w") as f:
        f.write(html)

else:
    print("爬取失败")
    print("响应码为{}".format(response.status_code))



# root = etree.HTML(html)
#
# xpath = "//img/@src"
# imgs = root.xpath(xpath)



