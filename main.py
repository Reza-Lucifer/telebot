import os
import telebot
from keep_alive import keep_alive

TOKEN = os.getenv("7298261967:AAE6HqKW1m3KMZD8vpMR3y1MJn_p8SRa6Kc")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "ربات فعال است روی Render ✅")

print("ربات در حال اجراست...")
keep_alive()
bot.infinity_polling()