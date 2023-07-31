from machine import Pin
ok=Pin(8,Pin.IN,Pin.PULL_UP)
if ok.value():
    import start

