# -*- coding: utf-8 -*-

import os

import config
import telebot
import book_dictionary
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

		directory = "/home/alexfox/libraryBot/books/economics"
		all_files_in_directory = os.listdir(directory)

		for book in all_files_in_directory:
			bot.send_message(message.from_user.id, book_dictionary.economics["all_files_in_directory"])
			file = open(os.path.join(directory, book), 'rb')
			bot.send_document(message.from_user.id, file)
			file.close()
			print(directory)
			print(os.path.join(directory, book))


	elif message.text == "NeuralNetworks":

		directory = "/home/alexfox/libraryBot/books/neural_networks"
		all_files_in_directory = os.listdir(directory)

		for book in all_files_in_directory:
			bot.send_message(message.from_user.id, book_dictionary.neural_networks["all_files_in_directory"])
			file = open(os.path.join(directory, book), 'rb')
			bot.send_document(message.from_user.id, file)
			file.close()
			print(directory)
			print(os.path.join(directory, book))


	elif message.text == "Psychology":

		directory = "/home/alexfox/libraryBot/books/psychology"
		all_files_in_directory = os.listdir(directory)

		for book in all_files_in_directory:
			bot.send_message(message.from_user.id, book_dictionary.psychology["all_files_in_directory"])
			file = open(os.path.join(directory, book), 'rb')
			bot.send_document(message.from_user.id, file)
			file.close()
			print(directory)
			print(os.path.join(directory, book))


	elif message.text == "PythonBooks":

		directory = "/home/alexfox/libraryBot/books/pybooks"
		all_files_in_directory = os.listdir(directory)

		for book in all_files_in_directory:
			bot.send_message(message.from_user.id, book_dictionary.pybooks["all_files_in_directory"])
			file = open(os.path.join(directory, book), 'rb')
			bot.send_document(message.from_user.id, file)
			file.close()
			print(directory)
			print(os.path.join(directory, book))


bot.polling(none_stop=True)
