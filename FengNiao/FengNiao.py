import pandas as pd
import requests
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

Headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.203',
        "Cookie": "app-uuid=WEB-876E35354DDE44A59C79D0EF86E8B33B; app-device=WEB; userinfo=%7B%22inviteCode%22%3A%229983692BB1D5B7CD%22%2C%22nickName%22%3A%2219921590773%22%2C%22isVip%22%3Atrue%2C%22vipStatus%22%3A%22vip%22%2C%22vipEndTime%22%3A%222025-08-21%22%2C%22mobile%22%3A%2219921590773%22%2C%22email%22%3Anull%2C%22timestamp%22%3A1724246915761%7D; first-authorization=1724246915761; token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwYXNzd29yZCI6IjdmMDgwMWQ1MWViNzUxOGZjYTIwYzdjNDU1MWE2Nzk1IiwiZXhwIjoxNzI0MjUwNTYxLCJ1c2VySWQiOjMxODMyOSwidXVpZCI6IjZkOWQ1MWM1LTU2ZmMtNGIzNC04M2MwLWViZTViMTQ1M2FjYiIsInVzZXJuYW1lIjoiMTk5MjE1OTA3NzMifQ.AaibsVaz45Fv_whZY_ey4vTf7WOmNvOtef-lau-Uo-k"
}
base_url = "https://www.riskbird.com/"
search_url = "https://www.riskbird.com/search/company"

def main():
    # 读取Excel文件
    df = pd.read_excel('test.xlsx', header=None)
    col1_list = df.iloc[:, 0].tolist()  # 第一列数据
    col2_list = df.iloc[:, 1].tolist()  # 第二列数据
    print("第一列数据:", col1_list)
    print("第二列数据:", col2_list)

    # 要搜索的关键词 当前时间戳（以毫秒为单位）
    keyword = col2_list[0]
    timestamp = int(time.time() * 1000)

    local_chromedriver_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
    service = Service(executable_path=local_chromedriver_path)
    driver = webdriver.Chrome(service=service)

    # 打开目标网址
    driver.get(f'https://www.riskbird.com/search/company?keyword={keyword}&timestamp={timestamp}')

    # 等待页面加载完成
    time.sleep(3)  # 等待 3 秒，可以根据实际情况调整

    elements = driver.find_elements(By.CSS_SELECTOR, 'div.company-name a')

    # 遍历找到的 a 标签并获取 href 属性
    for element in elements:
        href = element.get_attribute('href')
        print(href)

if __name__ == '__main__':
    main()
