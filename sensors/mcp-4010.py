##

from machine import Pin, SPI
from time import sleep

CS_pin = Pin(5, Pin.OUT) # create output pin for CS

# Software SPI used.
# MISO pin is not used for the MCP-4010 dig pot, so just set it to whatever.
spi = SPI(-1, baudrate=9600, polarity=0, phase=0, bits=8, sck=Pin(18), mosi=Pin(19), miso=Pin(22)) # Software SPI used.

# The first byte is the command byte, for writing to the digital pot. The second is a 0-255 byte, setting the wiper position.
# CS needs to be in low when sending.

def dig_pot(value):
    CS_pin.off()
    spi.write(bytes([int('00010011',2)]))
    spi.write(bytes([value]))
    print(value)
    CS_pin.on()

for i in range(0,255):
    dig_pot(i)
    sleep(0.2)
