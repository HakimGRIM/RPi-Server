#!/usr/bin/python
# -*- coding:Utf-8 -*-

import RPi.GPIO as GPIO
import time
from threading import Thread

class Arriere(Thread):

    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        Thread.__init__(self)
        self.TRIG = 30
        self.ECHO = 31
        GPIO.setup(self.TRIG, GPIO.OUT)
        GPIO.setup(self.ECHO, GPIO.IN)
    
    def run(self):
        GPIO.output(self.TRIG, False)
        print ("Distance Measurement In Progress")
        
        print ("Waiting For Sensor To Settle")
        time.sleep(2)
        GPIO.output(self.TRIG, True)
        time.sleep(0.00001)
        GPIO.output(self.TRIG, False)
        while GPIO.input(self.ECHO) == 0:
            pulse_start = time.time()
        while GPIO.input(self.ECHO) == 1:
            pulse_end = time.time()
        pulse_duration = pulse_end - pulse_start
        distance = pulse_duration * 17150
        distance = round(distance, 2)
        print "Distance: ", distance, " cm"
        GPIO.cleanup()