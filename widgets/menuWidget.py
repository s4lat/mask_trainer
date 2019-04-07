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
        Form.resize(605, 506)
        Form.setMaximumSize(QtCore.QSize(16777215, 16777215))

        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.hbox = QtWidgets.QHBoxLayout()
        self.vbox = QtWidgets.QVBoxLayout()
        self.hbox.addLayout(self.vbox)
        self.vbox.setObjectName("vbox")
        self.gridLayout.addLayout(self.hbox, 0, 0, 1, 1)
        Form.setStyleSheet("""
QWidget{
font-size: 18px;
}""")
        self.playBtn = QtWidgets.QPushButton(Form)
        self.playBtn.setMaximumSize(QtCore.QSize(250, 75))
        self.playBtn.setObjectName("playBtn")
        self.vbox.addWidget(self.playBtn)
        self.settingsBtn = QtWidgets.QPushButton(Form)
        self.settingsBtn.setMaximumSize(QtCore.QSize(250, 75))
        self.settingsBtn.setObjectName("settingsBtn")
        self.vbox.addWidget(self.settingsBtn)
        self.exitBtn = QtWidgets.QPushButton(Form)
        self.exitBtn.setMaximumSize(QtCore.QSize(250, 75))
        self.exitBtn.setObjectName("exitBtn")
        self.vbox.addWidget(self.exitBtn)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.playBtn.setText(_translate("Form", "Начать"))
        self.settingsBtn.setText(_translate("Form", "Настройки"))
        self.exitBtn.setText(_translate("Form", "Выход"))
