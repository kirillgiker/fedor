#link on pairs https://www.bitget.com/ru/spot/BTCUSDT?type=spot
#/html/body/div[4]/div/div/div/div[2]/div/div/div/div[3]/div/div[2] xpath for pairs
import requests, time, sqlite3, random
from db import Database
def Scrape_Pairs_Name(proxy):
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
file = open("proxy.txt")
proxiesList = [line for line in file]
db = Database('main.db')
global base, cur
base = sqlite3.connect('main.db')
db.__init__
#db.add(1, "hqwe")
while True:
    pairsName = Scrape_Pairs_Name()
    for i in range(len(pairsName)):
        try:
            if not(db.examintation(pairsName[i])): # проверка на наличие в базе данных (в случае отстуствия)
                proxy = random.choice(proxiesList)
                db.add(i, pairsName[i])
                ordersAsksBids = Scrape_Orders(pairsName[i]+"USDT", proxy=proxy)
                asks = str(ordersAsksBids["asks"])
                bids = str(ordersAsksBids["bids"])
                asks_bids = "{'asks': "+ asks + ", 'bids': " + bids +"}"
                db.add_asks_bids(pairsName[i], asks_bids)
            else:
                proxy = random.choice(proxiesList)
                ordersAsksBids = Scrape_Orders(pairsName[i]+"USDT", proxy=proxy)
                asks = str(ordersAsksBids["asks"])
                bids = str(ordersAsksBids["bids"])
                asks_bids = "{'asks': "+ asks + ", 'bids': " + bids +"}"
                db.add_asks_bids(pairsName[i], asks_bids)
        except:
            continue
    time.sleep(60*5)