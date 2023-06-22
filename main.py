import telebot
import requests

TOKEN = '***'

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "welcome to Digital Currency Price Teller Robot")


@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "send the digital currency symbol and get its price easily")


@bot.message_handler(func=lambda m: True)
def show_price(message):
    symbol = message.text.upper()
    response = requests.get(f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}")
    if response.status_code == 200:
        data = response.json()
        bot.reply_to(message, f"{data['symbol']} price is: {data['price']}")
    else:
        bot.reply_to(message, f"couldn't find anything, are you sure about this '{symbol}' symbol?")


bot.infinity_polling()
