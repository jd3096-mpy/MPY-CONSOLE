import st7789
from utils.drivers import SCREEN
import utils.dos_font as font

COLOR_EVA={
    'bg':st7789.color565(56, 36, 87),  
    'font':st7789.color565(78, 244, 72),  
    'warn':st7789.color565(101, 34, 54),  
    'border':st7789.color565(251, 164, 5), 
    'bg2':st7789.color565(113, 78, 158), 
}

theme=COLOR_EVA

class DialogBox:
    def __init__(self, x,y,width, height):
        self.display = SCREEN(320,240).tft
        self.x=x
        self.y=y
        self.width = width
        self.height = height
        self.border=2
    
    def calc_start_pixel(self,characters, length):
        total_width = characters * 8
        start_pixel = (length - total_width) // 2
        return start_pixel

    def show_dialog(self, title, text):
        # DRAW BOARDER
        self.display.fill_rect(self.x, self.y,self.width,self.height,theme['border'])
        # DRAW INNER BOX
        self.display.fill_rect(self.x+self.border, self.y+self.border,self.width-self.border*2,self.height-self.border*2,theme['bg'])
        # DRAW TITLE
        self.display.fill_rect(self.x+self.border, self.y+20, self.width-self.border*2, self.border, theme['border'])
        l=len(title)
        x=self.calc_start_pixel(l,self.width-self.border*2)+self.x
        self.display.write(font,title,x,self.y+self.border+1,theme['font'],theme['bg'])
        # DRAW TEXT
        l=len(text)
        x=self.calc_start_pixel(l,self.width-self.border*2)+self.x
        self.display.write(font,text,x,self.y+self.border+22,theme['font'],theme['bg'])
        # DRAW EXIT BUTTON
        self.display.fill_rect(self.x+self.width - 20, self.y+self.border, 18, 18, theme['warn'])
        self.display.write(font,"X", self.x+self.width - 15, self.y+self.border+2, theme['font'],theme['warn']) 
        # DRAW OK BUTTON
        #self.draw_rectangle(self.width - 80, self.height - 40, 40, 20, color=1)
        #self.display.text("OK", x=self.width - 70, y=self.height - 38, color=0) 

    def user_input(self, prompt):
        # 这里假设你有一个方法来接收用户的输入
        # 例如，如果你有一个按键读取函数，可以使用它来读取用户输入
        # 注意：这里的示例只是为了说明问题，实际上的方法调用可能会有所不同
        #user_input = read_user_input()
        #return user_input
        pass


dialog = DialogBox(20,20,222,140)

title_text = "Title"
main_text = "This is a dialog box."
dialog.show_dialog(title_text, main_text)

# 等待用户输入
# user_response = dialog.user_input("Please enter your response: ")
# print("User input:", user_response)
