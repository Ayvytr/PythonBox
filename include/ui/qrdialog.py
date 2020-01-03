import os

import pyperclip
import qrcode
from PIL import Image
from PyQt5 import QtGui
from PyQt5.QtGui import QPalette, QColor, QFont
from PyQt5.QtWidgets import QDialog, QFileDialog, QToolTip
from pyzbar.pyzbar import decode

from include.ui.qr_dialog import Ui_QrDialog


class QrDialog():
    def __init__(self):
        self.dialog = QDialog()
        self.qrDialog = Ui_QrDialog()
        self.qrDialog.setupUi(self.dialog)
        self.qrDialog.btnEncode.clicked.connect(self.encodeQrCode)
        self.qrDialog.btnDecode.clicked.connect(self.decodeQrCode)
        self.qrDialog.btnSavePhoto.clicked.connect(self.saveEncodeQrCode)
        self.qrDialog.btnCopyResult.clicked.connect(self.copyQrResult)

        self.qrDialog.labelEncodeImage.setScaledContents(True)
        self.qrDialog.labelEncodeImage.setAutoFillBackground(True)
        self.qrDialog.labelImage.setScaledContents(True)
        self.qrDialog.labelImage.setAutoFillBackground(True)

        palette = QPalette()
        palette.setColor(QPalette.Background, QColor(255, 255, 255))
        self.qrDialog.labelEncodeImage.setPalette(palette)
        self.qrDialog.labelImage.setPalette(palette)

        pass

    def show(self):
        self.dialog.exec_()

    def close(self):
        self.dialog.close()

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
        fileName, fileType = QFileDialog.getOpenFileName(
            filter='Jpg (*.jpg);;Jpeg (*.jpeg);;Png (*.png);;Bmp (*.bmp);;All Files (*.*)')
        if len(fileName) == 0:
            return

        self.qrDialog.labelImage.setPixmap(QtGui.QPixmap(fileName))
        value = decode(Image.open(fileName))
        v = value[0].data.decode('utf-8')
        self.qrDialog.etDecode.setText(v)

    def copyQrResult(self):
        value = self.qrDialog.etDecode.text()
        if len(value) == 0:
            return

        pyperclip.copy(value)
        # 不起作用
        QToolTip.setFont(QFont("SansSerif", 24))
        self.qrDialog.btnCopyResult.setToolTip("复制成功")
