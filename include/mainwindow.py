# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 640)
        MainWindow.setMinimumSize(QtCore.QSize(800, 640))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.etLeft = QtWidgets.QPlainTextEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.etLeft.sizePolicy().hasHeightForWidth())
        self.etLeft.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.etLeft.setFont(font)
        self.etLeft.setObjectName("etLeft")
        self.verticalLayout_2.addWidget(self.etLeft)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.btnToChinese = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnToChinese.sizePolicy().hasHeightForWidth())
        self.btnToChinese.setSizePolicy(sizePolicy)
        self.btnToChinese.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnToChinese.setFont(font)
        self.btnToChinese.setObjectName("btnToChinese")
        self.verticalLayout.addWidget(self.btnToChinese)
        self.btnToEnglish = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnToEnglish.sizePolicy().hasHeightForWidth())
        self.btnToEnglish.setSizePolicy(sizePolicy)
        self.btnToEnglish.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnToEnglish.setFont(font)
        self.btnToEnglish.setObjectName("btnToEnglish")
        self.verticalLayout.addWidget(self.btnToEnglish)
        self.btnJson = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnJson.sizePolicy().hasHeightForWidth())
        self.btnJson.setSizePolicy(sizePolicy)
        self.btnJson.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnJson.setFont(font)
        self.btnJson.setObjectName("btnJson")
        self.verticalLayout.addWidget(self.btnJson)
        self.btnUrlDecode = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnUrlDecode.sizePolicy().hasHeightForWidth())
        self.btnUrlDecode.setSizePolicy(sizePolicy)
        self.btnUrlDecode.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnUrlDecode.setFont(font)
        self.btnUrlDecode.setObjectName("btnUrlDecode")
        self.verticalLayout.addWidget(self.btnUrlDecode)
        self.btnUrlEncode = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnUrlEncode.sizePolicy().hasHeightForWidth())
        self.btnUrlEncode.setSizePolicy(sizePolicy)
        self.btnUrlEncode.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnUrlEncode.setFont(font)
        self.btnUrlEncode.setObjectName("btnUrlEncode")
        self.verticalLayout.addWidget(self.btnUrlEncode)
        self.gridLayout.addLayout(self.verticalLayout, 0, 1, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.etRight = QtWidgets.QPlainTextEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.etRight.sizePolicy().hasHeightForWidth())
        self.etRight.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.etRight.setFont(font)
        self.etRight.setObjectName("etRight")
        self.verticalLayout_3.addWidget(self.etRight)
        self.gridLayout.addLayout(self.verticalLayout_3, 0, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionGithub = QtWidgets.QAction(MainWindow)
        self.actionGithub.setObjectName("actionGithub")
        self.actionQr = QtWidgets.QAction(MainWindow)
        self.actionQr.setObjectName("actionQr")
        self.actionIssue = QtWidgets.QAction(MainWindow)
        self.actionIssue.setObjectName("actionIssue")
        self.menu_2.addAction(self.actionGithub)
        self.menu_2.addAction(self.actionIssue)
        self.menu_2.addAction(self.actionAbout)
        self.menu.addAction(self.actionQr)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnToChinese.setText(_translate("MainWindow", "翻译为中文"))
        self.btnToEnglish.setText(_translate("MainWindow", "翻译为英文"))
        self.btnJson.setText(_translate("MainWindow", "Json格式化"))
        self.btnUrlDecode.setText(_translate("MainWindow", "Url解码"))
        self.btnUrlEncode.setText(_translate("MainWindow", "Url编码"))
        self.menu_2.setTitle(_translate("MainWindow", "帮助"))
        self.menu.setTitle(_translate("MainWindow", "工具"))
        self.actionAbout.setText(_translate("MainWindow", "关于"))
        self.actionGithub.setText(_translate("MainWindow", "GitHub"))
        self.actionQr.setText(_translate("MainWindow", "二维码生成/解析"))
        self.actionIssue.setText(_translate("MainWindow", "Issue"))
