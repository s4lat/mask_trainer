# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widgets/gameWidget.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from utils import *

class GameWidget(QtWidgets.QWidget):
    def __init__(self, stage, parent=None):
        super(GameWidget, self).__init__(parent)
        self.stage = stage
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
        self.replyBtn.clicked.connect(self.reply)
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

        #########################My changes
        font = QtGui.QFont()
        font.setPointSize(14)
        self.checkBoxes = []
        self.buttonGroup = QtWidgets.QButtonGroup(Form)

        for i, answers in enumerate(self.stage.answers):
            checkBox = QtWidgets.QCheckBox(self.groupBox)
            checkBox.setMaximumSize(QtCore.QSize(256, 25))
            checkBox.setFont(font)
            checkBox.setStyleSheet("border-width: 0px;")
            checkBox.setObjectName("checkBox_%s" % i)
            self.buttonGroup.addButton(checkBox)
            self.verticalLayout.addWidget(checkBox)
            self.checkBoxes.append(checkBox)

        #########################My changes

        self.horizontalLayout_2.addWidget(self.groupBox)
        self.gridLayout.addLayout(self.horizontalLayout_2, 5, 0, 1, 3)
        

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        #########################My changes
        self.label.setText(_translate("Form", "Выберите подходящее под маску имя файла"))
        self.maskLabel.setText(_translate("Form", "Маска: %s" % self.stage.mask))
        self.replyBtn.setText(_translate("Form", "Ответить"))
        self.backBtn.setText(_translate("Form", "Вернуться в меню"))

        
        for i, checkBox in enumerate(self.checkBoxes):
            checkBox.setText(_translate("Form", self.stage.answers[i]))
        #########################My changes

    def reply(self):
        self.parent().backToMenu()




