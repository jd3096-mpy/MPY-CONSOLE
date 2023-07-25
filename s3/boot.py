import st7789
import tft_config
import framebuf
from machine import SoftI2C,Pin,UART,Timer,SPI
import time
from BC6561 import KEYBOARD


bt=Pin(0)

class SCREEN():
    def __init__(self, width, height):
        self.tft=st7789.ST7789(
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
        self.width = width
        self.height = height
        self.tft.init()
        self.tft.fill(0)
screen=SCREEN(320,240)
kb=KEYBOARD()



from fbconsole import FBConsole
import os
scr = FBConsole(screen,bgcolor=0,fgcolor=st7789.color565(66, 234, 71))
os.dupterm(scr)   
print('MPY CONSOLE by jd3096')
time.sleep(0.5)

def check_key(t):
    re=kb.check_key()
    if re!=None:
        if len(re)==1:
            scr._c=re
            scr._press()
        else:
            for b in re:
                scr._c=b.to_bytes(1,'big')
                scr._press()
    
tim=Timer(0)
tim.init(mode=Timer.PERIODIC, period=10, callback=check_key)





