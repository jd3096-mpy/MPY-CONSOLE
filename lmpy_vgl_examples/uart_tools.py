import machine
import ili9XXX
import lvgl as lv
from machine import Pin,UART,PWM
import time
import gc
import device

lv.init()

uart = UART(2,9600,tx=1,rx=2)   
bl=PWM(Pin(36), freq=5000, duty_u16=65535)

dispp = lv.disp_get_default()
theme = lv.theme_default_init(dispp, lv.palette_main(lv.PALETTE.BLUE), lv.palette_main(lv.PALETTE.RED), True, lv.font_default())
dispp.set_theme(theme)
#----------------------------SCREEN_SETTINGS--------------------------------------
def Button2_eventhandler(event_struct):
    event = event_struct.code
    if event == lv.EVENT.CLICKED and True:
        lv.scr_load_anim(ui_Screen2, lv.SCR_LOAD_ANIM.FADE_ON, 300, 0,False)
        screen_group(2)
    return

def slider_event_cb(evt):
    slider = evt.get_target()
    bl.duty_u16(int(slider.get_value())*6550)

def event_dropdown(e):
    code = e.get_code()
    obj = e.get_target()
    if code == lv.EVENT.VALUE_CHANGED:
        option1 = [9600,57600,14400,115200]
        option2 = [8,7,9]
        option3 = [1,2]
        o1=option1[ui_DDbaudrate.get_selected()]
        o2=option2[ui_DDdatabits.get_selected()]
        o3=option3[ui_DDstopbits.get_selected()]
        print(o1,o2,o3)
#         uart.deinit()
#         uart = UART(2, 9600) 
        uart.init(o1, bits=o2, parity=None, stop=o3)



ui_Screen1 = lv.obj()

ui_DDbaudrate = lv.dropdown(ui_Screen1)
ui_DDbaudrate.set_options("9600\n57600\n14400\n115200")
ui_DDbaudrate.set_width(96)
ui_DDbaudrate.set_height(lv.SIZE_CONTENT)   # 1
ui_DDbaudrate.set_x(61)
ui_DDbaudrate.set_y(-50)
ui_DDbaudrate.set_align(lv.ALIGN.CENTER)
ui_DDbaudrate.add_event_cb(event_dropdown, lv.EVENT.ALL, None)

ui_DDdatabits = lv.dropdown(ui_Screen1)
ui_DDdatabits.set_options("8\n7\n9")
ui_DDdatabits.set_width(96)
ui_DDdatabits.set_height(lv.SIZE_CONTENT)   # 1
ui_DDdatabits.set_x(60)
ui_DDdatabits.set_y(-4)
ui_DDdatabits.set_align( lv.ALIGN.CENTER)
ui_DDdatabits.add_event_cb(event_dropdown, lv.EVENT.ALL, None)

ui_DDstopbits = lv.dropdown(ui_Screen1)
ui_DDstopbits.set_options("1\n2")
ui_DDstopbits.set_width(96)
ui_DDstopbits.set_height(lv.SIZE_CONTENT)   # 1
ui_DDstopbits.set_x(61)
ui_DDstopbits.set_y(42)
ui_DDstopbits.set_align( lv.ALIGN.CENTER)
ui_DDstopbits.add_event_cb(event_dropdown, lv.EVENT.ALL, None)

ui_DATABITS = lv.label(ui_Screen1)
ui_DATABITS.set_text("DATABITS")
ui_DATABITS.set_width(lv.SIZE_CONTENT)	# 1
ui_DATABITS.set_height(lv.SIZE_CONTENT)   # 1
ui_DATABITS.set_x(-66)
ui_DATABITS.set_y(-1)
ui_DATABITS.set_align( lv.ALIGN.CENTER)

ui_Label2 = lv.label(ui_Screen1)
ui_Label2.set_text("BAUDRATE")
ui_Label2.set_width(lv.SIZE_CONTENT)	# 1
ui_Label2.set_height(lv.SIZE_CONTENT)   # 1
ui_Label2.set_x(-70)
ui_Label2.set_y(-47)
ui_Label2.set_align( lv.ALIGN.CENTER)
ui_Label2.set_flex_flow(lv.FLEX_FLOW.ROW)
ui_Label2.set_flex_align(lv.FLEX_ALIGN.START, lv.FLEX_ALIGN.START, lv.FLEX_ALIGN.START)

ui_Label3 = lv.label(ui_Screen1)
ui_Label3.set_text("STOPBITS")
ui_Label3.set_width(lv.SIZE_CONTENT)	# 1
ui_Label3.set_height(lv.SIZE_CONTENT)   # 1
ui_Label3.set_x(-63)
ui_Label3.set_y(40)
ui_Label3.set_align( lv.ALIGN.CENTER)

ui_BTback = lv.btn(ui_Screen1)
ui_BTback.set_width(71)
ui_BTback.set_height(37)
ui_BTback.set_x(-2)
ui_BTback.set_y(87)
ui_BTback.set_align( lv.ALIGN.CENTER)
ui_BTback.add_event_cb(Button2_eventhandler, lv.EVENT.ALL, None)

ui_Label4 = lv.label(ui_BTback)
ui_Label4.set_text("BACK")
ui_Label4.set_width(lv.SIZE_CONTENT)	# 1
ui_Label4.set_height(lv.SIZE_CONTENT)   # 1
ui_Label4.set_align( lv.ALIGN.CENTER)

ui_Label1 = lv.label(ui_Screen1)
ui_Label1.set_text("BACKLIGHT")
ui_Label1.set_width(lv.SIZE_CONTENT)	# 1
ui_Label1.set_height(lv.SIZE_CONTENT)   # 1
ui_Label1.set_x(-92)
ui_Label1.set_y(-87)
ui_Label1.set_align( lv.ALIGN.CENTER)
ui_Label1.set_flex_flow(lv.FLEX_FLOW.ROW)
ui_Label1.set_flex_align(lv.FLEX_ALIGN.START, lv.FLEX_ALIGN.START, lv.FLEX_ALIGN.START)

ui_Slider1 = lv.slider(ui_Screen1)
ui_Slider1.set_width(150)
ui_Slider1.set_height(10)
ui_Slider1.set_x(55)
ui_Slider1.set_y(-87)
ui_Slider1.set_align( lv.ALIGN.CENTER)
ui_Slider1.add_event_cb(slider_event_cb, lv.EVENT.VALUE_CHANGED, None) # Assign an event function
ui_Slider1.set_range(0,10)
ui_Slider1.set_value(10, lv.ANIM.OFF)


#----------------------------SCREEN_MAIN--------------------------------------
def Button1_eventhandler(event_struct):
    event = event_struct.code
    if event == lv.EVENT.CLICKED:
        lv.scr_load_anim(ui_Screen1, lv.SCR_LOAD_ANIM.FADE_ON, 300, 0,False)
        screen_group(1)
    return

def uart_send(event_struct):
    event = event_struct.code
    if event == lv.EVENT.CLICKED:
        data=ui_TextArea1.get_text()
        print(data," send!")
        uart.write(data.encode())
    return

ui_Screen2 = lv.obj()

ui_TextArea1 = lv.textarea(ui_Screen2)
ui_TextArea1.set_width(200)
ui_TextArea1.set_height(36)
ui_TextArea1.set_x(20)
ui_TextArea1.set_y(138)
ui_TextArea1.set_align( lv.ALIGN.CENTER)
ui_TextArea1.set_one_line(True)

ui_TextArea2 = lv.textarea(ui_Screen2)
ui_TextArea2.set_placeholder_text("UART data received")
ui_TextArea2.set_width(280)
ui_TextArea2.set_height(110)
ui_TextArea2.set_x(20)
ui_TextArea2.set_y(15)
ui_TextArea2.set_align( lv.ALIGN.CENTER)
ui_TextArea2.add_state(lv.STATE.DISABLED)

ui_BTsend = lv.btn(ui_Screen2)
ui_BTsend.set_width(71)
ui_BTsend.set_height(37)
ui_BTsend.set_x(107)
ui_BTsend.set_y(35)
ui_BTsend.set_align( lv.ALIGN.CENTER)
ui_BTsend.add_event_cb(uart_send, lv.EVENT.ALL, None)


ui_Label6 = lv.label(ui_BTsend)
ui_Label6.set_text("SEND")
ui_Label6.set_width(lv.SIZE_CONTENT)	# 1
ui_Label6.set_height(lv.SIZE_CONTENT)   # 1
ui_Label6.set_align( lv.ALIGN.CENTER)

ui_BTsetting = lv.btn(ui_Screen2)
ui_BTsetting.set_width(100)
ui_BTsetting.set_height(37)
ui_BTsetting.set_x(75)
ui_BTsetting.set_y(85)
ui_BTsetting.set_align( lv.ALIGN.CENTER)
ui_BTsetting.add_event_cb(Button1_eventhandler, lv.EVENT.ALL, None)

ui_Label5 = lv.label(ui_BTsetting)
ui_Label5.set_text("SETTINGS")
ui_Label5.set_width(lv.SIZE_CONTENT)
ui_Label5.set_height(lv.SIZE_CONTENT)
ui_Label5.set_align( lv.ALIGN.CENTER)

ui_Switch1 = lv.switch(ui_Screen2)
ui_Switch1.set_width(109)
ui_Switch1.set_height(25)
ui_Switch1.set_x(-60)
ui_Switch1.set_y(85)
ui_Switch1.set_align( lv.ALIGN.CENTER)
ui_Switch1.add_state(lv.STATE.CHECKED)

ui_Label8 = lv.label(ui_Switch1)
ui_Label8.set_text("FRESH")
ui_Label8.set_width(lv.SIZE_CONTENT)
ui_Label8.set_height(lv.SIZE_CONTENT)  
ui_Label8.set_align( lv.ALIGN.CENTER)


#------------------------------MAIN-----------------------------------------------------

def screen_group(scr):
    if scr==1:
        device.group.remove_all_objs()
        device.group.add_obj(ui_Slider1)
        device.group.add_obj(ui_DDbaudrate)
        device.group.add_obj(ui_DDdatabits)
        device.group.add_obj(ui_DDstopbits)
        device.group.add_obj(ui_BTback)
    elif scr==2:
        device.group.remove_all_objs()
        device.group.add_obj(ui_TextArea1)
        device.group.add_obj(ui_BTsend)
        device.group.add_obj(ui_Switch1)
        device.group.add_obj(ui_BTsetting )

lv.scr_load(ui_Screen2)
screen_group(2)

while 1:
    if ui_Switch1.has_state(lv.STATE.CHECKED):
        if uart.any():
            data=uart.read()
            ui_TextArea2.add_text(data)
