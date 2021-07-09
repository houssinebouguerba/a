import board
import neopixel
from time import sleep
pixels=neopixel.NeoPixel(board.D18,20)
for x in range (0,9):
    sleep(2)
    sleep(2)
    pixels[x]=(255,0,255)
    sleep(2)
    pixels[x]=(0,255,100)

