# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widgets/newGameWidget.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from functools import partial

class IntermWidget(QtWidgets.QWidget):
    def __init__(self, stage, opts, last=False,  parent=None):
        super(IntermWidget, self).__init__(parent)
        self.stage = stage
        self.opts = opts

        for i, opt in enumerate(self.opts):
            if opt.text() == self.stage.valid_answer:
                self.valid = opt.isChecked()
                opt.setObjectName("valid")

        if self.valid:
            self.parent().incScore()

        self.setupUi(self)


    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setStyleSheet("""
QRadioButton{
    font-size: 18px;
    color: rgb(206, 0, 0);
}
QRadioButton#valid{
    color: rgb(0, 177, 0);
}
#topLabel, #maskLabel, #optBox, #scoreLabel{
    background-color: rgb(230, 230, 230);
    border-style: outset;
    border-color: rgb(51, 51, 51);
    border-width: 1px;
}
#topLabel{
    background-color: %s;
}""" % ("rgb(0, 177, 0)" if self.valid else "rgba(230, 0, 0, 180)"))
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
        self.horizontalLayout.addStretch(1)
        self.verticalLayout.addLayout(self.horizontalLayout)
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

        self.buttonGroup = QtWidgets.QButtonGroup(Form)

        for i, opt in enumerate(self.opts):
            self.verticalLayout_2.addWidget(opt)
            if not opt.isChecked():
                opt.setCheckable(False)

            self.buttonGroup.addButton(opt)

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
        self.replyBtn.clicked.connect(partial(self.parent().nextStage, False))

        self.retranslate(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        

    def retranslate(self, Form):
        _translate = QtCore.QCoreApplication.translate
        
        self.maskLabel.setText(_translate("Form", "Маска: %s" % self.stage.mask))

        self.scoreLabel.setText(_translate("Form", "Счет: %s" % self.parent().getScore()))

        self.maskLabel_3.setText(_translate("Form", "Варианты ответа:"))
        
        for i, opt in enumerate(self.opts):
            if opt.text() == self.stage.valid_answer:
                opt.setText(_translate("Form", self.stage.answers[i] + "        << Верный ответ"))
            else:
                opt.setText(_translate("Form", self.stage.answers[i]))

        if self.valid:
            self.topLabel.setText(_translate("Form", "Ваш ответ - верен!"))
        else:
            self.topLabel.setText(_translate("Form", "Ваш ответ - неверен!"))

        self.replyBtn.setText(_translate("Form", "Продолжить"))

