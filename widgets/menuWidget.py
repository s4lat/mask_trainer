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
        self.trainModeBtn = QtWidgets.QPushButton(Form)
        self.trainModeBtn.setMaximumSize(QtCore.QSize(250, 75))
        self.trainModeBtn.setObjectName("trainModeBtn")
        self.vbox.addWidget(self.trainModeBtn)
        self.testModeBtn = QtWidgets.QPushButton(Form)
        self.testModeBtn.setMaximumSize(QtCore.QSize(250, 75))
        self.testModeBtn.setObjectName("testModeBtn")
        self.vbox.addWidget(self.testModeBtn)
        self.helpBtn = QtWidgets.QPushButton(Form)
        self.helpBtn.setMaximumSize(QtCore.QSize(250, 75))
        self.helpBtn.setObjectName("helpBtn")
        self.vbox.addWidget(self.helpBtn)
        self.exitBtn = QtWidgets.QPushButton(Form)
        self.exitBtn.setMaximumSize(QtCore.QSize(250, 75))
        self.exitBtn.setObjectName("exitBtn")
        self.vbox.addWidget(self.exitBtn)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.trainModeBtn.setText(_translate("Form", "Обучение"))
        self.testModeBtn.setText(_translate("Form", "Тест"))
        self.helpBtn.setText(_translate("Form", "Теория"))
        self.exitBtn.setText(_translate("Form", "Выход"))
