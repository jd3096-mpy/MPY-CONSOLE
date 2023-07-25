"""
hello.py

    Writes "Hello!" in random colors at random locations on the display.
"""

import random
import utime
import st7789
import tft_config
import vga1_bold_16x32 as font
from machine import Pin, SPI, freq

tft = st7789.ST7789(
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

def center(text):
    length = 1 if isinstance(text, int) else len(text)
    tft.text(
        font,
        text,
        tft.width() // 2 - length // 2 * font.WIDTH,
        tft.height() // 2 - font.HEIGHT //2,
        st7789.WHITE,
        st7789.RED)

def main():
    tft.init()
    tft.fill(st7789.RED)
    center(b'\xAEHello\xAF')
    utime.sleep(2)
    tft.fill(st7789.BLACK)

    while True:
        for rotation in range(4):
            tft.rotation(rotation)
            tft.fill(0)
            col_max = tft.width() - font.WIDTH*6
            row_max = tft.height() - font.HEIGHT

            for _ in range(128):
                tft.text(
                    font,
                    b'Hello!',
                    random.randint(0, col_max),
                    random.randint(0, row_max),
                    st7789.color565(
                        random.getrandbits(8),
                        random.getrandbits(8),
                        random.getrandbits(8)),
                    st7789.color565(
                        random.getrandbits(8),
                        random.getrandbits(8),
                        random.getrandbits(8)))


main()