from aiowebsocket.converses import AioWebSocket
import asyncio
import requests
import bs4
import websockets


# url = "https://websocket1.scrape.center/"
#
# response = requests.get(url)
# print(response.status_code)
# html = response.text
# soup = bs4.BeautifulSoup(html, 'html.parser')
# print(soup.prettify())
# with open("../data/websocket1.html","wb") as f:
#     f.write(soup.prettify().encode())
with websockets.connect('wss://websocket1.scrape.center/websocket') as websocket:
    # 发送消息到服务器
    websocket.send("Hello, Server!")