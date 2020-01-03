import json
import sys
import webbrowser
from urllib.parse import unquote
from urllib.parse import urlparse, parse_qs, urlencode

from GoogleFreeTrans import Translator
from PyQt5.QtCore import QTimer, QDateTime
from PyQt5.QtWidgets import *

from include.ui.about_dialog import Ui_Dialog
from include.command import Command
from include.const import Const
from include.ui.exceptiondialog import ExceptionDialog
from include.ui.mainwindow import Ui_MainWindow
from include.ui.qrdialog import QrDialog


class MainWindow():
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.window = QMainWindow()
        self.mainWindow = Ui_MainWindow()
        self.mainWindow.setupUi(self.window)
        self.mainWindow.verticalLayout.addStretch()

        self.qtimer = QTimer()
        self.qtimer.timeout.connect(self.showTime)
        self.qtimer.start(1000)
        # mainWindow.statusbar.showMessage("状态栏消息")
        self.timeLabel = QLabel()
        # mainWindow.statusbar.addPermanentWidget(self.label)
        self.registerEvent()

    def showTime(self):
        self.mainWindow.statusbar.addPermanentWidget(self.timeLabel)
        time = QDateTime.currentDateTime()
        timeDisplay = time.toString("yyyy-MM-dd hh:mm:ss dddd")
        self.timeLabel.setText(timeDisplay)

    def show(self):
        self.window.show()
        sys.exit(self.app.exec_())

    def registerEvent(self):
        self.mainWindow.btnToChinese.clicked.connect(lambda: self.execCommand(Command.TO_CN))
        self.mainWindow.btnToEnglish.clicked.connect(lambda: self.execCommand(Command.TO_EN))
        self.mainWindow.btnJson.clicked.connect(lambda: self.execCommand(Command.JSON_FORMAT))
        self.mainWindow.btnUrlDecode.clicked.connect(lambda: self.execCommand(Command.URL_DECODE))
        self.mainWindow.btnUrlEncode.clicked.connect(lambda: self.execCommand(Command.URL_ENCODE))

        self.mainWindow.actionAbout.triggered.connect(self.about)
        self.mainWindow.actionGithub.triggered.connect(self.openGithub)
        self.mainWindow.actionIssue.triggered.connect(self.openIssue)
        self.mainWindow.actionQr.triggered.connect(self.showQrWindow)

    def execCommand(self, command: Command):
        text = self.mainWindow.etLeft.toPlainText()
        if len(text) == 0:
            self.mainWindow.statusbar.showMessage("Null!")
            return

        try:
            if command == Command.TO_CN:
                self.translateToChinese(text)
            elif command == Command.TO_EN:
                self.translateToEnglish(text)
            elif command == Command.JSON_FORMAT:
                self.jsonFormat(text)
            elif command == Command.URL_DECODE:
                self.urlDecode(text)
            elif command == Command.URL_ENCODE:
                self.urlEncode(text)
        except Exception as exception:
            print(exception)
            self.showExceptionDialog(exception)
            pass

    def translateToChinese(self, text):
        translator = Translator.translator(src='en', dest='zh-CN')
        value = translator.translate(text)
        self.mainWindow.etRight.setPlainText(value)

    def translateToEnglish(self, text):
        translator = Translator.translator(src='zh-CN', dest='en')
        value = translator.translate(text)
        self.mainWindow.etRight.setPlainText(value)

    def jsonFormat(self, text):
        value = json.dumps(text, indent=2)
        self.mainWindow.etRight.setPlainText(eval(value))

    def urlDecode(self, text):
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

    def urlEncode(self, text):
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

    def about(self):
        self.aboutDialog = QDialog()
        dialog = Ui_Dialog()
        dialog.setupUi(self.aboutDialog)
        dialog.btnOk.clicked.connect(self.aboutOk)
        self.aboutDialog.exec_()
        pass

    def aboutOk(self):
        self.aboutDialog.close()

    def showQrWindow(self):
        QrDialog().show()

    def openGithub(self):
        webbrowser.open(Const.GITHUB)
        pass

    def openIssue(self):
        webbrowser.open(Const.ISSUE)
        pass

    def showExceptionDialog(self, exception):
        ExceptionDialog(exception).show()
        pass
