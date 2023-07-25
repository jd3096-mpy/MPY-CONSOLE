import st7789
import tft_config
import framebuf
from machine import SoftI2C,Pin,UART,Timer
import time

power=Pin(10,Pin.OUT)
power.on()

bt=Pin(0)

class SCREEN():
    def __init__(self, width, height):
        self.tft=tft_config.config(0)
        self.width = width
        self.height = height
        self.tft.init()
        self.tft.fill(0)
screen=SCREEN(320,240)

kb=SoftI2C(scl=Pin(8),sda=Pin(18))
KB_ADDR=0x55


from fbconsole import FBConsole
import os
scr = FBConsole(screen,bgcolor=0,fgcolor=st7789.color565(66, 234, 71))
os.dupterm(scr)   
print('MPY CONSOLE by jd3096')
time.sleep(0.5)

def check_key(t):
    re=kb.readfrom(KB_ADDR, 1)
    if re!=b'\x00':
        scr._c=re
        scr._press()
    
tim=Timer(0)
tim.init(mode=Timer.PERIODIC, period=10, callback=check_key)



