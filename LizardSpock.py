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

def tiradaComputer(plyer, argument):
	switcher = {
        1: "Piedra",
        2: "Papel",
        3: "Tijera",
        4: "Lagarto",
        5: "Spock",

    }
	movPc = switcher.get(argument)
	print movPc

	print plyer
	if str(plyer) == movPc:
		print "Empate"

	elif str(plyer) == "Piedra":
		if movPc == "Papel":
			print "Has perdido"
		elif movPc == "Tijera":
			print "Has ganado"
		elif movPc == "Lagarto":
			print "Has ganado"
		elif movPc == "Spock":
			print "Has perdido"

	elif str(plyer) == "Papel":
		if movPc == "Piedra":
			print "Has ganado"
		elif movPc == "Tijera":
			print "Has perdido"
		elif movPc == "Lagarto":
			print "Has perdido"
		elif movPc == "Spock":
			print "Has ganado"

	elif str(plyer) == "Tijera":
		if movPc == "Piedra":
			print "Has perdido"
		elif movPc == "Papel":
			print "Has ganado"
		elif movPc == "Lagarto":
			print "Has ganado"
		elif movPc == "Spock":
			print "Has perdido"

	elif str(plyer) == "Lagarto":
		if movPc == "Papel":
			print "Has ganado"
		elif movPc == "Tijera":
			print "Has perdido"
		elif movPc == "Piedra":
			print "Has perdido"
		elif movPc == "Spock":
			print "Has ganado"

	elif str(plyer) == "Spock":
		if movPc == "Piedra":
			print "Has ganado"
		elif movPc == "Papel":
			print "Has perdido"
		elif movPc == "Lagarto":
			print "Has perdido"
		elif movPc == "Tijera":
			print "Has ganado"


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.send_message(message.chat.id, "Bienvenido, Estas listo? ",reply_markup=json_keyboard)
#\nEmpieza el juego \nPiedra, Papel, Tijera, Lagarto, Spock...""

#\Opciones
@bot.message_handler(regexp='Piedra')
def elije(message):

	computer = randrange(1, 6)
	tiradaComputer(message.text,computer)

@bot.message_handler(regexp='Papel')
def elije(message):

	computer = randrange(1, 6)
	tiradaComputer(message.text,computer)

@bot.message_handler(regexp='Tijera')
def elije(message):

	computer = randrange(1, 6)
	tiradaComputer(message.text,computer)

@bot.message_handler(regexp='Lagarto')
def elije(message):

	computer = randrange(1, 6)
	tiradaComputer(message.text,computer)

@bot.message_handler(regexp='Spock')
def elije(message):

	computer = randrange(1, 6)
	tiradaComputer(message.text,computer)


@bot.message_handler(func=lambda message:True)
def empiezaPartida(message):
	print message.text
	if str(message.text) == str("Si"):
		bot.send_message(message.chat.id, "Empieza el juego \nPiedra, Papel, Tijera, Lagarto, Spock...",reply_markup=json_keyboard1)


	elif str(message.text) == "No":
		bot.send_message(message.chat.id, "otra vez sera")



	#bot.send_message(message.chat.id, message.text)

#Para que no finalize el programa i se mantenga a la espera de mas informacion
bot.polling()
