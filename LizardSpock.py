# -*- coding:utf-8 -*-
import telebot
import json
from random import randrange, uniform
from multiprocessing import Process, Value, Array
import threading
import os
import sys
reload(sys)
sys.setdefaultencoding('utf8')
# randrange gives you an integral value

#TOKEN BOT
bot = telebot.TeleBot("571633707:AAHooMJqG3oG740HqTkCTcjj30_zKyFZCS4")

playerId = Value('i', 0)

#TECLADOS PERSONALIZADOS
json_keyboard = json.dumps({'keyboard': [["Si"],["No"]],#PREGUNTA LISTO PARA EMPEZAR
							'one_time_keyboard':True,
							'resize_keyboard':True})

json_keyboard1 = json.dumps({'keyboard': [["Piedra"],["Papel"],["Tijera"],["Lagarto"],["Spock"]],#PREGUNTA TU ELECCCION
							'one_time_keyboard':True,
							'resize_keyboard':True})

json_keyboard2 = json.dumps({'keyboard': [["Puntuacion"],["Total partidas"],["Partidas ganadas"],["Partidas empatadas"],["Partidas perdidas"],["Salir"]],#PREGUNTA TU ELECCCION
							'one_time_keyboard':True,
							'resize_keyboard':True})

#METODO REVISA SI EXISTE EL FICHERO
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
		bot.send_message(playerId,"Empate, " + movPc)
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


	#GUARDA EN EL documentoPj

	if checkFile(str(playerId) + ".txt") == True:
		print "existe"

		documentoPl = open(str(playerId) + ".txt", "r+")
		lectura = documentoPl.readline().split(";")
		#TOTAL PUNTOS JUGADOR
		total = int(lectura[5])+1#TOTAL PARTIDAS JUGADAS
		g = int(lectura[2])#TOTAL PARTIDAS GANADAS
		e = int(lectura[3])#TOTAL PARTIDAS EMPATADAS
		p = int(lectura[4])#TOTAL PARTIDAS PERDIDAS
		#CHIVATO
		print lectura[1]
		print float(puntos)

		if float(puntos) == 1.0:
			g = g + 1
		elif float(puntos) == 0.5:
			e = e + 1
		elif float(puntos) == -1.0:
			p = p + 1

		documentoPj = open(str(playerId) + ".txt", "w+")#ABRE DOCUMENTO ESCRITURA
		puntos = puntos + float(lectura[1])
		#ESCRIBE EN EL DOCUMENTO YA EXISTENTE

		documentoPj.write(playerName + ";" + str(puntos) + ";" + str(g) + ";" + str(e) + ";" + str(p) + ";"+ str(total))
		documentoPj.close()
	else:
		print "NO existe"
		documentoPj = open(str(playerId) + ".txt", "w+")
		#ESCRIBE EN EL DOCUMENTO SI NO EXISTE
		if puntos == 1:
			documentoPj.write(playerName + ";" + str(puntos) + ";1;0;0;1")
		elif puntos == -1:
			documentoPj.write(playerName + ";" + str(puntos) + ";0;0;1;1")
		elif puntos == 0.5:
			documentoPj.write(playerName + ";" + str(puntos) + ";0;1;0;1")
		documentoPj.close()
#FIN DEL PROCESO


#MUESTRA PUNTUACION-------
def verPuntuacion(plyer,playerId,playerName,posicio):
	if checkFile(str(playerId) + ".txt") == True:
		print "existe"

		documentoPl = open(str(playerId) + ".txt", "r+")
		lectura = documentoPl.readline().split(";")
		Puntuacion = str(lectura[posicio])
		return Puntuacion
		#bot.send_message(playerId, "TINES UN TOTAL DE " + str(Puntuacion))




#----------START BOT------------

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.send_message(message.chat.id, "Bienvenido, Estas listo? ",reply_markup=json_keyboard)
	playerId.value = message.from_user.id
#\nEmpieza el juego Piedra, Papel, Tijera, Lagarto, Spock...""
@bot.message_handler(commands=['help'])
def send_welcome(message):
	bot.send_message(message.chat.id, "Hola Bienvenido veo que necesitas ayuda \nEste es el juego Piedra, Papel, Tijera, Lagarto, Spock\n  \n/start <-- para empezar \n Si quieres jugar elige SI, sino elige NO y puedes ver tus puntuaciones o salir y jugar otro dia")

#\nEmpieza el juego Piedra, Papel, Tijera, Lagarto, Spock...""

#\CUANDO ELIGES UN MOVIMIENTO  LLAMA AL METODO tiradaComputer LE PASA EL message(TU ELECCION), computer(RANDOM TIRADA PC), message(ID USUARIO JUGANDO)
@bot.message_handler(regexp='Piedra')
def elije(message):
	computer = randrange(1, 6)
	tiradaComputer(message.text, computer, message.from_user.id, message.from_user.first_name)

@bot.message_handler(regexp='Papel')
def elije(message):
	computer = randrange(1, 6)
	tiradaComputer(message.text, computer, message.from_user.id, message.from_user.first_name)

@bot.message_handler(regexp='Tijera')
def elije(message):
	computer = randrange(1, 6)
	tiradaComputer(message.text, computer, message.from_user.id, message.from_user.first_name)

@bot.message_handler(regexp='Lagarto')
def elije(message):
	computer = randrange(1, 6)
	tiradaComputer(message.text, computer, message.from_user.id, message.from_user.first_name)

@bot.message_handler(regexp='Spock')
def elije(message):
	computer = randrange(1, 6)
	tiradaComputer(message.text, computer, message.from_user.id, message.from_user.first_name)

#\CUANDO ELIJES (NO EMPEZAR) PUEDES VISUALIZAR

@bot.message_handler(regexp='Puntuacion')
def elije(message):
	bot.send_message(message.chat.id, "TINES UN TOTAL DE " + verPuntuacion(message.text, message.from_user.id, message.from_user.first_name,1) + " PUNTOS")

@bot.message_handler(regexp='Total partidas')
def elije(message):
	bot.send_message(message.chat.id, "TINES UN TOTAL DE " + verPuntuacion(message.text, message.from_user.id, message.from_user.first_name,5) + " PARTIDAS JUGADAS")

@bot.message_handler(regexp='Partidas ganadas')
def elije(message):
	bot.send_message(message.chat.id, "TINES UN TOTAL DE " + verPuntuacion(message.text, message.from_user.id, message.from_user.first_name,2) + " PARTIDAS GANADAS")

@bot.message_handler(regexp='Partidas empatadas')
def elije(message):
	bot.send_message(message.chat.id, "TINES UN TOTAL DE " + verPuntuacion(message.text, message.from_user.id, message.from_user.first_name,3) + " PARTIDAS EMPATADAS")

@bot.message_handler(regexp='Partidas perdidas')
def elije(message):
	bot.send_message(message.chat.id, "TINES UN TOTAL DE " + verPuntuacion(message.text, message.from_user.id, message.from_user.first_name,4) + " PARTIDAS PERDIDAS")

@bot.message_handler(regexp='Salir')
def elije(message):
	bot.send_message(message.chat.id, "Vuelve cuando quieras  \n")


#\RESPUESTA A LA PRIMERA PREGUNTA "QUIERES JUGAR? si/no"
@bot.message_handler(func=lambda message:True)
def empiezaPartida(message):

	if str(message.text) == str("Si"):
		bot.send_message(message.chat.id, "Empieza el juego \nPiedra, Papel, Tijera, Lagarto, Spock...",reply_markup=json_keyboard1)


	elif str(message.text) == "No":
		bot.send_message(message.chat.id, "Que necesitas? \n",reply_markup=json_keyboard2)


#Para que no finalize el programa i se mantenga a la espera de mas informacion
bot.polling()
