import random
import utime
import st7789
import tft_config
import vga2_bold_16x32 as font

tft = tft_config.config(0)

def center(text):
    tft.text(
        font,
        text,
        100,
        100,
        st7789.WHITE,
        st7789.RED)

def main():
    print(0)
    tft.init()
    tft.fill(st7789.RED)
    print(1)
    center(b'\xAEHello\xAF')
    


main()