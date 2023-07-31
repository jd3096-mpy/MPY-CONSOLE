import network
import espnow
import _thread
import time
import st7789
from utils.drivers import SCREEN
import utils.dos_font as font
import utils.color as color
import utils.settings as setting
from utils.drivers import KEYBOARD
from machine import Timer
import os

set_dic=setting.load_setting()
NAME=set_dic['OWNER']

theme=color.COLOR_CANDY
kb=KEYBOARD()

sta = network.WLAN(network.STA_IF) 
sta.active(True)

e = espnow.ESPNow()
e.active(True)
peer = b'\xff\xff\xff\xff\xff\xff'  # MAC address of peer's wifi interface
try:
    e.add_peer(peer)
except:
    pass

screen = SCREEN(320,240).tft

class RecvBox:
    def __init__(self):
        self.display = screen
        self.mess_box=[]
        self.border=2
        
    def message(self,message):
        if len(self.mess_box)>5:
            del self.mess_box[0]
        self.mess_box.append(message)
        i=0
        for mess in self.mess_box:
            self.show_mess(i,mess)
            i+=1
    
    def show_mess(self,num,mess):
        title=mess.split('|')[0]
        mess=mess.split('|')[1]
        self.display.fill_rect(0, 35*num,320,35,theme['bg'])
        # DRAW BOARDER
        self.display.rect(0, 35*num,320,35,theme['border'])
        # DRAW TITLE
        self.display.write(font,title,self.border+2,self.border+1+35*num,theme['warn'],theme['bg2'])
        # DRAW TEXT
        self.display.write(font,mess,self.border+2,self.border+15+35*num,theme['font'],theme['bg'])

    
recv=RecvBox()

class SendBox:
    def __init__(self):
        self.display = screen
        self.mess_box=[]
        self.border=2
           
    def input_box(self):
        title=NAME
        # DRAW BOARDER
        self.display.rect(0, 212,320,25,theme['bg2'])
        text=''
        t=0
        while 1:
            time.sleep_ms(5)
            re=kb.check_key()
            if re==b'\x08':
                text=text[:-1]
                self.display.fill_rect(1, 213,318,23,theme['bg'])
            if re==b'\r\n':
                if text!='':
                    break
            if re!=None and re!=b'\x08':
                text+=re.decode()
            self.display.write(font,text,self.border+2,215,theme['font'],theme['bg'])
        self.display.fill_rect(0, 212,320,25,theme['bg'])
        text=NAME+'|'+text
        recv.message(text)
        e.send(peer,text,False)

        
            
send=SendBox()



            
def recv_cb(e):
    while True:  # Read out all messages waiting in the buffer
        mac, msg = e.irecv(0)  # Don't wait if no messages left
        if mac is None:
            return
        recv.message(msg.decode())
        
e.irq(recv_cb)


while 1:
    send.input_box()










