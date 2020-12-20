import tkinter as tk
import tkinter.font as tkFont
class StockTool(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.grid()
        self.createWidgets()
        
    def createWidgets(self):
        # 標示文字        
        self.lable1 = tk.Label(self, text = "投資預算區間:", bg = 'Thistle')
        self.lable2 = tk.Label(self, text = "投資標的數目區間:", bg = "Thistle")
        self.lable3 = tk.Label(self, text = "投資標的單價區間:", bg = "Thistle")
        self.lable4 = tk.Label(self, text = "~")
        self.lable5 = tk.Label(self, text = "~")
        self.lable6 = tk.Label(self, text = "~")
        
        self.lable1.grid(row = 2, column = 0, columnspan = 5, sticky = tk.NE + tk.SW)
        self.lable2.grid(row = 5, column = 0, columnspan = 5, sticky = tk.NE + tk.SW)
        self.lable3.grid(row = 8, column = 0, columnspan = 5, sticky = tk.NE + tk.SW)
        self.lable4.grid(row = 3, column = 2)
        self.lable5.grid(row = 6, column = 2)
        self.lable6.grid(row = 9, column = 2)
        
        # 3個按鈕
        self.button1 = tk.Button(self, text = "上一步", command = self.clickBtn1)
        self.button2 = tk.Button(self, text = "下一步", command = self.clickBtn2)
        self.button3 = tk.Button(self, text = "離開", command = self.clickBtn3)
        
        self.button1.grid(row = 11, column = 1, sticky = tk.NE + tk.SW)
        self.button2.grid(row = 11, column = 2, sticky = tk.NE + tk.SW)
        self.button3.grid(row = 11, column = 3, sticky = tk.NE + tk.SW)
        
        # 給使用者輸入數字的6個地方
        self.entry1_1 = tk.Entry(self, width=10)
        self.entry1_2 = tk.Entry(self, width=10)
        self.entry2_1 = tk.Entry(self, width=10)
        self.entry2_2 = tk.Entry(self, width=10)
        self.entry3_1 = tk.Entry(self, width=10)
        self.entry3_2 = tk.Entry(self, width=10)
        
        self.entry1_1.grid(row = 3, column = 1)
        self.entry1_2.grid(row = 3, column = 3)
        self.entry2_1.grid(row = 6, column = 1)
        self.entry2_2.grid(row = 6, column = 3)
        self.entry3_1.grid(row = 9, column = 1)
        self.entry3_2.grid(row = 9, column = 3)
          
        
    def clickBtn1(self):  # 上一步
        pass
    def clickBtn2(self):  # 下一步
        pass
    def clickBtn3(self):  # 離開
        pass
        

cal = StockTool()
cal.master.title("My StockTool")
cal.mainloop()
