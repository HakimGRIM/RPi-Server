import RPi.GPIO as GPIO 
import time

GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BCM)

GPIO.setup(25, GPIO.OUT)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(8, GPIO.OUT)

GPIO.output(25, GPIO.HIGH)
GPIO.output(7, GPIO.LOW)
GPIO.output(8, GPIO.HIGH)
 
# creation d'un objet PWM. canal=4 frequence=50Hz
pwm = GPIO.PWM(25, 50)
 
# demarrage du PWM avec un cycle a 0 (LED off)
pwm.start(5)
while 1:
    pwm.ChangeDutyCycle(5)

"""
# On fait varier le rapport cyclique de 0 a 100 puis de 100 a 0
try:
    while 1:
        for dc in range(0, 101):
            pwm.ChangeDutyCycle(dc)
            time.sleep(0.01)
        #for dc in range(100, -1):
         #   pwm.ChangeDutyCycle(dc)
          #  time.sleep(0.01)
except KeyboardInterrupt:
    pass

pwm.stop()
GPIO.cleanup()
"""