from tkinter import *
import requests
from GoogleFreeTrans import Translator


class Window:

    def __init__(self):
        self.window = Tk()
        width = 800
        height = 640
        self.window.geometry(str(width) + "x" + str(height))
        self.window.title("PyBox")

        screenwidth = self.window.winfo_screenwidth()
        screenheight = self.window.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.window.geometry(alignstr)

        self.etInput = Entry(self.window)
        # self.etInput.pack()
        self.etInput.grid(row=0,column=0, sticky='w', columnspan=10)

        self.btnTranslate = Button(self.window, text=" 翻译 ", command=self.performTranslate)
        self.btnTranslate.grid(row=0, column=1)
        # self.btnTranslate.pack(side='right')

        self.tvTranslate = Text(self.window)
        # self.tvTranslate.pack()
        self.tvTranslate.grid(row=1, column=0)

    def show(self):
        self.window.mainloop()

    def performTranslate(self):
        text = self.etInput.get()
        if len(text) == 0:
            return

        translator = Translator.translator(src='en', dest='zh-CN')
        value = translator.translate(text)

        self.tvTranslate.delete(0.0, END)
        self.tvTranslate.insert("insert", value)
