#!/usr/bin/env python3
import RPi.GPIO as GPIO  # import GPIO
from hx711 import HX711  # import the class HX711
while True:
    try:
        GPIO.setmode(GPIO.BCM)  # set GPIO pin mode to BCM numbering
        hx = HX711(dout_pin=21, pd_sck_pin=20)
        ratio = -32700 / 150  # calculate the ratio for channel A and gain 128
        hx.set_scale_ratio(ratio)
        # set ratio for current channel
        
        print(hx.get_weight_mean(1)+507, 3,'g')

    except :
        print('Bye :)')


