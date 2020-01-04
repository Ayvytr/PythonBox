# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'exception_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ExceptionDialog(object):
    def setupUi(self, ExceptionDialog):
        ExceptionDialog.setObjectName("ExceptionDialog")
        ExceptionDialog.resize(640, 400)
        ExceptionDialog.setModal(True)
        self.tv = QtWidgets.QLabel(ExceptionDialog)
        self.tv.setGeometry(QtCore.QRect(30, 20, 581, 291))
        self.tv.setText("")
        self.tv.setObjectName("tv")
        self.widget = QtWidgets.QWidget(ExceptionDialog)
        self.widget.setGeometry(QtCore.QRect(30, 340, 581, 42))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnMail = QtWidgets.QPushButton(self.widget)
        self.btnMail.setMinimumSize(QtCore.QSize(160, 40))
        self.btnMail.setObjectName("btnMail")
        self.horizontalLayout.addWidget(self.btnMail)
        self.btnIssue = QtWidgets.QPushButton(self.widget)
        self.btnIssue.setMinimumSize(QtCore.QSize(160, 40))
        self.btnIssue.setObjectName("btnIssue")
        self.horizontalLayout.addWidget(self.btnIssue)
        self.btnCancel = QtWidgets.QPushButton(self.widget)
        self.btnCancel.setMinimumSize(QtCore.QSize(160, 40))
        self.btnCancel.setObjectName("btnCancel")
        self.horizontalLayout.addWidget(self.btnCancel)

        self.retranslateUi(ExceptionDialog)
        QtCore.QMetaObject.connectSlotsByName(ExceptionDialog)

    def retranslateUi(self, ExceptionDialog):
        _translate = QtCore.QCoreApplication.translate
        ExceptionDialog.setWindowTitle(_translate("ExceptionDialog", "发生异常了"))
        self.btnMail.setText(_translate("ExceptionDialog", "邮件错误给作者"))
        self.btnIssue.setText(_translate("ExceptionDialog", "提Issue"))
        self.btnCancel.setText(_translate("ExceptionDialog", "取消"))
