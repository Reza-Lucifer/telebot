import os
import telebot
from keep_alive import keep_alive

TOKEN = os.getenv("TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "ربات فعال است روی Render ✅")

print("ربات در حال اجراست...")
keep_alive()
bot.infinity_polling()
