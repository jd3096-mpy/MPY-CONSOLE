import framebuf
import uio
import dos_font as font
import st7789
import os

class FBConsole(uio.IOBase):
    def __init__(self, fb, bgcolor=0, fgcolor=-1, width=-1, height=-1, readobj=None):
        self.readobj = readobj
        self.fb = fb
        if width > 0:
            self.width=width
        else:
            try:
                self.width=fb.width
            except:
                raise ValueError
        if height > 0:
            self.height=height
        else:
            try:
                self.height=fb.height
            except:
                raise ValueError
        self.bgcolor = bgcolor
        self.fgcolor = fgcolor
        self.char_x=8
        self.char_y=16
        self.line_height(16)
        self.voffset = 0
        self.bottom_mark=False
        self._n = 0
        self._c = b'x'
        self.cls()
    
    def _press(self):
        self._n += 1
        os.dupterm_notify(None)
        
    

    def readinto(self, buf):
        n = min(len(buf), self._n)
        for i in range(n):
            buf[i:i+1] = self._c
        self._n -= n
        return None if n == 0 else n

    def cls(self):
        self.x = 0
        self.y = 0
        self.y_end = 0
        self.fb.tft.fill(self.bgcolor)
        self.bottom_mark=False
        self.voffset = 0

    def line_height(self, px):
        self.lineheight = px
        self.w =  self.width // self.char_x
        self.h =  self.height // self.char_y

    def _putc(self, c):
        c = chr(c)
        if c == '\n':
            self._newline()
        elif c == '\x08':
            self._backspace()
        elif c >= ' ':
            #self.fb.tft.fill_rect(self.x * self.char_x, self.y * self.lineheight, self.char_y, self.lineheight, st7789.RED)
            if self.bottom_mark:
                if self.voffset==0:
                    self.fb.tft.write(font, c, self.x * self.char_x, self.height-self.lineheight, self.fgcolor,self.bgcolor)
                else:
                    self.fb.tft.write(font, c, self.x * self.char_x, self.voffset-self.lineheight, self.fgcolor,self.bgcolor)
            else:
                self.fb.tft.write(font, c, self.x * self.char_x, self.y * self.lineheight, self.fgcolor,self.bgcolor)
            self.x += 1
            if self.x >= self.w:
                self._newline()

    def _esq_read_num(self, buf, pos):
        digit = 1
        n = 0
        while buf[pos] != 0x5b:
            n += digit * (buf[pos] - 0x30)
            pos -= 1
            digit *= 10
        return n

    def write(self, buf):
        self._draw_cursor(self.bgcolor)
        i = 0
        while i < len(buf):
            c = buf[i]
            if c == 0x1b:
                i += 1
                esc = i
                while chr(buf[i]) in '[;0123456789':
                    i += 1
                c = buf[i]
                if c == 0x4b and i == esc + 1:   # ESC [ K
                    self._clear_cursor_eol()
                elif c == 0x44:   # ESC [ n D
                    for _ in range(self._esq_read_num(buf, i - 1)):
                        self._backspace()
            else:
                self._putc(c)
            i += 1
        self._draw_cursor(self.fgcolor)
        return len(buf)
        
    def _newline(self):
        #self.fb.tft.vscrdef(0,self.height,self.lineheight)
        self.fb.tft.vscrdef(0,0,0)
        self.x = 0
        self.y += 1
        if self.y >= self.h:
            self.bottom_mark=True
        if self.bottom_mark:
            self.cls()
#             self.voffset += 16
#             self.voffset %= self.height
#             self.fb.tft.vscsad(self.voffset)
#             self.fb.tft.fill_rect(0, self.voffset - self.lineheight, self.width, self.lineheight, self.bgcolor)
#             #self.y = self.h - 1
#             self.y = self.voffset - 16
        self.y_end = self.y

    def _backspace(self):
        if self.x == 0:
            if self.y > 0:
                self.y -= 1
                self.x = self.w - 1
        else:
            self.x -= 1
            self.fb.tft.fill_rect(self.x*self.char_x,self.y*self.char_y,self.char_x, self.char_y, self.bgcolor)

    def _clear_cursor_eol(self):
        self.fb.tft.fill_rect(self.x * self.char_x, self.y * self.lineheight, self.width, self.lineheight, self.bgcolor)
        for l in range(self.y + 1, self.y_end + 1):
            self.fb.tft.fill_rect(0, l * self.lineheight, self.width, self.lineheight, self.bgcolor)
        self.y_end = self.y
        
    def _draw_cursor(self, color):
        if self.bottom_mark:
            self.fb.tft.hline(self.x * self.char_x, self.voffset-1, self.char_x, color)
        else:
            self.fb.tft.hline(self.x * self.char_x, self.y * self.lineheight + self.char_y-1, self.char_x, color)
