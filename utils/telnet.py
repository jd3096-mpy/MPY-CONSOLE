import network
import time
def wifi_connect():
    start_time=time.time()
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect('dundundun', '30963096')
        while not sta_if.isconnected():
            time.sleep_ms(200)
            if time.time()-start_time > 11:
                break
    print('network status3:', sta_if.status())
    if sta_if.isconnected():
        port=23
        print("Telnet server started on {}:{}".format(sta_if.ifconfig()[0], port))
        print("Dupterm has been redirect to telnet...")
        return True
    else:
        return False
    
wifi_connect()


import utelnetserver
utelnetserver.start()
