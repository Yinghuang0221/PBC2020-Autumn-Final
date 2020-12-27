import tkinter as tk
import tkinter.font as tkFont
from PIL import Image, ImageTk


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
        self.createWidgets()
        self.btu1 = tk.Button(self, text="開始",
                              command=lambda: master.switch_frame(PageOne))
        self.btu1.grid(row=1, column=0)
        self.btu1.grid_rowconfigure(1, weight=1)
        self.btu1.grid_columnconfigure(1, weight=1)
    def createWidgets(self):

        self.canvas = tk.Canvas(self, width="600", height="300", bg = 'white')
        self.canvas.grid(row = 0, column = 0,  sticky = tk.NE + tk.SW, padx = 1, pady = 3)

        self.img=Image.open("capm.png")
        self.pic = ImageTk.PhotoImage(self.img)
        self.canvas.create_image(400, 200, image = self.pic, anchor = tk.CENTER)


class PageOne(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.createWidgets()
        self.btu_frontpage = tk.Button(self, text="上一步",
                                       command=lambda: master.switch_frame(StartPage))
        self.btu_nextpage = tk.Button(self, text="下一步",
                                      command=lambda: master.switch_frame(PageTwo))
        self.btu_frontpage.grid(row=99, column=0, sticky=tk.W)
        self.btu_nextpage.grid(row=99, column=4, sticky=tk.E)

    def createWidgets(self):
        # 9題題目與選項
        valueq1 = tk.IntVar()
        self.lblq1 = tk.Label(self, text='1. 如果我的投資價值超過20%，我會感到不安。',
                              bg='Thistle')
        self.rdiq11 = tk.Radiobutton(self, text='非常同意', variable=valueq1,
                                     value=1)
        self.rdiq12 = tk.Radiobutton(self, text='同意', variable=valueq1,
                                     value=2)
        self.rdiq13 = tk.Radiobutton(self, text='普通', variable=valueq1,
                                     value=3)
        self.rdiq14 = tk.Radiobutton(self, text='不同意', variable=valueq1,
                                     value=4)
        self.rdiq15 = tk.Radiobutton(self, text='非常不同意', variable=valueq1,
                                     value=5)
        self.lblq1.grid(row=0, column=0, columnspan=5, sticky=tk.W)
        self.rdiq11.grid(row=1, column=0, sticky=tk.W)
        self.rdiq12.grid(row=1, column=1, sticky=tk.W)
        self.rdiq13.grid(row=1, column=2, sticky=tk.W)
        self.rdiq14.grid(row=1, column=3, sticky=tk.W)
        self.rdiq15.grid(row=1, column=4, sticky=tk.W)

        valueq2 = tk.IntVar()
        self.lblq2 = tk.Label(self, text='2. 為了能獲得更高的報酬，我願意接受較高的風險。',
                              bg='Thistle')
        self.rdiq21 = tk.Radiobutton(self, text='非常不同意', variable=valueq2,
                                     value=1)
        self.rdiq22 = tk.Radiobutton(self, text='不同意', variable=valueq2,
                                     value=2)
        self.rdiq23 = tk.Radiobutton(self, text='普通', variable=valueq2,
                                     value=3)
        self.rdiq24 = tk.Radiobutton(self, text='同意', variable=valueq2,
                                     value=4)
        self.rdiq25 = tk.Radiobutton(self, text='非常同意', variable=valueq2,
                                     value=5)
        self.lblq2.grid(row=2, column=0, columnspan=5, sticky=tk.W)
        self.rdiq21.grid(row=3, column=0, sticky=tk.W)
        self.rdiq22.grid(row=3, column=1, sticky=tk.W)
        self.rdiq23.grid(row=3, column=2, sticky=tk.W)
        self.rdiq24.grid(row=3, column=3, sticky=tk.W)
        self.rdiq25.grid(row=3, column=4, sticky=tk.W)

        valueq3 = tk.IntVar()
        self.lblq3 = tk.Label(self, text='3. 您平時多久調整一次您的投資組合(指的是大方向的資產配置，而不是個股的選擇) ?',
                              bg='Thistle')
        self.rdiq31 = tk.Radiobutton(self, text='只要一有損失就調整', variable=valueq3,
                                     value=1)
        self.rdiq32 = tk.Radiobutton(self, text='三年', variable=valueq3,
                                     value=2)
        self.rdiq33 = tk.Radiobutton(self, text='3-5年', variable=valueq3,
                                     value=3)
        self.rdiq34 = tk.Radiobutton(self, text='當有顯著獲利時', variable=valueq3,
                                     value=4)
        self.rdiq35 = tk.Radiobutton(self, text='5年以上', variable=valueq3,
                                     value=5)
        self.lblq3.grid(row=4, column=0, columnspan=5, sticky=tk.W)
        self.rdiq31.grid(row=5, column=0, sticky=tk.W)
        self.rdiq32.grid(row=5, column=1, sticky=tk.W)
        self.rdiq33.grid(row=5, column=2, sticky=tk.W)
        self.rdiq34.grid(row=5, column=3, sticky=tk.W)
        self.rdiq35.grid(row=5, column=4, sticky=tk.W)

        valueq4 = tk.IntVar()
        self.lblq4 = tk.Label(self, text='4. 我要追求長期報酬，我可以忍受短期的價值波動。',
                              bg='Thistle')
        self.rdiq41 = tk.Radiobutton(self, text='非常不同意', variable=valueq3,
                                     value=1)
        self.rdiq42 = tk.Radiobutton(self, text='不同意', variable=valueq4,
                                     value=2)
        self.rdiq43 = tk.Radiobutton(self, text='沒意見', variable=valueq4,
                                     value=3)
        self.rdiq44 = tk.Radiobutton(self, text='同意', variable=valueq4,
                                     value=4)
        self.rdiq45 = tk.Radiobutton(self, text='非常同意', variable=valueq4,
                                     value=5)
        self.lblq4.grid(row=6, column=0, columnspan=5, sticky=tk.W)
        self.rdiq41.grid(row=7, column=0, sticky=tk.W)
        self.rdiq42.grid(row=7, column=1, sticky=tk.W)
        self.rdiq43.grid(row=7, column=2, sticky=tk.W)
        self.rdiq44.grid(row=7, column=3, sticky=tk.W)
        self.rdiq45.grid(row=7, column=4, sticky=tk.W)

        valueq5 = tk.IntVar()
        self.lblq5 = tk.Label(self, text='5. 您對風險的接受程度 :', bg='Thistle')
        self.rdiq51 = tk.Radiobutton(self, text='極低風險接受者', variable=valueq5,
                                     value=1)
        self.rdiq52 = tk.Radiobutton(self, text='低風險接受者', variable=valueq5,
                                     value=2)
        self.rdiq53 = tk.Radiobutton(self, text='風險中立者', variable=valueq5,
                                     value=3)
        self.rdiq54 = tk.Radiobutton(self, text='高風險接受者', variable=valueq5,
                                     value=4)
        self.rdiq55 = tk.Radiobutton(self, text='極高風險接受者', variable=valueq5,
                                     value=5)
        self.lblq5.grid(row=8, column=0, columnspan=5, sticky=tk.W)
        self.rdiq51.grid(row=9, column=0, sticky=tk.W)
        self.rdiq52.grid(row=9, column=1, sticky=tk.W)
        self.rdiq53.grid(row=9, column=2, sticky=tk.W)
        self.rdiq54.grid(row=9, column=3, sticky=tk.W)
        self.rdiq55.grid(row=9, column=4, sticky=tk.W)

        valueq6 = tk.IntVar()
        self.lblq6 = tk.Label(self, text='6. 您對金融市場及金融實務的了解 :', bg='Thistle')
        self.rdiq61 = tk.Radiobutton(self, text='不清楚也沒興趣', variable=valueq6,
                                     value=1)
        self.rdiq62 = tk.Radiobutton(self, text='不是很清楚', variable=valueq6,
                                     value=2)
        self.rdiq63 = tk.Radiobutton(self, text='初淺了解(我只知道投資要多角化降低風險)',
                                     variable=valueq6, value=3)
        self.rdiq64 = tk.Radiobutton(self, text='清楚(我知道不同市場，不同標的有不同報酬與風險)',
                                     variable=valueq6, value=4)
        self.rdiq65 = tk.Radiobutton(self, text='很清楚(我知道所有的金融市場，也熟悉影響投資報酬與風險之因素)',
                                     variable=valueq6, value=5)
        self.lblq6.grid(row=10, column=0, columnspan=5, sticky=tk.W)
        self.rdiq61.grid(row=12, column=0, columnspan=5, sticky=tk.W)
        self.rdiq62.grid(row=13, column=0, columnspan=5, sticky=tk.W)
        self.rdiq63.grid(row=14, column=0, columnspan=5, sticky=tk.W)
        self.rdiq64.grid(row=15, column=0, columnspan=5, sticky=tk.W)
        self.rdiq65.grid(row=16, column=0, columnspan=5, sticky=tk.W)

        valueq7 = tk.IntVar()
        self.lblq7 = tk.Label(self, text='7. 我投資最大的要求是保值，安全；這比獲利更重要。',
                              bg='Thistle')
        self.rdiq71 = tk.Radiobutton(self, text='非常同意', variable=valueq7,
                                     value=1)
        self.rdiq72 = tk.Radiobutton(self, text='同意', variable=valueq7,
                                     value=2)
        self.rdiq73 = tk.Radiobutton(self, text='沒意見', variable=valueq7,
                                     value=3)
        self.rdiq74 = tk.Radiobutton(self, text='不同意', variable=valueq7,
                                     value=4)
        self.rdiq75 = tk.Radiobutton(self, text='非常不同意', variable=valueq7,
                                     value=5)
        self.lblq7.grid(row=17, column=0, columnspan=5, sticky=tk.W)
        self.rdiq71.grid(row=18, column=0, sticky=tk.W)
        self.rdiq72.grid(row=18, column=1, sticky=tk.W)
        self.rdiq73.grid(row=18, column=2, sticky=tk.W)
        self.rdiq74.grid(row=18, column=3, sticky=tk.W)
        self.rdiq75.grid(row=18, column=4, sticky=tk.W)

        valueq8 = tk.IntVar()
        self.lblq8 = tk.Label(self, text='8. 當您做完一項投資決策後，您的感覺是 :',
                              bg='Thistle')
        self.rdiq81 = tk.Radiobutton(self, text='非常擔心', variable=valueq8,
                                     value=1)
        self.rdiq82 = tk.Radiobutton(self, text='擔心', variable=valueq8,
                                     value=2)
        self.rdiq83 = tk.Radiobutton(self, text='不放在心上', variable=valueq8,
                                     value=3)
        self.rdiq84 = tk.Radiobutton(self, text='樂觀', variable=valueq8,
                                     value=4)
        self.rdiq85 = tk.Radiobutton(self, text='非常樂觀', variable=valueq8,
                                     value=5)
        self.lblq8.grid(row=19, column=0, columnspan=5, sticky=tk.W)
        self.rdiq81.grid(row=20, column=0, sticky=tk.W)
        self.rdiq82.grid(row=20, column=1, sticky=tk.W)
        self.rdiq83.grid(row=20, column=2, sticky=tk.W)
        self.rdiq84.grid(row=20, column=3, sticky=tk.W)
        self.rdiq85.grid(row=20, column=4, sticky=tk.W)

        valueq9 = tk.IntVar()
        self.lblq9 = tk.Label(self, text='9. 長期來看，高風險會有高報酬補償，如果您做一個10-20年期的投資，您會選擇下列何者 ?', bg='Thistle')
        self.rdiq91 = tk.Radiobutton(self, text='有一投資每10年會有一次負報酬，但每年報酬介在-2%~11%之間，平均年報酬是4.1%', variable=valueq9, value=1)
        self.rdiq92 = tk.Radiobutton(self, text='有一投資每10年會有一次負報酬，但每年報酬介在-5%~14%之間，平均年報酬是4.7%', variable=valueq9, value=2)
        self.rdiq93 = tk.Radiobutton(self, text='有一投資每10年會有一次負報酬，但每年報酬介在-7%~17%之間，平均年報酬是5.0%', variable=valueq9, value=3)
        self.rdiq94 = tk.Radiobutton(self, text='有一投資每10年會有一次負報酬，但每年報酬介在-9%~20%之間，平均年報酬是5.5%', variable=valueq9, value=4)
        self.rdiq95 = tk.Radiobutton(self, text='有一投資每10年會有一次負報酬，但每年報酬介在-11%~23%之間，平均年報酬是5.9%', variable=valueq9, value=5)
        self.lblq9.grid(row=21, column=0, columnspan=5, sticky=tk.W)
        self.rdiq91.grid(row=22, column=0, columnspan=5, sticky=tk.W)
        self.rdiq92.grid(row=23, column=0, columnspan=5, sticky=tk.W)
        self.rdiq93.grid(row=24, column=0, columnspan=5, sticky=tk.W)
        self.rdiq94.grid(row=25, column=0, columnspan=5, sticky=tk.W)
        self.rdiq95.grid(row=26, column=0, columnspan=5, sticky=tk.W)

        # Get所使用者回答之value並相加
        def sum():
            weight1 = valueq1.get()
            weight2 = valueq2.get()
            weight3 = valueq3.get()
            weight4 = valueq4.get()
            weight5 = valueq5.get()
            weight6 = valueq6.get()
            weight7 = valueq7.get()
            weight8 = valueq8.get()
            weight9 = valueq9.get()
            total_weight = (weight1 + weight2 + weight3 + weight4 + weight5 +
                            weight6 + weight7 + weight8 + weight9)
            total_weight_str = str(total_weight)
            return total_weight_str

        def update():
            weight_value.set(sum())

        weight_value = tk.StringVar()
        weight_value.set(sum())

        # 利用按鈕更新獲得的value
        self.lblan = tk.Button(self, text=str('您的風險趨避程度為'),
                               command=lambda: [sum(), update()])
        self.vale = tk.Label(self, textvariable=weight_value)

        self.vale.grid(row=98, column=3)
        self.lblan.grid(row=98, column=2)


class PageTwo(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.createWidgets()
        self.btu_frontpage = tk.Button(self, text="上一步",
                                       command=lambda: master.switch_frame(PageOne))
        self.btu_frontpage.grid(row=99, column=1)

    def createWidgets(self):
        f1 = tkFont.Font(size=10)
        # 三個條件給使用者填
        self.lable1 = tk.Label(self, text="投資預算區間:", bg='Thistle', font=f1)
        self.lable2 = tk.Label(self, text="投資標的數目上限:", bg="Thistle", font=f1)
        self.lable3 = tk.Label(self, text="投資標的前一日收盤價區間:", bg="Thistle",
                               font=f1)
        self.lable4 = tk.Label(self, text="~")
        self.lable6 = tk.Label(self, text="~")

        self.lable1.grid(row=2, column=0, columnspan=5, sticky=tk.NE+tk.SW)
        self.lable2.grid(row=5, column=0, columnspan=5, sticky=tk.NE+tk.SW)
        self.lable3.grid(row=8, column=0, columnspan=5, sticky=tk.NE+tk.SW)
        self.lable4.grid(row=3, column=2)
        self.lable6.grid(row=9, column=2)

        # 給使用者輸入數字的5個地方
        self.entry1_1 = tk.Entry(self, width=10)
        self.entry1_2 = tk.Entry(self, width=10)
        self.entry2_1 = tk.Entry(self, width=10)
        self.entry3_1 = tk.Entry(self, width=10)
        self.entry3_2 = tk.Entry(self, width=10)

        self.entry1_1.grid(row=3, column=1)
        self.entry1_2.grid(row=3, column=3)
        self.entry2_1.grid(row=6, column=1, columnspan=3, sticky=tk.SW+tk.NE)
        self.entry3_1.grid(row=9, column=1)
        self.entry3_2.grid(row=9, column=3)

if __name__ == "__main__":
    app = Project()
    app.geometry('700x700')
    app.title('My Stock Tool')
    app.grid_rowconfigure(0, weight=1)
    app.grid_columnconfigure(0, weight=1)
    app.mainloop()