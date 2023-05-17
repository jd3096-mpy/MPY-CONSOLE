import network
import time
def wifi_connect():
    start_time=time.time()
    sta_if = network.WLAN(network.STA_IF)
    print('network status1:', sta_if.status())
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect('dundundun', '30963096')
        print('network status2:', sta_if.status())
        while not sta_if.isconnected():
            time.sleep_ms(200)
            if time.time()-start_time > 11:
                break
    print('network status3:', sta_if.status())
    if sta_if.isconnected():
        return True
    else:
        return False
    
wifi_connect()