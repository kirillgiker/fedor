#link on pairs https://www.bitget.com/ru/spot/BTCUSDT?type=spot
#/html/body/div[4]/div/div/div/div[2]/div/div/div/div[3]/div/div[2] xpath for pairs
import requests, json, sqlite3
from bs4 import BeautifulSoup
from bot.db import Database
from db import Database
def Scrape_Pairs_Name():
    url = "https://api.bitget.com/api/spot/v1/public/currencies"
    response = requests.get(url)
    data = response.json()
    s = []
    for pair in data["data"]:
        s.append(pair["coinName"])
    return s
def Scrape_Orders(pair, proxy):
    pair = pair.replace('/', '')
    url = f"https://api.bitget.com/api/spot/v1/market/depth?symbol=" + pair + "_SPBL&limit=50"
    response = requests.get(url)
    data = response.json()["data"]
    return data
#cтакан class="bj3ny71RBfDxEisyLBeI" class="DucjjuqM2nt_HpBQzwUj"
#название токена class="SN7UY1iBNNtlyP7MCK7m"
db = Database('vkbot.db')
global base, cur
base = sqlite3.connect('vkbot.db')
db.__init__

