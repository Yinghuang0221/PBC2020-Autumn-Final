import tkinter as tk
import tkinter.font as tkFont

class Qustion (tk.Frame):
    
    def __init__(self):
        tk.Frame.__init__(self)
        self.grid()
        self.createWidgets()
        

    def createWidgets(self):
        f1 = tkFont.Font(size = 48, family = "Courier new")
        f2 = tkFont.Font(size = 32, family = "Courier new")
        
        self.valueq1 = tk.StringVar()
        self.lblq1 = tk.Label(self, text = '1. 如果我的投資價值超過20%，我會感到不安。')
        self.rdiq11 = tk.Radiobutton(self, text='非常同意',variable=self.valueq1,value=1)
        self.rdiq12 = tk.Radiobutton(self, text='同意',variable=self.valueq1,value=2)
        self.rdiq13 = tk.Radiobutton(self, text='普通',variable=self.valueq1,value=3)
        self.rdiq14 = tk.Radiobutton(self, text='不同意',variable=self.valueq1,value=4)
        self.rdiq15 = tk.Radiobutton(self, text='非常不同意',variable=self.valueq1,value=5)
        def w_value():
            X = self.valueq1.get()
            return X
        X = w_value()
        print(X)
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
        self.lblan.grid(row = 99, column = 2)
        
        # 2個按鈕
        self.button1 = tk.Button(self, text = "上一步", command = self.clickBtn1)
        self.button2 = tk.Button(self, text = "下一步", command = self.clickBtn2)
       
        self.button1.grid(row = 100, column = 0, sticky = tk.W)
        self.button2.grid(row = 100, column = 4, sticky = tk.E)
        
    
    def clickBtn1(self):  # 上一步
        pass
    def clickBtn2(self):  # 下一步
        pass
    
que = Qustion()
que.master.title("Question")
que.mainloop()
