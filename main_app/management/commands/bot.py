from django.core.management.base import BaseCommand
import telebot
import logging

from time import sleep
from dotenv import load_dotenv
from os import getenv

from...models import Client
from...serializer import ClientSerializer

load_dotenv()
bot = telebot.TeleBot(token=getenv('TOKEN'))


class Command(BaseCommand):
    help = 'bot'
    
    def handle():
        ...

    @bot.message_handler(commands=['start'])
    def cmd_start(message):
        bot.reply_to(message,'Привет, это телеграмм бот связанный с ритуальным сайтом. \t Что-бы подключиться к базе данных используйте команду /connect')

    @bot.message_handler(commands=['connect'])
    def cmd_connect(message):
        bot.reply_to(message, 'Вы подключились к базе данных, если будут приходить запросы через сайт они будут вам выгружаться\tБаза данных проверяеться примерно раз в 5 минут.')
        while True:
            clients = Client.objects.filter(send = True)
            serialized_data = ClientSerializer(clients)
            print(serialized_data.data, 'В телеграмм боте')

            for data in serialized_data.data:
                bot.send_message(message, 'Имя: {}, Номер:{}'.format(data['name'], data['phone']))

            clients.update(send = False)
            
            sleep(1)
    logger = telebot.logger
    telebot.logger.setLevel(logging.INFO)
    bot.infinity_polling()