#!/usr/bin/python
# -*- coding:Utf-8 -*-

import RPi.GPIO as GPIO
import time

#--Wheel one [pin 26 = GPIO 7 | pin 24 = GPIO 8| pin 22 = GPIO 25]
#--Wheel two [pin 19 = GPIO 10 | pin 21 = GPIO 9 | pin 23 = GPIO 11]
#--Wheel three [pin 11 = GPIO 17 | pin 13 = GPIO 27 | pin 15 = GPIO 22]
#--Wheel one [pin 12 = GPIO 18 | pin 16 = GPIO 23 | pin 18 = GPIO 24]

#--Déclaration des pin qui commande les 4 mouteurs du robot

var_pwma = [10,17,18,25]
var_av = [8,9,24,27]
var_ar = [7,11,22,23]
var_g = [9,24]
var_d = [8,27]

#--Configuration des GPIO en sorites numériques--Activation de la lecture bcm--#
#--Initialisation--#
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

for pin in var_pwma:
	GPIO.setup(pin, GPIO.OUT)
for pin in var_av:
	GPIO.setup(pin, GPIO.OUT)
for pin in var_ar:
	GPIO.setup(pin, GPIO.OUT)

#------------------------------------------------------------------------------------------------------#
#--Definition des fonction de commande--#

def forward():
	print "Forward"
	for pin in var_pwma:
	        GPIO.output(pin, GPIO.HIGH)
	for pin in var_av:
		GPIO.output(pin, GPIO.HIGH)
	for pin in var_ar:
		GPIO.output(pin, GPIO.LOW)

def retreat():
	print "Reverse"
	for pin in var_pwma:
                GPIO.output(pin, GPIO.HIGH)
        for pin in var_ar:
                GPIO.output(pin, GPIO.HIGH)
        for pin in var_av:
                GPIO.output(pin, GPIO.LOW)

def left():
	print "Turn left 2 et 4"
	for pin in var_pwma:
                GPIO.output(pin, GPIO.HIGH)
	for pin in var_g:
		GPIO.output(pin, GPIO.LOW)

def right():
	print "Trun right 1 et 3"
	for pin in var_pwma:
                GPIO.output(pin, GPIO.HIGH)
	for pin in var_d:
		GPIO.output(pin, GPIO.LOW)

while 1:
#	forward()
#	time.sleep(5)
#	left()
#	time.sleep(5)
#	retreat()
#	time.sleep(5)
	right()
	time.sleep(5)
#	forwars()
