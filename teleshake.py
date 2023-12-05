import serial
import math
import os

addy = '/dev/tty.usbserial-110'  # mac/linux
comport = 'COM4'    #windows -- change this to fit


ser = serial.Serial(port=addy, baudrate=9600, bytesize=8, parity='N', stopbits=1)

def telewite(cmd_ser):
    while ser is open:
