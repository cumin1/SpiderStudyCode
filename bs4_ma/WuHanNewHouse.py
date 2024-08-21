import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd

# 初始化 WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

base_url="https://wuhan.newhouse.fang.com"
myheaders = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.203'
}

year_list = ['202402', '202403', '202404', '202405', '202406', '202407', '202408', '202409', '202410', '202411', '202412', '202501']
select_house_url = "/house/saledate/"

data_rows = []

for year in year_list:
    house_url = base_url + select_house_url + year + ".htm"
    driver.get(house_url)  # 替换成目标网址
    time.sleep(5)
    for i in range(2):
        # 获取当前页面的信息
        content = driver.page_source
        soup = BeautifulSoup(content, "html.parser")
        # 查找所有<li>标签
        li_elements = soup.find_all('li')
        # 遍历每个<li>标签，获取其中class为"clearfix"的<div>元素
        for li in li_elements:
            clearfix_div = li.find('div', class_='nlc_details')
            if clearfix_div:
                # 楼盘名
                house_name = clearfix_div.find('div', class_='nlcd_name').find('a').text

                # 户型和面积
                house_type_area = clearfix_div.find('div', class_='house_type clearfix').get_text(strip=True)

                # 是否在售
                sale_status = clearfix_div.find('div', class_='fangyuan').find('span').text

                # 价格信息
                price = clearfix_div.find('div', class_='nhouse_price').get_text(strip=True)

                # 客服电话
                if (clearfix_div.find('div', class_='tel')):
                    tel = clearfix_div.find('div', class_='tel').find('p').text.strip()
                else:
                    tel = ''

                # 开盘时间
                if clearfix_div.find('div', class_='house_typea'):
                    opening_time = clearfix_div.find('div', class_='house_typea').get_text(strip=True)
                else:
                    opening_time = ''

                # 打印信息
                print(f"楼盘名: {house_name}")
                print(f"户型和面积: {house_type_area}")
                print(f"是否在售: {sale_status}")
                print(f"价格信息: {price}")
                print(f"客服电话: {tel}")
                print(f"开盘时间: {opening_time}")
                print("-" * 50)

                # 生成一些模拟数据
                data_row = {
                    'house_name': house_name,
                    'house_type_area': house_type_area,
                    'sale_status': sale_status,
                    'price': price,
                    'tel': tel,
                    'opening_time': opening_time,
                    'year_month' : year
                }
                data_rows.append(data_row)

        try:
            next_page_button = driver.find_element(By.XPATH, '//a[@class="next" and @data-page="2"]')
            if next_page_button:
                # 滚动到元素可见
                driver.execute_script("arguments[0].scrollIntoView(true);", next_page_button)
                time.sleep(3)
                driver.execute_script("arguments[0].click();", next_page_button)
                time.sleep(6)
            else:
                print("没有找到下一页按钮或出现错误:")
                break
        except Exception as e:
            print("没有找到下一页按钮:",e)
            continue

driver.quit()

# 将数据列表转换为DataFrame
df = pd.DataFrame(data_rows)

# 指定Excel文件路径
excel_path = 'saledate_house.xlsx'

# 写入Excel文件，如果文件已存在则会被覆盖
df.to_excel(excel_path, index=False)  # index=False表示不保存行索引