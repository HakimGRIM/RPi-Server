#!/usr/bin/python
# -*- coding:Utf-8 -*-

import RPi.GPIO as GPIO
import time
from threading import Thread

class Avant(Thread):

    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        Thread.__init__(self)
        self.running = True
        self.TRIG = 28
        self.ECHO = 29
        self.distance = 0
    
    def run(self):
        try:
            while 1:
                GPIO.setmode(GPIO.BCM)
                GPIO.setup(self.TRIG, GPIO.OUT)
                GPIO.setup(self.ECHO, GPIO.IN)
                GPIO.output(self.TRIG, False)
                time.sleep(2)
                GPIO.output(self.TRIG, True)
                time.sleep(0.00001)
                GPIO.output(self.TRIG, False)
                while GPIO.input(self.ECHO) == 0:
                    pulse_start = time.time()
                while GPIO.input(self.ECHO) == 1:
                    pulse_end = time.time()
                pulse_duration = pulse_end - pulse_start
                self.distance = pulse_duration * 17150
                self.distance = round(self.distance, 2)
                #print "Distance: ", self.distance, " cm"
            
        except KeyboardInterrupt:
            pass
            GPIO.cleanup()

    def result(self):
        return self.distance

    def stop(self):
        self.running = False