import RPi.GPIO as GPIO 
import time
 
GPIO.setmode(GPIO.BCM) 
GPIO.setup(25, GPIO.OUT)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(8, GPIO.OUT)
GPIO.OUTPUT(7, LOW)
GPIO.OUTPUT(7, HIGH)
 
# creation d'un objet PWM. canal=4 frequence=50Hz
pwm = GPIO.PWM(25, 50)
 
# demarrage du PWM avec un cycle a 0 (LED off)
pwm.start(0)
 
# On fait varier le rapport cyclique de 0 a 100 puis de 100 a 0
try:
    while 1:
        for dc in range(0, 101, 1):
            pwm.ChangeDutyCycle(dc)
            time.sleep(0.01)
        for dc in range(100, -1, -1):
            pwm.ChangeDutyCycle(dc)
            time.sleep(0.01)
except KeyboardInterrupt:
    pass
pwm.stop()
GPIO.cleanup()