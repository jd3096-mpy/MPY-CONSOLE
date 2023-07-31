import network,time
import utils.settings as setting

sta_if = network.WLAN(network.STA_IF)
connected=False
set_dic=setting.load_setting()
SSID=set_dic['SSID']
PWD=set_dic['PWD']

if sta_if.isconnected():
    connected=True
if connected:
    print('WIFI connected.')
    ip=sta_if.ifconfig()[0]
    netmask=sta_if.ifconfig()[1]
    DNS=sta_if.ifconfig()[3]
    print('IP:'+ip)
    print('Netmask:'+ip)
    print('DNS:'+ip)
else:
    print('WIFI disconnected.')
while 1:
    print('-'*20)
    print('CONNECT/SETTING/QUIT')
    print('Input the option:(c/s/q)')
    cmd=input()
    if cmd=='c':
        set_dic=setting.load_setting()
        SSID=set_dic['SSID']
        PWD=set_dic['PWD']
        start_time=time.time()
        if not sta_if.isconnected():
            print('Connecting to network...')
            sta_if.active(True)
            sta_if.connect(SSID, PWD)
            print('network status:', sta_if.status())
            while not sta_if.isconnected():
                time.sleep_ms(200)
                if time.time()-start_time > 15:
                    print('WIFI Timeout!')
                    break
        if sta_if.isconnected():
            print("WIFI CONNECTED")
        else:
            print("WIFI CONNECTED FAILED")
    elif cmd=='s':
        print('Input SSID:')
        ssid=input()
        print('Input PASSWORD:')
        pwd=input()
        set_dic['SSID']=ssid
        set_dic['PWD']=pwd
        setting.save_setting(set_dic)
    elif cmd=='q':
        break
    else:
        print('Wrong commands input,try again.')

