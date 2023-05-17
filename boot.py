import random
import utime
import st7789
import tft_config
import framebuf
from machine import Pin
import sys
from machine import SoftI2C,Pin,UART
import time
import _thread
import machine


class SCREEN():
    def __init__(self, width, height):
        self.tft=tft_config.config(0)
        self.width = width
        self.height = height
        self.tft.init()
        self.tft.fill(0)


screen=SCREEN(320,240)

# screen.tft.jpg('logo.jpg',0,0)
# time.sleep(2)
# screen.fb.text('oh houw',10, 10,222)
# screen.show()


from fbconsole import FBConsole
import os
scr = FBConsole(screen,bgcolor=st7789.color565(10, 27, 15),fgcolor=st7789.color565(66, 234, 71))
os.dupterm(scr)        # redirect REPL output to OLED
print('MPY CONSOLE by jd3096')
