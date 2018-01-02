#!/usr/bin/python
# -*- coding:Utf-8 -*-

from flask import Flask, render_template, request
import RPi.GPIO as GPIO
import time
import threading
from forward_threading import Forward
from capteurAr import Arriere

#--Wheel one [pin 26 = GPIO 7 | pin 24 = GPIO 8| pin 22 = GPIO 25]
#--Wheel two [pin 19 = GPIO 10 | pin 21 = GPIO 9 | pin 23 = GPIO 11]
#--Wheel three [pin 11 = GPIO 17 | pin 13 = GPIO 27 | pin 15 = GPIO 22]
#--Wheel one [pin 12 = GPIO 18 | pin 16 = GPIO 23 | pin 18 = GPIO 24]

class Server():

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
		self.app = Flask(__name__)
		self.var_pwma = [10,17,18,25]
		self.var_av = [8,9,24,27]
		self.var_ar = [7,11,22,23]
		self.var_g = [9,24]
		self.var_d = [8,27]


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
		#--Lancement des thread pour les capteur sonor--#
		th_sonsor_ar = Arriere()
		th_sonsor_ar.start()

	#------------------------------------------------------------------------------------------------------#
	#--Definition des fonction de commande--#

	def stop_it():
		GPIO.setmode(GPIO.BCM)
		for pin in var_pwma:
			GPIO.setup(pin, GPIO.OUT)
		for pin in var_pwma:
			GPIO.output(pin, GPIO.LOW)

	def retreat_it():
		print "Reverse"
		for pin in var_pwma:
			GPIO.output(pin, GPIO.HIGH)
		for pin in var_ar:
			GPIO.output(pin, GPIO.HIGH)
		for pin in var_av:
			GPIO.output(pin, GPIO.LOW)

	def go_left():
		print "Turn left 2 et 4"
		for pin in var_pwma:
			GPIO.output(pin, GPIO.HIGH)
		for pin in var_g:
			GPIO.output(pin, GPIO.LOW)
		for pin in var_d:
			GPIO.output(pin, GPIO.HIGH)

	def go_right():
		print "Trun right 1 et 3"
		for pin in var_pwma:
			GPIO.output(pin, GPIO.HIGH)
		for pin in var_d:
			GPIO.output(pin, GPIO.LOW)
		for pin in var_g:
			GPIO.output(pin, GPIO.HIGH)

	#----#
	#resultat = th_sonsor_ar.result()
	#if resultat <= 20:
	#	stop_it()
	#----#

	@app.route("/")
	def main():
	
	return render_template('home.html')

	#--Définition des routes pour l'association des action(commande ou fonction) a chaque boutton.--#
	@app.route("/stop")
	def stop():
		print("stop")
		th_forward.stop()
		stop_it()
		return ('', 204)

	@app.route("/start")
	def start():
		resultat = th_sonsor_ar.result()
		if resultat <=20:
			print ("Y a un obstacle")
			stop_it()
		else:
			print("start")
			global th_forward
			th_forward = Forward()
			th_forward.start()
			return ('', 204)

	@app.route("/retreat")
	def retreat():
		print("retreat")
		#th_forward.stop()
		retreat_it()
		return ('', 204)

	@app.route("/right")
	def right():
		print("right")
		#th_forward.stop()
		go_right()
		return ('', 204)

	@app.route("/left")
	def left():
		print("left")
		#th_forward.stop()
		go_left()
		return ('', 204)

	if __name__ == "__main__":
		app.run(host='192.168.0.12', port=5000)
