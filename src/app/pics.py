import st7789
from machine import SoftI2C,Pin,UART,Timer,SPI
import time

tft=st7789.ST7789(
        SPI(2, baudrate=20000000, sck=Pin(41), mosi=Pin(38)),
        240,
        320,
        cs=Pin(39, Pin.OUT),
        dc=Pin(40, Pin.OUT),
        backlight=Pin(36, Pin.OUT),
        reset=Pin(42, Pin.OUT),
        rotation=3,
        color_order=st7789.RGB,
        inversion=False)

tft.init()      
tft.jpg('logo.jpg',0,0)