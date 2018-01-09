#!/usr/bin/python
# -*- coding:Utf-8 -*-

from flask import Flask, render_template, request
import RPi.GPIO as GPIO
import time
import threading
from forward_threading import Forward
from retreat_threading import Retreat
from right_threading import Right
from left_threading import Left
from capteurAr import Arriere
from capteurAv import Avant

#--Wheel one [pin 26 = GPIO 7 | pin 24 = GPIO 8| pin 22 = GPIO 25]
#--Wheel two [pin 19 = GPIO 10 | pin 21 = GPIO 9 | pin 23 = GPIO 11]
#--Wheel three [pin 11 = GPIO 17 | pin 13 = GPIO 27 | pin 15 = GPIO 22]
#--Wheel one [pin 12 = GPIO 18 | pin 16 = GPIO 23 | pin 18 = GPIO 24]

class Server():

	puiss = 20

	""" Déclaration de :
	#--pin qui commande les 4 mouteurs du robot.--#
	#--L'application Flask.--#
	#--Module PWM qui gère le impulsion envoyé sur les GPIO.--#
	"""
	def __init__(self):
		#--Initialisation--#
		GPIO.setwarnings(False)
		GPIO.setmode(GPIO.BCM)
		#--Déclaration--#
		self.var_pwma = [10,17,18,25]
		self.var_av = [8,9,24,27]
		self.var_ar = [7,11,22,23]
		self.var_g = [9,24]
		self.var_d = [8,27]
		self.start_forward = False
		self.start_retreat = False
		self.start_right = False
		self.start_left = False
		self.th_forward = Forward(Server.puiss)
		self.th_retreat = Retreat(Server.puiss)
		self.th_right = Right(Server.puiss)
		self.th_left = Left(Server.puiss)
		self.th_sonsor_ar = Avant()
		self.th_sonsor_av = Arriere()
		self.if_init_foraward = True
		self.if_init_retreat = True
		self.if_init_right = True
		self.if_init_left = True


	#--Configuration des GPIO en sorites numériques--Activation de la lecture bcm--#
	#--Initialisation--#
	def run(self):
		for pin in self.var_pwma:
			GPIO.setup(pin, GPIO.OUT)
		for pin in self.var_av:
			GPIO.setup(pin, GPIO.OUT)
		for pin in self.var_ar:
			GPIO.setup(pin, GPIO.OUT)

	#------------------------------------------------------------------------------------------------------#
	#--Definition des fonction de commande--#

	def stop_it(self):
		for pin in self.var_pwma:
			GPIO.setup(pin, GPIO.OUT)
		for pin in self.var_pwma:
			GPIO.output(pin, GPIO.LOW)

##--Fin de la définition de la classe Server()--##

#--Declaration du serveur Flask & Instantiation de la classe Server()--#

app = Flask(__name__)
server = Server()
server.run()

#------------------------------------------------------------------------------------------------------#
#--Lancement des thread pour les capteur sonor--#

server.th_sonsor_ar = Arriere()
server.th_sonsor_av = Avant()
server.th_sonsor_ar.start()
server.th_sonsor_av.start()

@app.route("/")
def main():	
	return render_template('home.html')

#--Définition des routes pour l'association des action(commande ou fonction) a chaque boutton.--#
@app.route("/stop")
def stop():
	bol_forward = server.th_forward.result()
	bol_retreat = server.th_retreat.result()
	if bol_forward:
		print("stop")
		server.th_forward.stop()
		server.if_init_foraward = False
		server.stop_it()
		return ('', 204)
	elif bol_retreat:
		print("stop")
		server.th_retreat.stop()
		server.if_init_retreat = False
		server.stop_it()
		return ('', 204)
	else:
		print("stop")
		server.stop_it()
		return ('', 204)

@app.route("/start")
def start():
	if server.if_init_foraward:
		resultat = server.th_sonsor_ar.result()
		if resultat <=20:
			print ("Y a un obstacle")
			print ("Distance", resultat, "cm")
			server.stop_it()
			return ('', 204)
		elif server.th_retreat.result():
			print("start")
			server.th_retreat.stop()
			server.if_init_retreat = False
			server.th_forward.start()
			server.start_forward = True
			return ('', 204)
		elif server.th_right:
			print("start")
			server.th_right.stop()
			server.if_init_right = False
			server.th_forward.start()
			server.start_forward = True
			return ('', 204)
		elif server.th_left:
			print("start")
			server.th_left.stop()
			server.if_init_left = False
			server.th_forward.start()
			server.start_forward = True
			return ('', 204)
		else:
			print("start")
			server.th_forward.start()
			server.start_forward = True
			return ('', 204)
	else:
		server.th_forward = Forward(server.puiss)
		resultat = server.th_sonsor_ar.result()
		if resultat <=20:
			print ("Y a un obstacle")
			print ("Distance", resultat, "cm")
			server.stop_it()
			return ('', 204)
		elif server.th_retreat.result():
			print("start")
			server.th_retreat.stop()
			server.if_init_retreat = False
			server.th_forward.start()
			server.start_forward = True
			return ('', 204)
		elif server.th_right:
			print("start")
			server.th_right.stop()
			server.if_init_right = False
			server.th_forward.start()
			server.start_forward = True
			return ('', 204)
		elif server.th_left:
			print("start")
			server.th_left.stop()
			server.if_init_left = False
			server.th_forward.start()
			server.start_forward = True
			return ('', 204)
		else:
			print("start")
			server.th_forward.start()
			server.start_forward = True
			return ('', 204)


@app.route("/retreat")
def retreat():
	if server.if_init_retreat:
		resultat = server.th_sonsor_av.result()
		if resultat <=20:
			print ("Y a un obstacle")
			print ("Distance", resultat, "cm")
			server.stop_it()
			return ('', 204)
		elif server.th_forward.result():
			print("retreat")
			server.th_forward.stop()
			server.if_init_foraward = False
			server.th_retreat.start()
			server.start_retreat = True
			return ('', 204)
		elif server.th_right:
			print("retreat")
			server.th_right.stop()
			server.if_init_right = False
			server.th_forward.start()
			server.start_forward = True
			return ('', 204)
		elif server.th_left:
			print("retreat")
			server.th_left.stop()
			server.if_init_left = False
			server.th_forward.start()
			server.start_forward = True
			return ('', 204)
		else:
			print("retreat")
			server.th_retreat.start()
			server.start_retreat = True
			return ('', 204)
	else :
		resultat = server.th_sonsor_av.result()
		server.th_retreat = Retreat(server.puiss)
		if resultat <=20:
			print ("Y a un obstacle")
			print ("Distance", resultat, "cm")
			server.stop_it()
			return ('', 204)
		elif server.th_forward.result():
			print("retreat")
			server.th_forward.stop()
			server.if_init_foraward = False
			server.th_retreat.start()
			server.start_retreat = True
			return ('', 204)
		elif server.th_right:
			print("retreat")
			server.th_right.stop()
			server.if_init_right = False
			server.th_forward.start()
			server.start_forward = True
			return ('', 204)
		elif server.th_left:
			print("retreat")
			server.th_left.stop()
			server.if_init_left = False
			server.th_forward.start()
			server.start_forward = True
			return ('', 204)
		else:
			print("retreat")
			server.th_retreat.start()
			server.start_retreat = True
			return ('', 204)

@app.route("/right")
def right():
	if server.if_init_right:
		if server.th_forward.result():
			print("right")
			server.th_forward.stop()
			server.if_init_foraward = False
			server.th_right.start()
			server.start_right = True
			return ('', 204)
		elif server.th_retreat:
			print("right")
			server.th_retreat.stop()
			server.if_init_retreat = False
			server.th_right.start()
			server.start_right = True
			return ('', 204)
		elif server.th_left:
			print("right")
			server.th_left.stop()
			server.if_init_left = False
			server.th_right.start()
			server.start_right = True
			return ('', 204)
		else:
			print("right")
			server.th_right.start()
			server.start_right = True
			return ('', 204)
	else :
		server.th_right = Right(server.puiss)
		if server.th_forward.result():
			print("right")
			server.th_forward.stop()
			server.if_init_foraward = False
			server.th_right.start()
			server.start_right = True
			return ('', 204)
		elif server.th_retreat:
			print("right")
			server.th_retreat.stop()
			server.if_init_retreat = False
			server.th_right.start()
			server.start_right = True
			return ('', 204)
		elif server.th_left:
			print("start")
			server.th_left.stop()
			server.if_init_left = False
			server.th_right.start()
			server.start_right = True
			return ('', 204)
		else:
			print("retreat")
			server.th_right.start()
			server.start_right = True
			return ('', 204)

@app.route("/left")
def left():
	if server.if_init_left:
		if server.th_forward.result():
			print("left")
			server.th_forward.stop()
			server.if_init_foraward = False
			server.th_left.start()
			server.start_left = True
			return ('', 204)
		elif server.th_retreat:
			print("left")
			server.th_retrart.stop()
			server.if_init_retreat = False
			server.th_left.start()
			server.start_left = True
			return ('', 204)
		elif server.th_right:
			print("left")
			server.th_right.stop()
			server.if_init_right = False
			server.th_left.start()
			server.start_left = True
			return ('', 204)
		else:
			print("left")
			server.th_left.start()
			server.start_left = True
			return ('', 204)
	else :
		server.th_left = Left(server.puiss)
		if server.th_forward.result():
			print("left")
			server.th_forward.stop()
			server.if_init_foraward = False
			server.th_left.start()
			server.start_left = True
			return ('', 204)
		elif server.th_retreat:
			print("left")
			server.th_retreat.stop()
			server.if_init_retreat = False
			server.th_left.start()
			server.start_left = True
			return ('', 204)
		elif server.th_right:
			print("left")
			server.th_right.stop()
			server.if_init_right = False
			server.th_left.start()
			server.start_left = True
			return ('', 204)
		else:
			print("left")
			server.th_left.start()
			server.start_left = True
			return ('', 204)

@app.route("/accelerer")
def accelerer():
	if server.puiss < 100:
		server.puiss = server.puiss + 20
		if server.start_forward:
			print("acceleration")
			server.th_forward.stop()
			server.th_forward = Forward(server.puiss)
			server.th_forward.start()
			return ('', 204)
		elif server.start_retreat:
			print("acceleration")
			server.th_retreat.stop()
			server.th_retreat = Retreat(server.puiss)
			server.th_retreat.start()
			return ('', 204)
		else:
			print("Attention ! Verage Dangereux")
			return ('', 204)
	else :
		print("Puissance Max")
		return ('', 204)

@app.route("/decelerer")
def decelerer():
	if server.puiss > 20:
		server.puiss = server.puiss - 20
		if server.th_forward.result():
			print("deceleration")
			server.th_forward.stop()
			server.th_forward = Forward(server.puiss)
			server.th_forward.start()
			return ('', 204)
		elif server.th_retreat.result():
			print("deceleration")
			server.th_retreat.stop()
			server.th_retreat = Retreat(server.puiss)
			server.th_retreat.start()
			return ('', 204)
		else:
			print("Attention ! Verage Dangereux")
			return ('', 204)
	else :
		print("Puissance Min")
		return ('', 204)

if __name__ == "__main__":
	app.run(host='192.168.0.12', port=5000)
