"""M5Stack CORE2 ili9342 320x240 display"""

from machine import Pin, SPI, freq
import st7789

TFA = 0
BFA = 0


def config(rotation=0, buffer_size=0, options=0):
    return st7789.ST7789(
        SPI(2, baudrate=24000000, sck=Pin(41), mosi=Pin(37)),
        240,
        320,
        cs=Pin(39, Pin.OUT),
        dc=Pin(40, Pin.OUT),
        backlight=Pin(36, Pin.OUT),
        rotation=1,
        color_order=st7789.RGB,
        inversion=False,
        options=options,
        buffer_size=buffer_size)