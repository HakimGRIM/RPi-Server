#!/usr/bin/python
# -*- coding:Utf-8 -*-

from threading import Thread
import time
import RPi.GPIO as GPIO

class Stop_it(Thread):
    def __init__(self, puiss):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        ''' Constructor. '''
        Thread.__init__(self)
        self.var_pwma = [10,17,18,25]
        self.var_av = [8,9,24,27]
        self.var_ar = [7,11,22,23]
        self.var_g = [9,24]
        self.var_d = [8,27]
    
    def run(self):
	    for pin in var_pwma:
		    GPIO.output(pin, GPIO.LOW)