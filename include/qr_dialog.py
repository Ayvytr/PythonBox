# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qr_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_QrDialog(object):
    def setupUi(self, QrDialog):
        QrDialog.setObjectName("QrDialog")
        QrDialog.resize(776, 591)
        self.layoutWidget = QtWidgets.QWidget(QrDialog)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 330, 1004, 244))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.labelImage = QtWidgets.QLabel(self.layoutWidget)
        self.labelImage.setMinimumSize(QtCore.QSize(240, 240))
        self.labelImage.setMaximumSize(QtCore.QSize(240, 240))
        self.labelImage.setText("")
        self.labelImage.setObjectName("labelImage")
        self.horizontalLayout_2.addWidget(self.labelImage)
        self.btnDecode = QtWidgets.QPushButton(self.layoutWidget)
        self.btnDecode.setMinimumSize(QtCore.QSize(100, 40))
        self.btnDecode.setObjectName("btnDecode")
        self.horizontalLayout_2.addWidget(self.btnDecode)
        self.etDecode = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.etDecode.sizePolicy().hasHeightForWidth())
        self.etDecode.setSizePolicy(sizePolicy)
        self.etDecode.setMinimumSize(QtCore.QSize(0, 40))
        self.etDecode.setObjectName("etDecode")
        self.horizontalLayout_2.addWidget(self.etDecode)
        self.btnCopyResult = QtWidgets.QPushButton(self.layoutWidget)
        self.btnCopyResult.setMinimumSize(QtCore.QSize(100, 40))
        self.btnCopyResult.setObjectName("btnCopyResult")
        self.horizontalLayout_2.addWidget(self.btnCopyResult)
        self.layoutWidget_2 = QtWidgets.QWidget(QrDialog)
        self.layoutWidget_2.setGeometry(QtCore.QRect(20, 50, 741, 242))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.et = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.et.setMinimumSize(QtCore.QSize(0, 40))
        self.et.setObjectName("et")
        self.horizontalLayout.addWidget(self.et)
        self.btnEncode = QtWidgets.QPushButton(self.layoutWidget_2)
        self.btnEncode.setMinimumSize(QtCore.QSize(100, 40))
        self.btnEncode.setObjectName("btnEncode")
        self.horizontalLayout.addWidget(self.btnEncode)
        self.labelEncodeImage = QtWidgets.QLabel(self.layoutWidget_2)
        self.labelEncodeImage.setMinimumSize(QtCore.QSize(240, 240))
        self.labelEncodeImage.setMaximumSize(QtCore.QSize(240, 240))
        self.labelEncodeImage.setText("")
        self.labelEncodeImage.setObjectName("labelEncodeImage")
        self.horizontalLayout.addWidget(self.labelEncodeImage)
        self.btnSavePhoto = QtWidgets.QPushButton(self.layoutWidget_2)
        self.btnSavePhoto.setMinimumSize(QtCore.QSize(100, 40))
        self.btnSavePhoto.setObjectName("btnSavePhoto")
        self.horizontalLayout.addWidget(self.btnSavePhoto)
        self.label = QtWidgets.QLabel(QrDialog)
        self.label.setGeometry(QtCore.QRect(30, 20, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(QrDialog)
        self.label_2.setGeometry(QtCore.QRect(30, 300, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(QrDialog)
        QtCore.QMetaObject.connectSlotsByName(QrDialog)

    def retranslateUi(self, QrDialog):
        _translate = QtCore.QCoreApplication.translate
        QrDialog.setWindowTitle(_translate("QrDialog", "Dialog"))
        self.btnDecode.setText(_translate("QrDialog", "解析"))
        self.btnCopyResult.setText(_translate("QrDialog", "复制结果"))
        self.btnEncode.setText(_translate("QrDialog", "生成"))
        self.btnSavePhoto.setText(_translate("QrDialog", "保存图片"))
        self.label.setText(_translate("QrDialog", "二维码生成"))
        self.label_2.setText(_translate("QrDialog", "二维码解析"))
