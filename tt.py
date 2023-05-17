from machine import SoftI2C,Pin
import time

kb=SoftI2C(scl=Pin(8),sda=Pin(18))
KB_ADDR=0x55

print(kb.scan())

while 1:
    re=kb.readfrom(KB_ADDR, 1)
    print(re)
    time.sleep_ms(100)