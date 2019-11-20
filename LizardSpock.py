# -*- coding:utf-8 -*-
import telebot
import json
from random import randrange, uniform
from multiprocessing import Process, Value, Array
import os
import sys
reload(sys)
sys.setdefaultencoding('utf8')
# randrange gives you an integral value


bot = telebot.TeleBot("571633707:AAHooMJqG3oG740HqTkCTcjj30_zKyFZCS4")
playerId = Value('i', 0)
json_keyboard = json.dumps({'keyboard': [["Si"],["No"]],
							'one_time_keyboard':True,
							'resize_keyboard':True})

json_keyboard1 = json.dumps({'keyboard': [["Piedra"],["Papel"],["Tijera"],["Lagarto"],["Spock"]],
							'one_time_keyboard':True,
							'resize_keyboard':True})

def checkFile(file_Id):
	return os.path.isfile(str(file_Id))
#\Funcionamient juego

def tiradaComputer(plyer, randomPc, playerId,playerName):
	#CONVIERTE RANDOM EN UNA DE LAS ELECCIONES

	switcher = {
        1: "Piedra",
        2: "Papel",
        3: "Tijera",
        4: "Lagarto",
        5: "Spock",
    }
	#----VARIABLES FUNCION
	puntos = 0
	movPc = switcher.get(randomPc)
	#----CHIVATOS
	print movPc
	print plyer
	#----

	#---- lista possibilidades
	if str(plyer) == movPc:
		bot.send_message(playerId,"Empate")
		puntos = 0.5
	elif str(plyer) == "Piedra":
		if movPc == "Papel":
			puntos = -1
			bot.send_message(playerId, "Papel\nHas perdido")
		elif movPc == "Tijera":
			puntos = 1
			bot.send_message(playerId, "Tijera\nHas ganado")
		elif movPc == "Lagarto":
			puntos = 1
			bot.send_message(playerId, "Lagarto\nHas ganado")
		elif movPc == "Spock":
			puntos = -1
			bot.send_message(playerId, "Spock\nHas perdido")

	elif str(plyer) == "Papel":
		if movPc == "Piedra":
			puntos = 1
			bot.send_message(playerId, "Piedra\nHas ganado")
		elif movPc == "Tijera":
			puntos = -1
			bot.send_message(playerId, "Tijera\nHas perdido")
		elif movPc == "Lagarto":
			puntos = -1
			bot.send_message(playerId, "Lagarto\nHas perdido")
		elif movPc == "Spock":
			puntos = 1
			bot.send_message(playerId, "Spock\nHas ganado")

	elif str(plyer) == "Tijera":
		if movPc == "Piedra":
			puntos = -1
			bot.send_message(playerId, "Piedra\nHas perdido")
		elif movPc == "Papel":
			puntos = 1
			bot.send_message(playerId, "Papel\nHas ganado")
		elif movPc == "Lagarto":
			puntos = 1
			bot.send_message(playerId, "Lagarto\nHas ganado")
		elif movPc == "Spock":
			puntos = -1
			bot.send_message(playerId, "Spock\nHas perdido")

	elif str(plyer) == "Lagarto":
		if movPc == "Papel":
			puntos = 1
			bot.send_message(playerId, "Papel\nHas ganado")
		elif movPc == "Tijera":
			puntos = -1
			bot.send_message(playerId, "Tijera\nHas perdido")
		elif movPc == "Piedra":
			puntos = -1
			bot.send_message(playerId, "Piedra\nHas perdido")
		elif movPc == "Spock":
			puntos = 1
			bot.send_message(playerId, "Spock\nHas ganado")

	elif str(plyer) == "Spock":
		if movPc == "Piedra":
			puntos = 1
			bot.send_message(playerId, "Piedra\nHas ganado")
		elif movPc == "Papel":
			puntos = -1
			bot.send_message(playerId, "Papel\nHas perdido")
		elif movPc == "Lagarto":
			puntos = -1
			bot.send_message(playerId, "Lagarto\nHas perdido")
		elif movPc == "Tijera":
			puntos = 1
			bot.send_message(playerId, "Tijera\nHas ganado")

	#playerId(playerId)

#-------FIN tiradaCom()puter()----
#def playerId(playerId):
	#GUARDA EN EL documentoPj

	if checkFile(str(playerId) + ".txt") == True:
		print "existe"

		documentoPl = open(str(playerId) + ".txt", "r+")
		lectura = documentoPl.readline().split(";")
		puntos = puntos + int(lectura[1])
		print lectura[1]
		print puntos

		documentoPj = open(str(playerId) + ".txt", "w+")
		documentoPj.write(playerName + ";" + str(puntos))
		documentoPj.close()
	else:
		print "NO existe"
		documentoPj = open(str(playerId) + ".txt", "w+")
		documentoPj.write(playerName + ";" + str(puntos))
		documentoPj.close()




@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.send_message(message.chat.id, "Bienvenido, Estas listo? ",reply_markup=json_keyboard)
	playerId.value = message.from_user.id
#\nEmpieza el juego \nPiedra, Papel, Tijera, Lagarto, Spock...""


#\CUANDO ELIGES UN MOVIMIENTO  LLAMA AL METODO tiradaComputer LE PASA EL message(TU ELECCION), computer(RANDOM TIRADA PC), message(ID USUARIO JUGANDO)
@bot.message_handler(regexp='Piedra')
def elije(message):

	computer = randrange(1, 6)
	tiradaComputer(message.text,computer, message.from_user.id,message.from_user.first_name)

@bot.message_handler(regexp='Papel')
def elije(message):

	computer = randrange(1, 6)
	tiradaComputer(message.text,computer, message.from_user.id,message.from_user.first_name)

@bot.message_handler(regexp='Tijera')
def elije(message):

	computer = randrange(1, 6)
	tiradaComputer(message.text,computer, message.from_user.id,message.from_user.first_name)

@bot.message_handler(regexp='Lagarto')
def elije(message):

	computer = randrange(1, 6)
	tiradaComputer(message.text,computer, message.from_user.id,message.from_user.first_name)

@bot.message_handler(regexp='Spock')
def elije(message):
	computer = randrange(1, 6)
	tiradaComputer(message.text,computer, message.from_user.id,message.from_user.first_name)


#\RESPUESTA A LA PRIMERA PREGUNTA "QUIERES JUGAR"
@bot.message_handler(func=lambda message:True)
def empiezaPartida(message):
	print message.text
	if str(message.text) == str("Si"):
		print  message.from_user.first_name
		bot.send_message(message.chat.id, "Empieza el juego \nPiedra, Papel, Tijera, Lagarto, Spock...",reply_markup=json_keyboard1)


	elif str(message.text) == "No":
		bot.send_message(message.chat.id, "otra vez sera")


#Para que no finalize el programa i se mantenga a la espera de mas informacion
bot.polling()
