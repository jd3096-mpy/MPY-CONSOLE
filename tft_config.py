"""M5Stack CORE2 ili9342 320x240 display"""

from machine import Pin, SPI, freq
import st7789

TFA = 0
BFA = 0


def config(rotation=0, buffer_size=0, options=0):
    return st7789.ST7789(
        SPI(1, baudrate=24000000, sck=Pin(40), mosi=Pin(41)),
        240,
        320,
        cs=Pin(12, Pin.OUT),
        dc=Pin(11, Pin.OUT),
        backlight=Pin(42, Pin.OUT),
        rotation=1,
        color_order=st7789.RGB,
        inversion=False,
        options=options,
        buffer_size=buffer_size)