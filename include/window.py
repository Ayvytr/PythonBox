import json
import sys
from urllib.parse import quote, urlparse, parse_qs, urlunparse, parse_qsl, urlencode
from urllib.parse import unquote

from GoogleFreeTrans import Translator
from PyQt5.QtWidgets import *
from url_decode import urldecode

from include.mainwindow import Ui_MainWindow


class MainWindow():
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.window = QMainWindow()
        self.mainWindow = Ui_MainWindow()
        self.mainWindow.setupUi(self.window)
        # mainWindow.statusbar.showMessage("状态栏消息")
        # self.label = QLabel()
        # self.label.setText("label")
        # mainWindow.statusbar.addPermanentWidget(self.label)
        self.registerEvent()

    def show(self):
        self.window.show()
        sys.exit(self.app.exec_())

    def registerEvent(self):
        self.mainWindow.btnToChinese.clicked.connect(self.translateToChinese)
        self.mainWindow.btnToEnglish.clicked.connect(self.translateToEnglish)
        self.mainWindow.btnJson.clicked.connect(self.jsonFormat)
        self.mainWindow.btnUrlDecode.clicked.connect(self.urlDecode)
        self.mainWindow.btnUrlEncode.clicked.connect(self.urlEncode)

    def translateToChinese(self):
        text = self.mainWindow.etLeft.toPlainText()
        if len(text) == 0:
            self.mainWindow.statusbar.showMessage("Null!")
            return

        translator = Translator.translator(src='en', dest='zh-CN')
        value = translator.translate(text)
        self.mainWindow.etRight.setPlainText(value)

    def translateToEnglish(self):
        text = self.mainWindow.etLeft.toPlainText()
        if len(text) == 0:
            self.mainWindow.statusbar.showMessage("Null!")
            return

        translator = Translator.translator(src='zh-CN', dest='en')
        value = translator.translate(text)
        self.mainWindow.etRight.setPlainText(value)

    def jsonFormat(self):
        text = self.mainWindow.etLeft.toPlainText()
        if len(text) == 0:
            self.mainWindow.statusbar.showMessage("Null!")
            return

        try:
            value = json.dumps(text, indent=2)
        except Exception as exception:
            print(exception)
            self.mainWindow.statusbar.showMessage(str(exception))

        self.mainWindow.etRight.setPlainText(eval(value))

    def urlDecode(self):
        text = self.mainWindow.etLeft.toPlainText()
        if len(text) == 0:
            self.mainWindow.statusbar.showMessage("Null!")
            return

        try:
            result = urlparse(text)
            qs = parse_qs(result.query)
            if len(qs) == 0:
                self.mainWindow.etRight.setPlainText(text)
            else:
                query = ""
                for key, value in qs.items():
                    query += key + "=" + unquote(value[0]) + "&"

                if len(query) > 0:
                    query = query[0:-1]
                url = text[0:text.find('?') + 1]

                self.mainWindow.etRight.setPlainText(url + query)

        except Exception as exception:
            self.mainWindow.statusbar.showMessage(str(exception))
            return

    def urlEncode(self):
        text = self.mainWindow.etLeft.toPlainText()
        if len(text) == 0:
            self.mainWindow.statusbar.showMessage("Null!")
            return

        try:
            result = urlparse(text)
            qs = parse_qs(result.query)
            if len(qs) == 0:
                self.mainWindow.etRight.setPlainText(text)
            else:
                map = {}
                for key, value in qs.items():
                    map[key] = value[0]
                encodeQuery = urlencode(map)
                url = text[0:text.find('?') + 1]

                self.mainWindow.etRight.setPlainText(url + encodeQuery)

        except Exception as exception:
            self.mainWindow.statusbar.showMessage(str(exception))
            return

