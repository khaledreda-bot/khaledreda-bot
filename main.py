import requests
import time
from telegram import Bot

TOKEN = "6387546779:AAGtTC44Po4sAomAKPH4DybAjNf3yT6F2dc"
CHAT_ID = "7832886101"

bot = Bot(token=TOKEN)

def get_price():
    url = "https://api.twelvedata.com/price?symbol=XAU/USD&apikey=demo"
    try:
        response = requests.get(url)
        price = float(response.json().get("price", 0))
        return price
    except:
        return 0

last_signal = None

while True:
    price = get_price()
    if price == 0:
        continue

    if price > 2400 and last_signal != "sell":
        bot.send_message(chat_id=CHAT_ID, text=f"إشارة بيع الذهب XAUUSD عند {price}")
        last_signal = "sell"

    elif price < 2300 and last_signal != "buy":
        bot.send_message(chat_id=CHAT_ID, text=f"إشارة شراء الذهب XAUUSD عند {price}")
        last_signal = "buy"

    time.sleep(60)
