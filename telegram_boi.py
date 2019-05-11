#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import telebot
from telebot import * 
import datetime
from time import sleep
token = "You'r_secret_token_here"
now = datetime.datetime.now()
today = now.day
hour = now.hour
bot = telebot.TeleBot(token)
markup_yes_no = types.ReplyKeyboardMarkup(row_width=2)
itembtn1 = types.KeyboardButton('Yes')
itembtn2 = types.KeyboardButton('No')
markup_yes_no.add(itembtn1, itembtn2)
markup_remove = types.ReplyKeyboardRemove(selective=False)

def greeting(message, name):
	if 6 <= hour < 12:
		bot.send_message(message.chat.id, 'Good morning, {}!'.format(name))			
	elif 12 <= hour < 17:
		bot.send_message(message.chat.id, 'Good day, {}!'.format(name))			
	elif 17 <= hour < 23:
		bot.send_message(message.chat.id, 'Good evening, {}!'.format(name))			
	elif 23 <= hour < 6:
		bot.send_message(message.chat.id, 'Good night, {}!'.format(name))

@bot.message_handler(commands=['set_alarm'])
def alarm(message):	
	bot.send_message(message.chat.id, "I also know how to wake you up with messages, until you write me a passphrase. It can be just a word, a sentence or a couplet of a song. Your choice. Set a passphrase?", reply_markup=markup_yes_no)
	bot.register_next_step_handler(message, if_alarm)
	

def if_alarm(message):
	markup_yes = types.ReplyKeyboardMarkup(row_width=2)
	button1 = types.KeyboardButton('Yes')
	markup_yes.add(button1)
	if message.text.lower() == "yes":
		bot.send_message(message.chat.id, 'Fine. Please enter a passphrase. The default passphrase is "Good morning!". If you want to leave the default phrase, just click on "yes", otherwise - enter your phrase ', reply_markup=markup_yes)
		bot.register_next_step_handler(message, set_alarm)
	elif message.text.lower() == "no":
		bot.send_message(message.chat.id, 'Okay. If you need help, just click on the "/" and select the option help', reply_markup=markup_remove)
	else:
		bot.send_message(message.chat.id, 'I can not understand you ... Please select one of the options below.', reply_markup=markup_yes_no)
		bot.register_next_step_handler(message, if_alarm)
						
	
def set_alarm(message):
	phrase = "Good morning!"
	if message.text.lower() != "yes":
		phrase = message.text
	bot.send_message(message.chat.id, 'The code phrase "{}" was successfully applied. Would you like to set the alarm now?'.format(phrase), reply_markup=markup_yes_no)
	bot.register_next_step_handler(message, answer)

def answer(message):
	if message.text.lower() == "yes":
		bot.send_message(message.chat.id, 'What time to wake you up?', reply_markup=markup_remove)
		bot.register_next_step_handler(message, users_alarm)
	elif message.text.lower() == "no":
		bot.send_message(message.chat.id, 'Developing...', reply_markup=markup_remove)
	else:
		bot.send_message(message.chat.id, 'Я вас не понимаю. Пожалуйста, нажмите на кнопки ниже', reply_markup=markup_remove)

def users_alarm(message):
	bot.send_message(message.chat.id, 'Developing...', reply_markup=markup_remove)

@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
	bot.send_message(message.chat.id, 'Dear {}! As long as I can only display this help, say hello and set the alarm ... Greet me and I will answer you :)'.format(message.from_user.first_name))

@bot.message_handler(content_types=["text"])
def say_hello(message): 
	greetings = ('здравствуй', 'привет', 'ку', 'здорово', 'приветули','салам','салам пополам', 'здравствуйте','приветствую','добрый день','доброе утро','добрый вечер','хай','hi','hello','хеллоу','хелоу','здорова','здарова', 'hi','hello','good day','good morning', 'good evening', 'good night') 
	if message.text.lower() in greetings:
		greeting(message, message.from_user.first_name)
	print (message)

if __name__ == '__main__':
	bot.polling(none_stop=True)
