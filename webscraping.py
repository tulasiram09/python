import time 
from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent

url = "https://www.amazon.in/s?k=mobile+phone+under+20000&crid=1B0TVXF23MU4K&sprefix=mobile%2Caps%2C194&ref=nb_sb_ss_ts-doa-p_2_6"

session = requests.Session()

headers = {
    'user-Agent': UserAgent().random,
    'Accept-Language' : 'en-US,en;q=0.9',
    'Accept-Encoding' : 'gzip,deflate,br',
    'Connection' : 'Keep-alive',
    'Referer' : 'https://www.google.com'
}
proxies = {
    "http" :"http://scraperapi:613709adbc3eb9fff09a9d6540d29b74@proxy-server.scraperapi.com:8001"
}

time.sleep(2)
r = session.get(url,proxies=proxies,headers=headers)
print(r.status_code)

with open("flipkart.html","w",encoding="utf-8") as f:
    f.write(r.text)
print(r.text)