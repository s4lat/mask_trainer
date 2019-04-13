# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './widgets/menuWidget.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class MenuWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(MenuWidget, self).__init__(parent)

        self.setupUi(self);

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setMaximumSize(QtCore.QSize(16777215, 16777215))
        Form.setStyleSheet("""
QWidget#Form{
}
QWidget{
font-size: 18px;
}""")


        self.main_vbox = QtWidgets.QVBoxLayout(Form)
        self.main_vbox.addStretch(1)

        self.gridLayoutHeader = QtWidgets.QGridLayout()
        self.gridLayoutHeader.setObjectName("gridLayoutHeader")
        self.main_vbox.addLayout(self.gridLayoutHeader, QtCore.Qt.AlignVCenter)

        self.gridLayoutMenu = QtWidgets.QGridLayout()
        self.gridLayoutMenu.setObjectName("gridLayoutMenu")
        self.main_vbox.addLayout(self.gridLayoutMenu, QtCore.Qt.AlignTop)


        self.header = QtWidgets.QLabel(self)
        header_pixmap = QtGui.QPixmap("assets/header_nobg.png")
        header_pixmap = header_pixmap.scaled(400, 200)
        self.header.setPixmap(header_pixmap)
        self.header.setMaximumSize(QtCore.QSize(400, 200))
        self.header.setObjectName("header")
        self.gridLayoutHeader.addWidget(self.header, 0, 0)

        self.vbox = QtWidgets.QVBoxLayout()
        self.gridLayoutMenu.addLayout(self.vbox, 0, 0)

        self.testModeBtn = QtWidgets.QPushButton(Form)
        self.testModeBtn.setMaximumSize(QtCore.QSize(250, 75))
        self.testModeBtn.setObjectName("testModeBtn")
        self.vbox.addWidget(self.testModeBtn)
        self.trainModeBtn = QtWidgets.QPushButton(Form)
        self.trainModeBtn.setMaximumSize(QtCore.QSize(250, 75))
        self.trainModeBtn.setObjectName("trainModeBtn")
        self.vbox.addWidget(self.trainModeBtn)
        self.helpBtn = QtWidgets.QPushButton(Form)
        self.helpBtn.setMaximumSize(QtCore.QSize(250, 75))
        self.helpBtn.setObjectName("helpBtn")
        self.vbox.addWidget(self.helpBtn)
        self.aboutBtn = QtWidgets.QPushButton(Form)
        self.aboutBtn.setMaximumSize(QtCore.QSize(250, 75))
        self.aboutBtn.setObjectName("aboutBtn")
        self.vbox.addWidget(self.aboutBtn)
        self.exitBtn = QtWidgets.QPushButton(Form)
        self.exitBtn.setMaximumSize(QtCore.QSize(250, 75))
        self.exitBtn.setObjectName("exitBtn")
        self.vbox.addWidget(self.exitBtn)

        self.main_vbox.addStretch(1)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.trainModeBtn.setText(_translate("Form", "Обучение"))
        self.testModeBtn.setText(_translate("Form", "Тест"))
        self.helpBtn.setText(_translate("Form", "Теория"))
        self.aboutBtn.setText(_translate("Form", "ℹ О программе"))
        self.exitBtn.setText(_translate("Form", "Выход"))