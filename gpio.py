from gpiozero import LED
import RPi.GPIO as GPIO
GPIO.cleanup()# import GPIO
GPIO.setmode(GPIO.BCM)
arret_urgence=23
start=22
GPIO.setup(17,GPIO.IN)
GPIO.setup(arret_urgence,GPIO.IN)
GPIO.setup(start,GPIO.IN)

import time
while True:
    #GPIO.output(17,GPIO.HIGH)
    #GPIO.output(17,GPIO.LOW)
    
    time.sleep(2)
    print("ok")
    print(GPIO.input(start))
    print(GPIO.input(17))
    print(GPIO.input(arret_urgence))