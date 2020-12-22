import tkinter as tk                   # 匯入tkinter模組
import tkinter.font as tkFont
from PIL import Image, ImageTk


class mainpage(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.grid()
        #self.image = ImageTk.PhotoImage(file = 'stock.png')
        
        self.createWidgets()

    def createWidgets(self):

        self.button1 = tk.Button(self, text = "開始", command = self.clickBtn1, height = 1, width = 5)
        self.button2 = tk.Button(self, text = "離開", command = self.clickBtn2, height = 1, width = 5)
        
        self.button1.grid(row = 15, column = 1, sticky = tk.NE + tk.SW)
        self.button2.grid(row = 15, column = 2, sticky = tk.NE + tk.SW)
    def clickBtn1(self):
        pass
    def clickBtn2(self):
        pass


win = mainpage()
win.master.title("my stock portfolio")
win.mainloop()