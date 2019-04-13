##

from machine import Pin, SPI
from time import sleep
import struct

#spi = SPI(baudrate=9600, polarity=1, phase=0, sck=Pin(19), mosi=Pin(23), miso=Pin(21))

CS_pin = Pin(5, Pin.OUT) # create output pin 27 for CS
spi = SPI(-1, baudrate=9600, polarity=0, phase=0, bits=8, sck=Pin(18), mosi=Pin(19), miso=Pin(22))
#spi.init(baudrate=9600) # set the baudrate

def dig_pot(value):
    CS_pin.off()
    spi.write(bytes([int('00010011',2)]))
    spi.write(bytes([value]))
    print(value)
    CS_pin.on()

for i in range(0,255):
    dig_pot(i)
    sleep(0.2)
