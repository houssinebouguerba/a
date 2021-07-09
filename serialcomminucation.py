"""from time import sleep
import serial
ser = serial.Serial('/dev/ttyACM0', 9600) # Establish the connection on a specific port
counter = 32 # Below 32 everything in ASCII is gibberish
while True:
     counter +=1
     ser.write(str(chr(counter))) # Convert the decimal number to ASCII then send it to the Arduino
     print (ser.readline()) # Read the newest output from the Arduino
     sleep(.1) # Delay for one tenth of a second
     if counter == 255:
         counter = 32


"""
"""
## Open a serial connection with Arduino.

import serial
ser = serial.Serial('/dev/ttyACM0', 9600)  # open serial port that Arduino is using
print (ser)                           # print serial config

ser.write(bytes(100))

# Reminder to close the connection when finished
if(ser.isOpen()):
   print ("Serial connection is still open.")

"""
import tkinter
from tkinter import *
import serial
from time import sleep

# Enter your COM port in the below line
ard = serial.Serial('/dev/ttyACM0', 9600)  # open serial port that Arduino is using
sleep(2)
print (ard.readline(ard.inWaiting()))

top = tkinter.Tk()
a='999.2'
b='898.3'
def TrunOn():
  ard.write(a.encode("utf-8"))
  sleep(0.1)
  data = ard.readline(ard.inWaiting())
  label1.config(text=str(data))
  print (ard.readline(ard.inWaiting()))
  
def Turnoff():
  ard.write(b.encode("utf-8"))
  sleep(0.1)
  data = ard.readline(ard.inWaiting())
  label1.config(text=str(data))
  print (ard.readline(ard.inWaiting()))

OnButton = tkinter.Button(top, text ="LED ON", command = TrunOn)
OffButton = tkinter.Button(top, text ="LED OFF", command = Turnoff)
label1 = Label(top, fg="green")

label1.pack()
OnButton.pack()
OffButton.pack()
top.mainloop()
