import pandas as pd
import requests
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import json

# 要搜索的关键词 当前时间戳（以毫秒为单位）
keyword = '海南珑达昌科技有限公司'
timestamp = int(time.time() * 1000)
params = {
    'keyword': keyword,
    'timestamp': timestamp
}

Headers = {
    'Content-Type': 'application/json',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.203',
    "Cookie": "app-uuid=WEB-5702E669F8A84D2A87CD13F4F1194C0A; app-device=WEB; token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwYXNzd29yZCI6IjdmMDgwMWQ1MWViNzUxOGZjYTIwYzdjNDU1MWE2Nzk1IiwiZXhwIjoxNzI0MjUxOTE1LCJ1c2VySWQiOjMxODMyOSwidXVpZCI6Ijc0OWFjODk4LTcyNmMtNGE3YS05MTg2LTBjZGI5ZmNmZDM3ZSIsInVzZXJuYW1lIjoiMTk5MjE1OTA3NzMifQ.cg6B3lXbRpBSD_CN3_Ot7PgL_cnkStqWvGMuJh-cUIk; userinfo=%7B%22inviteCode%22%3A%229983692BB1D5B7CD%22%2C%22nickName%22%3A%2219921590773%22%2C%22isVip%22%3Atrue%2C%22vipStatus%22%3A%22vip%22%2C%22vipEndTime%22%3A%222025-08-21%22%2C%22mobile%22%3A%2219921590773%22%2C%22email%22%3Anull%2C%22timestamp%22%3A1724250115203%7D; first-authorization=1724250115203"
}
base_url = "https://www.riskbird.com"
search_url = "https://www.riskbird.com/riskbird-api/newSearch"
# 请求体（数据）
payload = {
    "queryType": "1",
    "searchKey": keyword,
    "pageNo": 1,
    "range": 10,
    "selectConditionData": "{\"regionid\":\"\",\"status\":\"\",\"nicid\":\"\",\"sort_field\":\"\"}"
}


response = requests.post(url=search_url, headers=Headers,json=payload)
# 获取响应 JSON 数据
response_data = response.json()

# 提取 entid 和 fuzzyId
entid = response_data['data']['list'][0].get('entid', None)
# 提取 fuzzyId
fuzzyId = response_data['data'].get('fuzzyId', None)

print('entid:', entid)
print('fuzzyId:', fuzzyId)

# 拼凑目标页面url
need_url = base_url + f"/ent/{keyword}.html?entid={entid}&fuzzyId={fuzzyId}&position=1"

response_ = requests.get(need_url,headers=Headers)

from bs4 import BeautifulSoup

soup = BeautifulSoup(response_.text, 'html.parser')

# 查找第一个匹配的元素
element = soup.select_one('.xs-clip-text.xs-clip-on.info-basic-grow-bold')
if element:
    # 提取文本内容
    text = element.get_text(separator=' ', strip=True)

    status_keywords = ['在营', '不在营']  # 可以根据实际情况增加其他状态

    # 提取公司名称和状态
    for keyword in status_keywords:
        if keyword in text:
            company_name = text.split(keyword)[0].strip()
            status = keyword
            break
    else:
        # 如果没有找到状态，默认状态为空
        company_name = text.strip()
        status = '未知'

    print('Company Name:', company_name)
    print('Status:', status)
else:
    print('No matching element found.')



# 找到 ID 为 __NUXT_DATA__ 的 <script> 标签
script_tag = soup.find('script', id='__NUXT_DATA__')

# 提取并处理文本内容
if script_tag:
    script_content = script_tag.string.strip()

    try:
        # 尝试将文本内容解析为 JSON
        json_data = json.loads(script_content)

        # 如果数据是数组，则将其作为列表返回
        if isinstance(json_data, list):
            print(json_data)
        else:
            print('JSON 数据不是一个数组')
    except json.JSONDecodeError as e:
        print('无法解析 JSON 数据:', e)
else:
    print('未找到 ID 为 __NUXT_DATA__ 的 <script> 标签')

# company 21