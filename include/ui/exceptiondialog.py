import webbrowser

from PyQt5.QtWidgets import QDialog

from include.const import Const
from include.ui.exception_dialog import Ui_ExceptionDialog


class ExceptionDialog:
    def __init__(self, exception: Exception):
        self.exception = exception
        self.dialog = QDialog()
        self.exceptionDialog = Ui_ExceptionDialog()
        self.exceptionDialog.setupUi(self.dialog)
        self.exceptionDialog.btnMail.clicked.connect(self.performMail)
        self.exceptionDialog.btnIssue.clicked.connect(self.performIssue)
        self.exceptionDialog.btnCancel.clicked.connect(self.close)
        self.exceptionDialog.tv.setText(str(type(exception)) + "\n" + str(exception))
        pass

    def show(self):
        self.dialog.exec_()
        pass

    def performMail(self):
        webbrowser.open(Const.MAIL.format(str(self.exception)))
        pass

    def close(self):
        self.dialog.close()
        pass

    def performIssue(self):
        webbrowser.open(Const.ISSUE)
        self.close()
        pass
