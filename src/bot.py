import telebot
from src import config
from src import book_dictionary

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['start','help'])
def send_welcome(message):
	bot.reply_to(message, "Oh, hey there!")





bot.polling()