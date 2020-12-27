import tkinter as tk                   # 匯入tkinter模組
import tkinter.font as tkFont
from PIL import Image, ImageTk


class mainpage(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        self.button1 = tk.Button(self, text = "開始", command = self.clickBtn1, height = 1, width = 5)
        self.button2 = tk.Button(self, text = "離開", command = self.clickBtn2, height = 1, width = 5)
        self.canvas = tk.Canvas(self, width="600", height="300", bg = 'white')
        self.canvas.grid(row = 0, rowspan = 10, column = 0, columnspan = 18, sticky = tk.NE + tk.SW, padx = 1, pady = 3)

        self.img=Image.open("C://Users//許嘉城//Desktop//junior//商管程//期末專案//capm.png")
        self.pic = ImageTk.PhotoImage(self.img)
        self.canvas.create_image(400, 200, image = self.pic, anchor = tk.CENTER)
        self.button1.grid(row = 15, column = 1, columnspan = 7, sticky = tk.NE + tk.SW)
        self.button2.grid(row = 15, column = 9, columnspan = 7, sticky = tk.NE + tk.SW)
    def clickBtn1(self):
        pass
    def clickBtn2(self):
        pass


win = mainpage()
win.master.title("my stock portfolio")
win.mainloop()