#ST7789
from machine import Pin, SPI, freq
import st7789

class SCREEN():
    def __init__(self, width, height):
        self.tft=st7789.ST7789(
        SPI(2, baudrate=20000000, sck=Pin(41), mosi=Pin(38)),
        height,
        width,
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

#BC6561 KEYBOARD
from machine import UART,Pin
import time

key_map={
0:b'q',1:b'w',7:b'e',14:b'r',16:b't',23:b'y',21:b'u',30:b'i',28:b'o',10:b'p',
3:b'a',8:b's',9:b'd',20:b'f',15:b'g',22:b'h',27:b'j',34:b'k',29:b'l',31:b'\x08',
4:None,12:b'z',11:b'x',19:b'c',18:b'v',25:b'b',26:b'n',33:b'm',32:b'tab',24:b'\r\n',
13:b'import',6:b'0',5:b' ',2:b'sym',17:None,
    }

key_map_sym={
0:b'#',1:b'1',7:b'2',14:b'3',16:b'(',23:b')',21:b'-',30:b'_',28:b'+',10:b'@',
3:b'*',8:b'4',9:b'5',20:b'6',15:b'/',22:b':',27:b';',34:b"'",29:b'"',31:b'\x08',
4:None,12:b'7',11:b'8',19:b'9',18:b'?',25:b'!',26:b',',33:b'.',32:b'$',24:b'\n',
13:b'import',6:b'0',5:b' ',2:b'sym',17:None,
    }

class KEYBOARD():
    def __init__(self):
        self.uart=UART(1,9600,rx=15,tx=3)
        self.alt=False
        self.bl=Pin(16,Pin.OUT)
        self.bl_state=False

    def check_key(self):
        rx_data=self.uart.read()
        if rx_data!=None:
            key_num=rx_data[0]
            if key_num==4:
                self.alt=True
            elif key_num==132:
                self.alt=False
            elif key_num==17:
                self.bl_state=not self.bl_state
                if self.bl_state:
                    self.bl.on()
                else:
                    self.bl.off()
            if key_num>127:
                return None
            if self.alt:
                return key_map_sym[key_num]
            else:
                return key_map[key_num]
            

            
    



