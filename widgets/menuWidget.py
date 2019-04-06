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
        Form.setMaximumSize(QtCore.QSize(9999999, 9999999))
        self.hbox = QtWidgets.QHBoxLayout(Form)
        self.vbox = QtWidgets.QVBoxLayout()
        self.hbox.addLayout(self.vbox)
        self.vbox.setObjectName("vbox")
        Form.setStyleSheet("""
QPushButton{
border-width: 2px;
border-color: blue;
border-radius: 32px;
border-style: outset;
font-size: 24px;
}
QPushButton::hover{
border-color: red;
}
""")
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
