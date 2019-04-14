# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widgets/TrainWidget.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from functools import partial

class GameWidget(QtWidgets.QWidget):
    def __init__(self, stage, test, last=False,  parent=None):
        super(GameWidget, self).__init__(parent)
        self.test = test
        self.last = last
        self.stage = stage
        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setMaximumSize(QtCore.QSize(16777215, 16777215))
        Form.move(self.parent().rect().center())
        Form.setStyleSheet("""
QWidget{
font-size: 18px;
}
QLabel{
border-width: 1px;
border-radius: 10px;
border-style: outset;
border-color: rgb(51, 51, 51);
}
QLabel#scoreLabel{
border-radius: 3px;
}
QLabel#countLabel{
border-radius: 3px;
}
QLabel#maskLabel{
border-radius: 3px;
font-size: 24px;
}""")

        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setMaximumSize(QtCore.QSize(16777215, 64))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.horizontalLayout.addWidget(self.label)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 3)
        self.maskLabel = QtWidgets.QLabel(Form)
        self.maskLabel.setMaximumSize(QtCore.QSize(512, 32))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.maskLabel.setFont(font)
        self.maskLabel.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.maskLabel.setScaledContents(False)
        self.maskLabel.setObjectName("maskLabel")
        self.gridLayout.addWidget(self.maskLabel, 3, 0, 1, 1)
        self.replyBtn = QtWidgets.QPushButton(Form)
        self.replyBtn.setMaximumSize(QtCore.QSize(300, 75))
        self.replyBtn.setObjectName("replyBtn")
        self.gridLayout.addWidget(self.replyBtn, 13, 2, 1, 1)
        self.backBtn = QtWidgets.QPushButton(Form)
        self.backBtn.setMaximumSize(QtCore.QSize(300, 45))
        self.backBtn.setObjectName("backBtn")
        self.gridLayout.addWidget(self.backBtn, 13, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setContentsMargins(23, 1, -1, 1)
        self.verticalLayout.setObjectName("verticalLayout")

        #########################My changes
        font = QtGui.QFont()
        font.setPointSize(16)
        self.checkBoxes = []
        self.buttonGroup = QtWidgets.QButtonGroup(Form)

        for i, answers in enumerate(self.stage.answers):
            checkBox = QtWidgets.QRadioButton(self.groupBox)
            checkBox.setMaximumSize(QtCore.QSize(512, 25))
            checkBox.setFont(font)
            checkBox.setStyleSheet("border-width: 0px;")
            checkBox.setObjectName("checkBox_%s" % i)
            self.buttonGroup.addButton(checkBox)
            self.verticalLayout.addWidget(checkBox)
            self.checkBoxes.append(checkBox)

        #########################My changes
        self.horizontalLayout_2.addWidget(self.groupBox)
        self.gridLayout.addLayout(self.horizontalLayout_2, 5, 0, 1, 3)

        if self.test:
            self.countLabel = QtWidgets.QLabel(Form)
            self.countLabel.setMaximumSize(QtCore.QSize(256, 25))
            font = QtGui.QFont()
            font.setPointSize(16)
            self.countLabel.setFont(font)
            self.countLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
            self.countLabel.setObjectName("countLabel")
            self.gridLayout.addWidget(self.countLabel, 3, 2, 1, 1)
        else:
            self.scoreLabel = QtWidgets.QLabel(Form)
            self.scoreLabel.setMaximumSize(QtCore.QSize(256, 25))
            font = QtGui.QFont()
            font.setPointSize(16)
            self.scoreLabel.setFont(font)
            self.scoreLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
            self.scoreLabel.setObjectName("scoreLabel")
            self.gridLayout.addWidget(self.scoreLabel, 3, 2, 1, 1)

        self.replyBtn.clicked.connect(self.reply)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.backBtn.clicked.connect(self.parent().backToMenu)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        #########################My changes
        self.label.setText(_translate("Form", "Выберите подходящее под маску имя файла"))
        
        self.replyBtn.setText(_translate("Form", "Ответить"))
        self.backBtn.setText(_translate("Form", "Вернуться в меню"))

        
        for i, checkBox in enumerate(self.checkBoxes):
            checkBox.setText(_translate("Form", self.stage.answers[i]))

        if self.test:
            self.countLabel.setText(_translate("Form", "Вопрос: %s/%s" % (self.parent().question, 
                                            self.parent().total_questions)))
        else:
            self.scoreLabel.setText(_translate("Form", "Счет: %s" % self.parent().score))
        
        self.maskLabel.setText(_translate("Form", "Маска: %s" % self.stage.mask))
        #########################My changes


    def reply(self):
        checked = False

        for checkbox in self.checkBoxes:
            if checkbox.isChecked():
                checked = True

        if not checked:
            return

        if self.test:
            if self.last:
                self.parent().testToConclusion(self.stage, self.checkBoxes)
            else:
                self.parent().testToTest(self.stage, self.checkBoxes)
        else:
            self.parent().trainToInterm(self.stage, self.checkBoxes)


