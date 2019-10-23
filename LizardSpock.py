# -*- coding:utf-8 -*-
import telebot
import json
from random import randrange, uniform

# randrange gives you an integral value


bot = telebot.TeleBot("571633707:AAHooMJqG3oG740HqTkCTcjj30_zKyFZCS4")

json_keyboard = json.dumps({'keyboard': [["Si"],["No"]],
							'one_time_keyboard':True,
							'resize_keyboard':True})

json_keyboard1 = json.dumps({'keyboard': [["Piedra"],["Papel"],["Tijera"],["Lagarto"],["Spock"]],
							'one_time_keyboard':True,
							'resize_keyboard':True})
#\Funcionamient juego

def tiradaComputer(argument):
	switcher = {
        1: "Piedra",
        2: "Papel",
        3: "Tijera",
        4: "Lagarto",
        5: "Spock",

    }
	movPc = switcher.get(argument)
	print movPc


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.send_message(message.chat.id, "Bienvenido, Estas listo? ",reply_markup=json_keyboard)
#\nEmpieza el juego \nPiedra, Papel, Tijera, Lagarto, Spock...""


@bot.message_handler(func=lambda message:True)
def empiezaPartida(message):
		if str(message.text) == str("Si"):
			bot.send_message(message.chat.id, "Empieza el juego \nPiedra, Papel, Tijera, Lagarto, Spock...",reply_markup=json_keyboard1)
			computer = randrange(1, 6)
			tiradaComputer(computer)
		elif str(message.text) == "No":
			bot.send_message(message.chat.id, "otra vez sera")

	#bot.send_message(message.chat.id, message.text)

#Para que no finalize el programa i se mantenga a la espera de mas informacion
bot.polling()
