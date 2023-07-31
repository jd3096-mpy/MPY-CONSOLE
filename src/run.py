#run py files in repl

import os,gc
from machine import Timer,Pin
from utils.drivers import SCREEN
from utils.fbconsole import FBConsole
import utils.color as color
from utils.drivers import KEYBOARD

ok=Pin(8,Pin.IN,Pin.PULL_UP)
kb=KEYBOARD()
screen=SCREEN(320,240)

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
    

os.dupterm(None)
theme=color.COLOR_CANDY

scr = FBConsole(screen,bg_color=theme['bg'],fg_color=theme['bg2'])
os.dupterm(scr)
tim=Timer(0)
tim.init(mode=Timer.PERIODIC, period=3, callback=check_key)

print('Enter the filename you want to run:')
file=input()+'.py'
err=0
tim.deinit()
try:
    exec(open('./app/'+file).read())
except OSError as e:
    err=1
except Exception as e:
    err=2


if err==1:
    os.dupterm(None)
    scr = FBConsole(screen,bg_color=theme['bg'],fg_color=theme['font'])
    os.dupterm(scr)
    tim=Timer(0)
    tim.init(mode=Timer.PERIODIC, period=3, callback=check_key)
    print(file+' not found!')
elif err==2:
    os.dupterm(None)
    scr = FBConsole(screen,bg_color=theme['bg'],fg_color=theme['font'])
    os.dupterm(scr)
    tim=Timer(0)
    tim.init(mode=Timer.PERIODIC, period=3, callback=check_key)
    print('An error occurred in py file.')
elif err==0:
    print('Press OK button to continue.')
    while ok.value():
        pass
    os.dupterm(None)
    scr = FBConsole(screen,bg_color=theme['bg'],fg_color=theme['font'])
    os.dupterm(scr)
    tim=Timer(0)
    tim.init(mode=Timer.PERIODIC, period=3, callback=check_key)
    print(file+' execution completed.')
    
gc.collect()
    