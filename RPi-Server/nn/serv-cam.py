import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT)
GPIO.setwarnings(False)

ajoutAngle = 5

print("\n+------------------/ ServoMoteur  Controlleur /------------------+")
print("|                                                |")
print("| Le Servo doit etre branche au pins physique 4 / 6 / 8 =  GPIO 17 |")
print("|                                                |")
print("+----------------------------------------------------------------+\n")

print("Comment controler le Servo ?")
choix = input("1. Choisir un angle\n2. Faire tourner de 0 a 180\n")

if choix == 2 :

    nbrTour = input ("Entrez le nombre d'aller-retour que fera le Servo :\n")

    pwm=GPIO.PWM(14,10)
    pwm.start(-20)

    #angle1 = 0
    #duty1 = float(angle1)/10 + ajoutAngle

    #angle2=180
    #duty2= float(angle2)/10 + ajoutAngle

    i = 0

    while i <= nbrTour:
         pwm.ChangeDutyCycle(20)
         time.sleep(0.8)
         pwm.ChangeDutyCycle(20)
         time.sleep(0.8)
         i = i+1
    GPIO.cleanup()

if choix == 1 :
    angle = input("Entrez l'angle souhaite :\n")
    duree = input("Entrez la duree durant laquelle le Servo devra tenir sa position : ( en secondes )\n")

    pwm=GPIO.PWM(14,50)
    pwm.start(20)

    angleChoisi = float(angle)/10 + ajoutAngle
    pwm.ChangeDutyCycle(6)
    time.sleep(duree)
    GPIO.cleanup()
