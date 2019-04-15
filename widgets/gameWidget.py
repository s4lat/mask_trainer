# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widgets/newGameWidget.ui'
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
        Form.setStyleSheet("""
QRadioButton{
    font-size: 16px;
}
#topLabel, #maskLabel, #scoreLabel, #optBox{
    background-color: rgb(230, 230, 230);
    border-style: outset;
    border-color: rgb(51, 51, 51);
    border-width: 1px;
}""")
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.backBtn = QtWidgets.QPushButton(Form)
        self.backBtn.setMinimumSize(QtCore.QSize(64, 64))
        self.backBtn.setMaximumSize(QtCore.QSize(64, 64))
        self.backBtn.setIconSize(QtCore.QSize(44, 44))
        self.backBtn.setIcon(QtGui.QIcon("assets/backBtn.png"))
        self.backBtn.setObjectName("backBtn")


        self.horizontalLayout_4.addWidget(self.backBtn)
        self.topLabel = QtWidgets.QLabel(Form)
        self.topLabel.setMinimumSize(QtCore.QSize(400, 64))
        self.topLabel.setMaximumSize(QtCore.QSize(16777215, 64))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.topLabel.setFont(font)
        self.topLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.topLabel.setObjectName("topLabel")
        self.horizontalLayout_4.addWidget(self.topLabel)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.addStretch(1)
        self.maskLabel = QtWidgets.QLabel(Form)
        self.maskLabel.setMinimumSize(QtCore.QSize(256, 32))
        self.maskLabel.setMaximumSize(QtCore.QSize(16777215, 32))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.maskLabel.setFont(font)
        self.maskLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.maskLabel.setObjectName("maskLabel")
        self.horizontalLayout.addWidget(self.maskLabel)
        self.horizontalLayout.addStretch(1)
        self.scoreLabel = QtWidgets.QLabel(Form)
        self.scoreLabel.setMinimumSize(QtCore.QSize(256, 32))
        self.scoreLabel.setMaximumSize(QtCore.QSize(16777215, 32))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.scoreLabel.setFont(font)
        self.scoreLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.scoreLabel.setObjectName("scoreLabel")
        self.horizontalLayout.addWidget(self.scoreLabel)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout.addStretch(1)
        self.maskLabel_3 = QtWidgets.QLabel(Form)
        self.maskLabel_3.setMaximumSize(QtCore.QSize(16777215, 32))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.maskLabel_3.setFont(font)
        self.maskLabel_3.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.maskLabel_3.setObjectName("maskLabel_3")
        self.verticalLayout.addWidget(self.maskLabel_3)

        self.optBox = QtWidgets.QFrame(Form)
        self.optBox.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.optBox.setFrameShadow(QtWidgets.QFrame.Raised)
        self.optBox.setObjectName("optBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.optBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.opts = []
        self.buttonGroup = QtWidgets.QButtonGroup(Form)
        for i, answ in enumerate(self.stage.answers):
            opt = QtWidgets.QRadioButton(self.optBox)
            opt.setObjectName("opt_%s" % i)
            self.verticalLayout_2.addWidget(opt)
            self.buttonGroup.addButton(opt)
            self.opts.append(opt)

        self.verticalLayout.addWidget(self.optBox)

        self.replyBtn = QtWidgets.QPushButton(Form)
        self.replyBtn.setMinimumSize(QtCore.QSize(0, 48))
        font = QtGui.QFont()
        font.setPointSize(16)

        self.replyBtn.setFont(font)
        self.replyBtn.setObjectName("replyBtn")
        self.verticalLayout.addWidget(self.replyBtn)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.backBtn.clicked.connect(self.parent().backToMenu)
        self.replyBtn.clicked.connect(self.reply)

        self.retranslate(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)


    def reply(self):
        checked = False

        for opt in self.opts:
            if opt.isChecked():
                checked = True

        if not checked:
            return

        if self.test and not self.last:
            return self.parent().nextStage(self.test, stage=self.stage, opts=self.opts)
        
        return self.parent().conclusionWidget(self.test, stage=self.stage, opts=self.opts)

    def retranslate(self, Form):
        _translate = QtCore.QCoreApplication.translate
        self.topLabel.setText(_translate("Form", "Выберите подходящее под маску имя файла"))
        self.maskLabel.setText(_translate("Form", "Маска: %s" % self.stage.mask))

        if self.test:
            self.scoreLabel.setText(_translate("Form", "Вопрос: %s/%s" % (self.parent().question, 
                                        self.parent().total_questions)))
        else:
            self.scoreLabel.setText(_translate("Form", "Счет: %s" % self.parent().getScore()))

        self.maskLabel_3.setText(_translate("Form", "Варианты ответа:"))
        
        for i, opt in enumerate(self.opts):
            opt.setText(_translate("Form", self.stage.answers[i]))

        self.replyBtn.setText(_translate("Form", "Ответить"))

