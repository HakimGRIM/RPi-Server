#!/usr/bin/python
# -*- coding:Utf-8 -*-

from threading import Thread
import time
import RPi.GPIO as GPIO

class Retreat(Thread):

    def __init__(self, puiss, v_pwma):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        ''' Constructor. '''
        Thread.__init__(self)
        self._puiss = puiss
        self._start = True
        self._puiss = puiss
        self.var_pwma = v_pwma
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
        pwm_1.start(self._puiss)
        pwm_2 = GPIO.PWM(17, 50)
        pwm_2.start(self._puiss)
        pwm_3 = GPIO.PWM(18, 50)
        pwm_3.start(self._puiss)
        pwm_4 = GPIO.PWM(25, 50)
        pwm_4.start(self._puiss)
        try:
            while self._start:
                pwm_1.ChangeDutyCycle(self._puiss)
                pwm_2.ChangeDutyCycle(self._puiss)
                pwm_3.ChangeDutyCycle(self._puiss)
                pwm_4.ChangeDutyCycle(self._puiss)
        except KeyboardInterrupt:
            pass 
    def stop(self):
        self._start = False
    
    def result(self):
        return self._start