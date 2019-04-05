# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widgets/gameWidget.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class GameWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(GameWidget, self).__init__(parent)

        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(532, 340)
        Form.setMaximumSize(QtCore.QSize(864, 608))
        Form.setStyleSheet("alternate-background-color: rgb(255, 0, 0);")
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setMaximumSize(QtCore.QSize(512, 32))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(225, 225, 225);\n"
"border-style: outset;\n"
"border-color: rgb(100, 100, 100);\n"
"border-width: 1px;\n"
"border-radius: 3px;\n"
"")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 3)
        self.maskLabel = QtWidgets.QLabel(Form)
        self.maskLabel.setMaximumSize(QtCore.QSize(256, 25))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.maskLabel.setFont(font)
        self.maskLabel.setStyleSheet("background-color: rgb(190, 255, 200);\n"
"\n"
"border-color: rgb(100, 100, 100);\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 3px;\n"
"")
        self.maskLabel.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.maskLabel.setScaledContents(False)
        self.maskLabel.setObjectName("maskLabel")
        self.gridLayout.addWidget(self.maskLabel, 3, 0, 1, 1)
        self.replyBtn = QtWidgets.QPushButton(Form)
        self.replyBtn.setMaximumSize(QtCore.QSize(300, 75))
        self.replyBtn.setStyleSheet("")
        self.replyBtn.setObjectName("replyBtn")
        self.gridLayout.addWidget(self.replyBtn, 13, 2, 1, 1)
        self.backBtn = QtWidgets.QPushButton(Form)
        self.backBtn.setMaximumSize(QtCore.QSize(300, 45))
        self.backBtn.setStyleSheet("")
        self.backBtn.setObjectName("backBtn")
        self.gridLayout.addWidget(self.backBtn, 13, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setStyleSheet("background-color: rgb(255, 248, 186);\n"
"border-color: rgb(100, 100, 100);\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 3px;\n"
"")
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setContentsMargins(23, 1, -1, 1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.checkBox_4 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_4.setMaximumSize(QtCore.QSize(256, 25))
        self.checkBox_4.setStyleSheet("border-width: 0px;")
        self.checkBox_4.setTristate(False)
        self.checkBox_4.setObjectName("checkBox_4")
        self.verticalLayout.addWidget(self.checkBox_4)
        self.checkBox_3 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_3.setMaximumSize(QtCore.QSize(256, 25))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.checkBox_3.setFont(font)
        self.checkBox_3.setStyleSheet("border-width: 0px;")
        self.checkBox_3.setObjectName("checkBox_3")
        self.verticalLayout.addWidget(self.checkBox_3)
        self.checkBox_2 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_2.setMaximumSize(QtCore.QSize(256, 25))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setStyleSheet("border-width: 0px;")
        self.checkBox_2.setObjectName("checkBox_2")
        self.verticalLayout.addWidget(self.checkBox_2)
        self.checkBox = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox.setMaximumSize(QtCore.QSize(256, 25))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.checkBox.setFont(font)
        self.checkBox.setStyleSheet("border-width: 0px;")
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout.addWidget(self.checkBox)
        self.horizontalLayout_2.addWidget(self.groupBox)
        self.gridLayout.addLayout(self.horizontalLayout_2, 5, 0, 1, 3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Выберите подходящее под маску имя файла"))
        self.maskLabel.setText(_translate("Form", "Маска: "))
        self.replyBtn.setText(_translate("Form", "Ответить"))
        self.backBtn.setText(_translate("Form", "Вернуться в меню"))
        self.checkBox_4.setText(_translate("Form", "CheckBox"))
        self.checkBox_3.setText(_translate("Form", "CheckBox"))
        self.checkBox_2.setText(_translate("Form", "CheckBox"))
        self.checkBox.setText(_translate("Form", "CheckBox"))


