#system setting
import json

def load_setting():
    setting={'OWNER':'jd3096','SSID':'dundundun','PWD':'30963096'}
    set_str=json.dumps(setting)
    try:
        with open('./utils/setting.dat', 'r') as f:
            setting=f.read()
    except:
        print('No setting file!')
        with open('./utils/setting.dat', 'w') as f:
            f.write(set_str)
    print(setting)
    set_dic=json.loads(setting)
    return set_dic

def save_setting(set_dic):
    set_str=json.dumps(set_dic)
    with open('./utils/setting.dat', 'w') as f:
            f.write(set_str)
    print('saved!')
