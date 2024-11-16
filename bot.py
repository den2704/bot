import telebot
from telebot import types

bot = telebot.TeleBot('7722160124:AAHG4GIJTQiDBphuKmgbH-YayjAhoApwi4g')

menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
about =  types.KeyboardButton("Что такое коррупция?")
history = types.KeyboardButton("История коррупции")
forms = types.KeyboardButton("Виды коррупции")
cor = types.KeyboardButton("Борьба с коррупцией в РФ")
against = types.KeyboardButton("Ответственность за коррупцию")
sign_up = types.KeyboardButton("Написать о факте проявления коррупции")
menu.add(about, history, forms, cor, against, sign_up)

back = types.ReplyKeyboardMarkup(resize_keyboard=True)
back_button = types.KeyboardButton("Назад")
back.add(back_button)

@bot.message_handler(commands=['start'])
def start_message(message):
	bot.send_message(message.chat.id, "Добро пожаловать!")
	bot.send_message(message.chat.id, "Антикоррупционный чат-бот к Вашим услугам! Пожалуйста, выберите действие с помощью кнопок", reply_markup=menu)

@bot.message_handler(content_types=['text'])
def text_message(message):
	if message.text == "Назад":
		bot.send_message(message.chat.id, "Что Вас интересует?", reply_markup=menu)
	elif message.text == "Что такое коррупция?":
		file = open('cor.txt', 'r', encoding='utf-8')
		content = file.read()		
		bot.send_message(message.chat.id, content, reply_markup=back)
	elif message.text == "История коррупции":
		file = open('his.txt', 'r', encoding='utf-8')
		content1 = file.read()
		bot.send_message(message.chat.id, content1, reply_markup=back)
	elif message.text == "Виды коррупции":
		file = open('forms.txt', 'r', encoding='utf-8')
		content2 = file.read()
		bot.send_message(message.chat.id, content2, reply_markup=back)
	elif message.text == "Борьба с коррупцией в РФ":
		file = open('cor_rf.txt', 'r', encoding='utf-8')
		content3 = file.read()
		bot.send_message(message.chat.id, content3, reply_markup=back)
	elif message.text == "Ответственность за коррупцию":
		file = open('pravo.txt', 'r', encoding='utf-8')
		content4 = file.read()
		bot.send_message(message.chat.id, content4, reply_markup=back)
	elif message.text == "Написать о факте проявления коррупции":
		bot.send_message(message.chat.id, "Напишите нам о факте проявления коррупции", reply_markup=types.ReplyKeyboardRemove())
		bot.register_next_step_handler(message, forward)

def forward(message):
	bot.forward_message(chat_id = '@Kazan_against_corruption', from_chat_id = message.chat.id, message_id=message.id)
	bot.send_message(message.chat.id, "Спасибо за Ваше обращение!", reply_markup=menu)

bot.infinity_polling()