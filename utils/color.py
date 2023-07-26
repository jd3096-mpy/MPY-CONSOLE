import st7789
from utils.drivers import SCREEN
import utils.dos_font as font

COLOR_CANDY={
    'bg':st7789.color565(0, 0, 0),  #BLACK
    'font':st7789.color565(242, 242, 242),  #WHITE
    'warn':st7789.color565(229, 34, 34),  #RED
    'border':st7789.color565(166, 227, 45), #GREEN
    'bg2':st7789.color565(196, 141, 255), #BLUE

}
COLOR_EVA={
    'bg':st7789.color565(56, 36, 87),  
    'font':st7789.color565(78, 244, 72),  
    'warn':st7789.color565(101, 34, 54),  
    'border':st7789.color565(251, 164, 5), 
    'bg2':st7789.color565(113, 78, 158), 
}

#diaglo test
# scr=SCREEN(320,240).tft
# theme=COLOR_EVA
# scr.init()
# scr.rect(30, 30, 200, 100, theme['border'])
# scr.fill_rect(32, 32, 196, 96, theme['bg'])
# scr.fill_rect(32, 50, 196, 3, theme['border'])
# scr.write(font,'TITLE',80,33,theme['font'],theme['bg'])

