# -*- coding: utf-8 -*-

import os

import telebot
import config
from telebot import types

bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=['start'])
def handle_start(message):
	user_markup = types.ReplyKeyboardMarkup()

	user_markup.row('Economics', 'NeuralNetworks')
	user_markup.row('Psychology', 'PythonBooks')
	bot.send_message(message.from_user.id, "Hello!")
	bot.send_message(message.from_user.id, "Choose books' genre you want to download", reply_markup=user_markup)


@bot.message_handler(content_types=['text'])
def handle_start(message):
	if message.text == "Economics":

		directory = "/home/alex/PycharmProjects/bot/books/economics"
		all_files_in_directory = os.listdir(directory)

		for book in all_files_in_directory:
			bot.send_message(message.from_user.id, all_files_in_directory)
			file = open(os.path.join(directory, book), 'rb')
			bot.send_document(message.from_user.id, file)
			file.close()
			print(directory)
			print(os.path.join(directory, book))


	elif message.text == "NeuralNetworks":

		directory = "/home/alex/PycharmProjects/bot/books/neural_networks"
		all_files_in_directory = os.listdir(directory)

		for book in all_files_in_directory:
			bot.send_message(message.from_user.id, all_files_in_directory)
			file = open(os.path.join(directory, book), 'rb')
			bot.send_document(message.from_user.id, file)
			file.close()
			print(directory)
			print(os.path.join(directory, book))


	elif message.text == "Psychology":

		directory = "/home/alex/PycharmProjects/bot/books/psychology"
		all_files_in_directory = os.listdir(directory)

		for book in all_files_in_directory:
			bot.send_message(message.from_user.id, all_files_in_directory)
			file = open(os.path.join(directory, book), 'rb')
			bot.send_document(message.from_user.id, file)
			file.close()
			print(directory)
			print(os.path.join(directory, book))


	elif message.text == "PythonBooks":

		directory = "/home/alex/PycharmProjects/bot/books/pybooks"
		all_files_in_directory = os.listdir(directory)

		for book in all_files_in_directory:
			bot.send_message(message.from_user.id, all_files_in_directory)
			file = open(os.path.join(directory, book), 'rb')
			bot.send_document(message.from_user.id, file)
			file.close()
			print(directory)
			print(os.path.join(directory, book))



bot.polling(none_stop=True)

directory = "/home/alex/PycharmProjects/bot/books/economics"
all_files_in_directory = os.listdir(directory)
for book in all_files_in_directory:
	file = open(os.path.join(directory, book), 'rb')
	print(os.path.join(directory, book))
