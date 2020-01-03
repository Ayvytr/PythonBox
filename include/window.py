import json
import os
import sys
from urllib.parse import quote, urlparse, parse_qs, urlunparse, parse_qsl, urlencode
from urllib.parse import unquote

import qrcode
import zxing
from GoogleFreeTrans import Translator
from PIL import Image
from PyQt5 import Qt, QtGui
from PyQt5.QtCore import QTimer, QDateTime, QRectF
from PyQt5.QtGui import QPixmap, QPalette, QColor
from PyQt5.QtWidgets import *
from pyzbar.pyzbar import decode
from url_decode import urldecode

from include.about_dialog import Ui_Dialog
from include.mainwindow import Ui_MainWindow
from include.qr_dialog import Ui_QrDialog


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
        self.mainWindow.btnToChinese.clicked.connect(self.translateToChinese)
        self.mainWindow.btnToEnglish.clicked.connect(self.translateToEnglish)
        self.mainWindow.btnJson.clicked.connect(self.jsonFormat)
        self.mainWindow.btnUrlDecode.clicked.connect(self.urlDecode)
        self.mainWindow.btnUrlEncode.clicked.connect(self.urlEncode)

        self.mainWindow.actionAbout.triggered.connect(self.about)
        self.mainWindow.actionGithub.triggered.connect(self.openGithub)
        self.mainWindow.actionIssue.triggered.connect(self.openIssue)
        self.mainWindow.actionQr.triggered.connect(self.showQrWindow)

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
        self.qrQDialog = QDialog()
        self.qrDialog = Ui_QrDialog()
        self.qrDialog.setupUi(self.qrQDialog)
        # dialog.btnOk.clicked.connect(self.aboutOk)
        self.qrDialog.btnEncode.clicked.connect(self.encodeQrCode)
        self.qrDialog.btnDecode.clicked.connect(self.decodeQrCode)
        self.qrDialog.btnSavePhoto.clicked.connect(self.saveEncodeQrCode)
        self.qrDialog.labelEncodeImage.setScaledContents(True)
        self.qrDialog.labelEncodeImage.setAutoFillBackground(True)
        self.qrDialog.labelImage.setScaledContents(True)
        self.qrDialog.labelImage.setAutoFillBackground(True)

        palette = QPalette()
        palette.setColor(QPalette.Background, QColor(255, 255, 255))
        self.qrDialog.labelEncodeImage.setPalette(palette)
        self.qrDialog.labelImage.setPalette(palette)

        self.qrQDialog.exec_()

        pass

    def openGithub(self):
        pass

    def openIssue(self):
        pass

    def encodeQrCode(self):
        filename = 'tempEncodeQr.png'
        qr = qrcode.QRCode(
            version=None,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=1,
        )

        text = self.qrDialog.et.text()
        if len(text) == 0:
            return

        qr.clear()
        qr.add_data(text)
        qr.make(fit=True)
        self.imgEncode = qr.make_image()
        self.imgEncode.save(filename)
        self.qrDialog.labelEncodeImage.setPixmap(QtGui.QPixmap(filename))

        if os.path.exists(filename):
            os.remove(filename)

    def saveEncodeQrCode(self):
        try:
            if self.imgEncode is not None:
                fileName, fileType = QFileDialog.getSaveFileName(filter='Jpg (*.jpg);;Png (*.png)')
                if len(fileName) > 0:
                    self.imgEncode.save(fileName)
        except AttributeError:
            pass

    def decodeQrCode(self):
        fileName, fileType = QFileDialog.getOpenFileName(filter='Jpg (*.jpg);;Jpeg (*.jpeg);;Png (*.png);;Bmp (*.bmp);;All Files (*.*)')
        if len(fileName) == 0:
            return

        img = QtGui.QPixmap(fileName)
        print(img, img.isNull())
            # .scaled(self.qrDialog.labelImage.width(),
            #                                  self.qrDialog.labelImage.height())
        self.qrDialog.labelImage.setPixmap(img)

        value = decode(Image.open(fileName))
        v = value[0].data.decode('utf-8')
        self.qrDialog.etDecode.setText(v)




