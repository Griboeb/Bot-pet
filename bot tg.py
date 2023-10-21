# import telebot
# from telebot import types
# from random import choice

# bot_token='6514568483:AAHanWMDjGyIPIZWAWrO1Y9FjPVp4FKCfZ0'
# bot=telebot.TeleBot(bot_token)

# def reading_file(filename):
#     with open(filename,'r',encoding='utf-8') as file:
#         line_list=file.readlines()
#     return line_list

# @bot.message_handler(commands=['start'])
# def welcome(message):
#     bot.send_message(message.chat.id,'Привет кого ты больше любишь?Оnghfdm /button')

# @bot.message_handler(commands=['button'])
# def button(message):
#     markuap=types.InlineKeyboardMarkup(row_width=1)
#     item1=types.InlineKeyboardButton('Кошки',callback_data='cats')
#     item2=types.InlineKeyboardButton('Собаки',callback_data='dogs')
#     markuap.add(item1,item2)
#     bot.send_message(message.chat.id,'кошки или собаки',reply_markup=markuap)

# @bot.add_callback_query_handler(func=lambda call:True)
# def callback(call):
#     if call.message:
#         if call.data=='cats':
#             fact=choice(cat_fact)
#             bot.send_message(call.message.chat.id,fact)
#         elif call.data=='dogs':
#             bot.send_message(call.message.chat.id,choice(Dogs_gy))





# cat_fact=reading_file('cats.txt')
# Dogs_gy=reading_file('cats.txt')

# bot.polling()



import telebot
from telebot import types
from random import choice

bot_token='6514568483:AAHanWMDjGyIPIZWAWrO1Y9FjPVp4FKCfZ0'
bot=telebot.TeleBot(bot_token)

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id,'2+2?Оnghfdm /button')

@bot.message_handler(commands=['button'])
def button(message):
    markuap=types.InlineKeyboardMarkup(row_width=1)
    item1=types.InlineKeyboardButton('4',callback_data='4')
    item2=types.InlineKeyboardButton('5',callback_data='5')
    markuap.add(item1,item2)
    bot.send_message(message.chat.id,'2+2',reply_markup=markuap)

@bot.add_callback_query_handler()
def callback(call):
    if call.message:
        if call.data=='4':
            print('True')
            bot.send_message(call.message.chat.id)
        elif call.data=='5':
            print('Fals')
            bot.send_message(call.message.chat.id)



bot.polling()


























# import requests
# import random

# bot_token='6514568483:AAHanWMDjGyIPIZWAWrO1Y9FjPVp4FKCfZ0'
# bot=telebot.TeleBot(token=bot_token)

# poke_api_url='https://pokeapi.co/api/v2/pokemon'

# @bot.message_handler(commands=['start'])
# def send_welkome(message):
#     bot.reply_to(message,'Пивет')

# @bot.message_handler(commands=['pokemon'])
# def send_pokemon_info(message):
#     poke_id=random(1,898)
#     url=poke_api_url+str(poke_id)

#     response=requests.get(url)
#     data=response.json()
   
#     if 'sprites' in data and 'font_default' in data['sprites']:
#         poke




# bot.polling()






















# import telebot
# bot_token='6514568483:AAHanWMDjGyIPIZWAWrO1Y9FjPVp4FKCfZ0'
# bot=telebot.TeleBot(token=bot_token)

# def read_cities(filename):

#     with open('cities.txt','r', encoding='utf-8') as file:
#         cities=[line.strip().lower()for line in file]
#     return cities_

# @bot.message_handler(commands=['start'])
# def str_messg(message):
#     bot.send_msg(message.chat.id,'привет,поиграем в города')


# def is_vaid()




# last_city={}

# import telebot
# bot_token='6514568483:AAHanWMDjGyIPIZWAWrO1Y9FjPVp4FKCfZ0'
# bot=telebot.TeleBot(token=bot_token)

# @bot.message_handler(commands=['start'])
# def start_message(message):
#     bot.reply_to(message, text:'Привет я твой бот')

# @bot.message_handler(func=lambda message:message=='Как дела?')
# def reply_to_hello(message):
#     bot
# bot.polling()