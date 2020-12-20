import tkinter as tk
import tkinter.font as tkFont

class Project(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(StartPage)
    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.grid()
class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.grid()
        self.btu1 =tk.Button(self, text="開始",command=lambda: master.switch_frame(PageOne))
        self.btu1.grid(row = 1, column = 1)
        self.btu1.grid_rowconfigure(1, weight=1)
        self.btu1.grid_columnconfigure(1, weight=1)

class PageOne(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.createWidgets()
        self.btu_frontpage = tk.Button(self, text="上一步",command=lambda: master.switch_frame(StartPage))
        self.btu_nextpage = tk.Button(self, text="下一步",command=lambda: master.switch_frame(PageTwo))
        self.btu_frontpage.grid(row = 99, column = 1)
        self.btu_nextpage.grid(row = 99, column = 3)
        
    def createWidgets(self):
        f1 = tkFont.Font(size = 48, family = "Courier new")
        f2 = tkFont.Font(size = 32, family = "Courier new")
        
        self.valueq1 = tk.IntVar()
        self.lblq1 = tk.Label(self, text = '1. 如果我的投資價值超過20%，我會感到不安。')
        self.rdiq11 = tk.Radiobutton(self, text='非常同意',variable=self.valueq1,value=1)
        self.rdiq12 = tk.Radiobutton(self, text='同意',variable=self.valueq1,value=2)
        self.rdiq13 = tk.Radiobutton(self, text='普通',variable=self.valueq1,value=3)
        self.rdiq14 = tk.Radiobutton(self, text='不同意',variable=self.valueq1,value=4)
        self.rdiq15 = tk.Radiobutton(self, text='非常不同意',variable=self.valueq1,value=5)
        self.lblq1.grid(row = 0, column = 0, columnspan = 5)
        self.rdiq11.grid(row = 1, column = 0)
        self.rdiq12.grid(row = 1, column = 1)
        self.rdiq13.grid(row = 1, column = 2)
        self.rdiq14.grid(row = 1, column = 3)
        self.rdiq15.grid(row = 1, column = 4)
        
        valueq2 = tk.IntVar()
        self.lblq2 = tk.Label(self, text = '2. 為了能獲得更高的報酬，我願意接受較高的風險。')
        self.rdiq21 = tk.Radiobutton(self, text='非常不同意',variable=valueq2,value=1)
        self.rdiq22 = tk.Radiobutton(self, text='不同意',variable=valueq2,value=2)
        self.rdiq23 = tk.Radiobutton(self, text='普通',variable=valueq2,value=3)
        self.rdiq24 = tk.Radiobutton(self, text='同意',variable=valueq2,value=4)
        self.rdiq25 = tk.Radiobutton(self, text='非常同意',variable=valueq2,value=5)
        self.lblq2.grid(row = 2, column = 0, columnspan = 5)
        self.rdiq21.grid(row = 3, column = 0)
        self.rdiq22.grid(row = 3, column = 1)
        self.rdiq23.grid(row = 3, column = 2)
        self.rdiq24.grid(row = 3, column = 3)
        self.rdiq25.grid(row = 3, column = 4)
        
        valueq3 = tk.IntVar()
        self.lblq3 = tk.Label(self, text = '3. 您平時多久調整一次您的投資組合(指的是大方向的資產配置，而不是個股的選擇)')
        self.rdiq31 = tk.Radiobutton(self, text='只要一有損失就調整',variable=valueq3,value=1)
        self.rdiq32 = tk.Radiobutton(self, text='三年',variable=valueq3,value=2)
        self.rdiq33 = tk.Radiobutton(self, text='3-5年',variable=valueq3,value=3)
        self.rdiq34 = tk.Radiobutton(self, text='當有顯著獲利時',variable=valueq3,value=4)
        self.rdiq35 = tk.Radiobutton(self, text='5年以上',variable=valueq3,value=5)
        self.lblq3.grid(row = 4, column = 0, columnspan = 5)
        self.rdiq31.grid(row = 5, column = 0)
        self.rdiq32.grid(row = 5, column = 1)
        self.rdiq33.grid(row = 5, column = 2)
        self.rdiq34.grid(row = 5, column = 3)
        self.rdiq35.grid(row = 5, column = 4)
        
        self.lblan = tk.Label(self, text = str('您的風險趨避程度為'))
        self.lblan.grid(row = 98, column = 2)

class PageTwo(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.createWidgets()
        self.btu_frontpage = tk.Button(self, text="上一步",command=lambda: master.switch_frame(PageOne))
        self.btu_frontpage.grid(row = 99, column = 1)
    
    def createWidgets(self):
        # 標示文字        
        self.lable1 = tk.Label(self, text = "投資預算區間:", bg = 'Thistle')
        self.lable2 = tk.Label(self, text = "投資標的數目上限:", bg = "Thistle")
        self.lable3 = tk.Label(self, text = "投資標的前一日收盤價區間:", bg = "Thistle")
        self.lable4 = tk.Label(self, text = "~")
        self.lable6 = tk.Label(self, text = "~")
        
        self.lable1.grid(row = 2, column = 0, columnspan = 5, sticky = tk.NE + tk.SW)
        self.lable2.grid(row = 5, column = 0, columnspan = 5, sticky = tk.NE + tk.SW)
        self.lable3.grid(row = 8, column = 0, columnspan = 5, sticky = tk.NE + tk.SW)
        self.lable4.grid(row = 3, column = 2)
        self.lable6.grid(row = 9, column = 2)
        

        
        # 給使用者輸入數字的5個地方
        self.entry1_1 = tk.Entry(self, width=10)
        self.entry1_2 = tk.Entry(self, width=10)
        self.entry2_1 = tk.Entry(self, width=10)

        self.entry3_1 = tk.Entry(self, width=10)
        self.entry3_2 = tk.Entry(self, width=10)
        
        self.entry1_1.grid(row = 3, column = 1)
        self.entry1_2.grid(row = 3, column = 3)
        self.entry2_1.grid(row = 6, column = 1, columnspan = 5, sticky = tk.NE + tk.SW)
        self.entry3_1.grid(row = 9, column = 1)
        self.entry3_2.grid(row = 9, column = 3)
if __name__ == "__main__":
    app = Project()
    app.geometry('700x700')
    app.grid_rowconfigure(0, weight=1)
    app.grid_columnconfigure(0, weight=1)
    app.mainloop()