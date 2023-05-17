from machine import Pin
import time

class TRACKBALL:
    def __init__(self,pin_up,pin_down,pin_left,pin_right,pin_button):
        self.pin=Pin(pin_button,Pin.IN,Pin.PULL_UP)
        self.button_up=Pin(pin_up,Pin.IN,Pin.PULL_UP)
        self.button_down=Pin(pin_down,Pin.IN,Pin.PULL_UP)
        self.button_left=Pin(pin_left,Pin.IN,Pin.PULL_UP)
        self.button_right=Pin(pin_right,Pin.IN,Pin.PULL_UP)
        self.x=0
        self.y=0
        self.old_u=0
        self.old_d=0
        self.old_l=0
        self.old_r=0
        
    def clear(self):
        self.x=0
        self.y=0
        self.old_u=0
        self.old_d=0
        self.old_l=0
        self.old_r=0
    
    def pressed(self, flag = 0):
        last_state = self.pin.value()
        if flag:
            if not last_state:
                return False
            else:
                while self.pin.value():
                    time.sleep_ms(10)
                return True
        else:
            if last_state:
                return False
            else:
                while not self.pin.value():
                    time.sleep_ms(10)
                return True
    
    def roll_check(self,interval=10):
        u=self.button_up.value()
        d=self.button_down.value()
        l=self.button_left.value()
        r=self.button_right.value()
        if l!=self.old_l:
            self.x-=1
            self.old_l=l
        if r!=self.old_r:
            self.x+=1
            self.old_r=r
        if u!=self.old_u:
            self.y+=1
            self.old_u=u
        if d!=self.old_d:
            self.y-=1
            self.old_d=d
        time.sleep_ms(interval)
        return self.x,self.y
    
if __name__ == '__main__':
    tb=TRACKBALL(3,15,1,2,0)
    while 1:
        print(tb.roll_check(10))
    


        
    

