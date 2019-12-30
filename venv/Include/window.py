from tkinter import *
import requests


class Window:
    window = Tk()
    et = Entry(window)
    # performTranslate问题
    btnTranslate = Button(window, text="翻译", command=lambda:performTranslate())

    def __init__(self):
        self.window.geometry("800x640")
        self.window.title("PyBox")

        self.et.pack()

        self.btnTranslate.pack()

    def show(self):
        self.window.mainloop()

    def performTranslate(self):
        url = "https://translate.google.cn/#view=home&op=translate&sl=zh-CN&tl=en&text="
        response = requests.get(url)
        return response
