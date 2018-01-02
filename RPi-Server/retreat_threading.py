#!/usr/bin/python
# -*- coding:Utf-8 -*-

from threading import Thread
import time
import RPi.GPIO as GPIO
import subprocess
class Retreat(Thread):

    def __init__(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        ''' Constructor. '''
        Thread.__init__(self)
        self._start = True
        self.var_pwma = [10,17,18,25]
        self.var_av = [8,9,24,27]
        self.var_ar = [7,11,22,23]
        self.var_g = [9,24]
        self.var_d = [8,27]
        for pin in self.var_pwma:
            GPIO.setup(pin, GPIO.OUT)
        for pin in self.var_av:
            GPIO.setup(pin, GPIO.OUT)
        for pin in self.var_ar:
            GPIO.setup(pin, GPIO.OUT)
    
    def run(self):
        for pin in self.var_pwma:
            GPIO.output(pin, GPIO.HIGH)
        for pin in self.var_ar:
            GPIO.output(pin, GPIO.HIGH)
        for pin in self.var_av:
            GPIO.output(pin, GPIO.LOW)

        #--Création des PWM pour chaque mouteur, ainsi que la fixation du rapport cyclique de demarage à 20%--#
        
        pwm_1 = GPIO.PWM(10, 50)
        pwm_1.start(20)
        pwm_2 = GPIO.PWM(17, 50)
        pwm_2.start(20)
        pwm_3 = GPIO.PWM(18, 50)
        pwm_3.start(20)
        pwm_4 = GPIO.PWM(25, 50)
        pwm_4.start(20)
        try:
            while self._start:
                pwm_1.ChangeDutyCycle(20)
                pwm_2.ChangeDutyCycle(20)
                pwm_3.ChangeDutyCycle(20)
                pwm_4.ChangeDutyCycle(20)
        except KeyboardInterrupt:
            pass 
	#subprocess.call("start python capteurAr.py")
    def stop(self):
        self._start = False     
