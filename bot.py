import telebot
from datetime import datetime
import os

today = datetime.now()
next = datetime(2025, 10, 30)
delta = next - today
token = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(token)
chnl = '@VoidOpa'
bot.edit_message_text(f"Осталось {delta.days}", chat_id=chnl, message_id = 186)
