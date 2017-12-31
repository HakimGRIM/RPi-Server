#!/usr/bin/python
# -*- coding:Utf-8 -*-

from flask import Flask, render_template, request
import RPi.GPIO as GPIO
import time
import threading
from forward_threading import Forward

#--Wheel one [pin 26 = GPIO 7 | pin 24 = GPIO 8| pin 22 = GPIO 25]
#--Wheel two [pin 19 = GPIO 10 | pin 21 = GPIO 9 | pin 23 = GPIO 11]
#--Wheel three [pin 11 = GPIO 17 | pin 13 = GPIO 27 | pin 15 = GPIO 22]
#--Wheel one [pin 12 = GPIO 18 | pin 16 = GPIO 23 | pin 18 = GPIO 24]

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

""" Déclaration de :
  #--pin qui commande les 4 mouteurs du robot.--#
  #--L'application Flask.--#
  #--Module PWM qui gère le impulsion envoyé sur les GPIO.--#
"""
app = Flask(__name__)

var_pwma = [10,17,18,25]
var_av = [8,9,24,27]
var_ar = [7,11,22,23]
var_g = [9,24]
var_d = [8,27]


#--Configuration des GPIO en sorites numériques--Activation de la lecture bcm--#
#--Initialisation--#

for pin in var_pwma:
	GPIO.setup(pin, GPIO.OUT)
for pin in var_av:
	GPIO.setup(pin, GPIO.OUT)
for pin in var_ar:
	GPIO.setup(pin, GPIO.OUT)

#------------------------------------------------------------------------------------------------------#
#--Definition des fonction de commande--#

def stop_it():
	print "Stop Rebot"
	for pin in var_pwma:
		GPIO.output(pin, GPIO.LOW)

def forward():
	print "Forward"
	for pin in var_pwma:
		GPIO.output(pin, GPIO.HIGH)
	for pin in var_av:
		GPIO.output(pin, GPIO.HIGH)
	for pin in var_ar:
		GPIO.output(pin, GPIO.LOW)
	"""#--Création des PWM pour chaque mouteur, ainsi que la fixation du rapport cyclique de demarage à 20%--#
	pwm_1 = GPIO.PWM(10, 50)
	pwm_1.start(20)
	pwm_2 = GPIO.PWM(17, 50)
	pwm_2.start(20)
	pwm_3 = GPIO.PWM(18, 50)
	pwm_3.start(20)
	pwm_4 = GPIO.PWM(25, 50)
	pwm_4.start(20)
	try:
		while _start:
			pwm_1.ChangeDutyCycle(20)
			pwm_2.ChangeDutyCycle(20)
			pwm_3.ChangeDutyCycle(20)
			pwm_4.ChangeDutyCycle(20)
	except KeyboardInterrupt:
		pass"""

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

#th_1 = threading.Thread(None, forward, None, (200,), {'nom':'thread th_1'})

@app.route("/")
def main():
 
   # Pass the template data into the template main.html and return it to the user
   return render_template('home.html')

#--Définition des routes pour l'association des action(commande ou fonction) a chaque boutton.--#
@app.route("/stop")
def stop():
	#_satrt = False
	#th_1._Thread_stop()
	print("stop")
	th_forward.stop()
	stop_it()
	return ('', 204)

@app.route("/start")
def start():
	print("start")
	#th_1.start()
	#thread.start_new_thread(forward, ())
	global th_forward
	th_forward = Forward()
	th_forward.start()
	return ('', 204)

@app.route("/retreat")
def retreat():
	print("retreat")
	retreat_it()
	return ('', 204)

@app.route("/right")
def right():
	print("right")
	go_right()
	return ('', 204)

@app.route("/left")
def left():
	print("left")
	go_left()
	return ('', 204)

if __name__ == "__main__":
	app.run(host='192.168.0.12', port=5000)
