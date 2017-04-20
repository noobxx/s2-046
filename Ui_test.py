# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/xx/PycharmProjects/s2-046/test.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_s2046(object):
    def setupUi(self, s2046):
        s2046.setObjectName("s2046")
        s2046.resize(843, 743)
        self.label = QtWidgets.QLabel(s2046)
        self.label.setGeometry(QtCore.QRect(10, 10, 101, 31))
        self.label.setStyleSheet("font: 18pt \"Abyssinica SIL\";")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(s2046)
        self.pushButton.setGeometry(QtCore.QRect(20, 50, 81, 21))
        self.pushButton.setStyleSheet("font: 12pt \"Abyssinica SIL\";")
        self.pushButton.setObjectName("pushButton")
        self.textBrowser_2 = QtWidgets.QTextBrowser(s2046)
        self.textBrowser_2.setGeometry(QtCore.QRect(10, 120, 821, 571))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.label_2 = QtWidgets.QLabel(s2046)
        self.label_2.setGeometry(QtCore.QRect(30, 80, 101, 31))
        self.label_2.setStyleSheet("font: 18pt \"Abyssinica SIL\";")
        self.label_2.setObjectName("label_2")
        self.pushButton_2 = QtWidgets.QPushButton(s2046)
        self.pushButton_2.setGeometry(QtCore.QRect(780, 80, 61, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(s2046)
        self.pushButton_3.setGeometry(QtCore.QRect(730, 700, 97, 26))
        self.pushButton_3.setObjectName("pushButton_3")
        self.lineEdit = QtWidgets.QLineEdit(s2046)
        self.lineEdit.setGeometry(QtCore.QRect(100, 20, 711, 26))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(s2046)
        self.lineEdit_2.setGeometry(QtCore.QRect(130, 80, 641, 26))
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.retranslateUi(s2046)
        QtCore.QMetaObject.connectSlotsByName(s2046)

    def retranslateUi(self, s2046):
        _translate = QtCore.QCoreApplication.translate
        s2046.setWindowTitle(_translate("s2046", "Dialog"))
        s2046.setWhatsThis(_translate("s2046", "<html><head/><body><p><br/></p></body></html>"))
        self.label.setText(_translate("s2046", "目标url"))
        self.pushButton.setText(_translate("s2046", "获取信息"))
        self.label_2.setText(_translate("s2046", "执行命令"))
        self.pushButton_2.setText(_translate("s2046", "执行"))
        self.pushButton_3.setText(_translate("s2046", "清空信息"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    s2046 = QtWidgets.QDialog()
    ui = Ui_s2046()
    ui.setupUi(s2046)
    s2046.show()
    sys.exit(app.exec_())

