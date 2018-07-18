# -*- coding: utf-8 -*-

import os

import config
import telebot
import book_dictionary
import cherrypy
from telebot import types

bot = telebot.TeleBot(config.token)

WEBHOOK_HOST = '185.103.110.156'
WEBHOOK_PORT = 443  # 443, 80, 88 или 8443 (порт должен быть открыт!)
WEBHOOK_LISTEN = '0.0.0.0'  # На некоторых серверах придется указывать такой же IP, что и выше

WEBHOOK_SSL_CERT = '../webhook_cert.pem'  # Путь к сертификату
WEBHOOK_SSL_PRIV = '../webhook_pkey.pem'  # Путь к приватному ключу

WEBHOOK_URL_BASE = "https://%s:%s" % (WEBHOOK_HOST, WEBHOOK_PORT)
WEBHOOK_URL_PATH = "/%s/" % (config.token)

class WebhookServer(object):
    @cherrypy.expose
    def index(self):
        if 'content-length' in cherrypy.request.headers and \
                        'content-type' in cherrypy.request.headers and \
                        cherrypy.request.headers['content-type'] == 'application/json':
            length = int(cherrypy.request.headers['content-length'])
            json_string = cherrypy.request.body.read(length).decode("utf-8")
            update = telebot.types.Update.de_json(json_string)
            bot.process_new_updates([update])
            return ''
        else:
            raise cherrypy.HTTPError(403)


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

		directory = "../books/economics"
		all_files_in_directory = os.listdir(directory)

		for book in all_files_in_directory:
			bot.send_message(message.from_user.id, book_dictionary.economics[book])
			file = open(os.path.join(directory, book), 'rb')
			bot.send_document(message.from_user.id, file)
			file.close()
			print(directory)
			print(os.path.join(directory, book))


	elif message.text == "NeuralNetworks":

		directory = "../books/neural_networks"
		all_files_in_directory = os.listdir(directory)

		for book in all_files_in_directory:
			bot.send_message(message.from_user.id, book_dictionary.neural_networks[book])
			file = open(os.path.join(directory, book), 'rb')
			bot.send_document(message.from_user.id, file)
			file.close()
			print(directory)
			print(os.path.join(directory, book))


	elif message.text == "Psychology":

		directory = "../books/psychology"
		all_files_in_directory = os.listdir(directory)

		for book in all_files_in_directory:
			bot.send_message(message.from_user.id, book_dictionary.psychology[book])
			file = open(os.path.join(directory, book), 'rb')
			bot.send_document(message.from_user.id, file)
			file.close()
			print(directory)
			print(os.path.join(directory, book))


	elif message.text == "PythonBooks":

		directory = "../books/pybooks"
		all_files_in_directory = os.listdir(directory)

		for book in all_files_in_directory:
			bot.send_message(message.from_user.id, book_dictionary.pybooks[book])
			file = open(os.path.join(directory, book), 'rb')
			bot.send_document(message.from_user.id, file)
			file.close()
			print(directory)
			print(os.path.join(directory, book))


bot.remove_webhook()

 # Ставим заново вебхук
bot.set_webhook(url=WEBHOOK_URL_BASE + WEBHOOK_URL_PATH,
                certificate=open(WEBHOOK_SSL_CERT, 'r'))

cherrypy.config.update({
    'server.socket_host': WEBHOOK_LISTEN,
    'server.socket_port': WEBHOOK_PORT,
    'server.ssl_module': 'builtin',
    'server.ssl_certificate': WEBHOOK_SSL_CERT,
    'server.ssl_private_key': WEBHOOK_SSL_PRIV
})


cherrypy.quickstart(WebhookServer(), WEBHOOK_URL_PATH, {'/': {}})