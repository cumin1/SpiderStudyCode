import requests
from bs4 import BeautifulSoup

url = "http://spiderbuf.cn/playground/s05"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.203'
}
base_url = "http://spiderbuf.cn"

def load_img(url):
    reponse = requests.get(url)
    # print(reponse.text)

    soup = BeautifulSoup(reponse.text,"html.parser")
    img_list = soup.select(".img-responsive")

    imgs = []
    for img in img_list:
        imgs.append(img['src'])
    print(imgs)
    for item in imgs:
        img_data = requests.get('http://spiderbuf.cn' + item, headers=headers).content
        path = "./pictures/" + str(item).replace('/','')
        img = open(path, 'wb')
        img.write(img_data)
        img.close()
        print(path,"下载完毕!")

def main():
    load_img(url)

if __name__ == '__main__':
    main()