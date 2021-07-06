import telebot
from os import path
from config import API_TOKEN,admin_ip




bot = telebot.TeleBot(API_TOKEN, parse_mode=None)




class TelegaBot:


    def send_text(self,message):
        bot.send_message(admin_ip,message)
    

    def send_photo(self,pathToImage):

        if path.exists(pathToImage):
            image = open(pathToImage,"rb")
            bot.send_photo(admin_ip,image)
        else :
            print("файла не существует" + pathToImage)