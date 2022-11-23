from telebot import TeleBot
import os
import setup

print(os.environ["BOT_API_KEY"])
bot = TeleBot(token=os.environ["BOT_API_KEY"])
SEARCH_API_KEY = os.environ["SEARCH_API_KEY"]
TG_ADMIN_ID = os.environ["TG_ADMIN_ID"]