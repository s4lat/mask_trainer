# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widgets/settingsWidget.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from functools import partial
import utils, json

class SettingsWidget(QtWidgets.QWidget):
    def __init__(self,  test, parent=None):
        super(SettingsWidget, self).__init__(parent)
        self.test = test

        self.nameText = "<html><head/><body><p align=\"center\">Максимальная длина имени маски:</p><p align=\"center\"><span style=\" font-weight:600;\">%s</span></p></body></html>"
        self.extText = "<html><head/><body><p align=\"center\">Максимальная длина расширения маски:</p><p align=\"center\"><span style=\" font-weight:600;\">%s</span></p></body></html>"
        self.starText = "<html><head/><body><p align=\"center\"><span>Максимальная длина последовательности</span></p><p align=\"center\"><span\">на месте &quot;</span><span style=\"font-weight:600;\">*</span><span>&quot;:</span></p><p align=\"center\"><span style=\" font-weight:600;\">%s</span></p></body></html>"
        self.optText = "<html><head/><body><p align=\"center\">Кол-во вариантов ответа:</p><p align=\"center\"><span style=\" font-weight:600;\">%s</span></p></body></html>"
        self.answersText = "<html><head/><body><p align=\"center\">Кол-во вопросов:</p><p align=\"center\"><span style=\" font-weight:600;\">%s</span></p></body></html>"
        self.settings = utils.readSettings()
        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setMaximumSize(QtCore.QSize(16777215, 16777215))
        Form.setStyleSheet("""
QWidget{
font-size: 18px;
}
QLabel#titleLabel{
border-style:outset;
border-width: 1px;
border-color: rgb(51, 51, 51);
border-radius: 15px;
font-size: 24px;
}""")
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")


        self.titleLabel = QtWidgets.QLabel(Form)
        self.titleLabel.setMaximumSize(QtCore.QSize(380, 64))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.titleLabel.setFont(font)
        self.titleLabel.setLineWidth(1)
        self.titleLabel.setMidLineWidth(0)
        self.titleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.titleLabel.setObjectName("titleLabel")
        self.verticalLayout.addWidget(self.titleLabel)
        #self.verticalLayout.addStretch(10)

        if self.test:
            self.answersLabel = QtWidgets.QLabel(Form)
            self.answersLabel.setMaximumSize(QtCore.QSize(380, 64))
            self.answersLabel.setAlignment(QtCore.Qt.AlignCenter)
            self.answersLabel.setObjectName("answersLabel")
            self.verticalLayout.addWidget(self.answersLabel)
            self.answersSlider = QtWidgets.QSlider(Form)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.answersSlider.sizePolicy().hasHeightForWidth())
            self.answersSlider.setSizePolicy(sizePolicy)
            self.answersSlider.setMaximumSize(QtCore.QSize(380, 17))
            self.answersSlider.setMinimum(5)
            self.answersSlider.setMaximum(100)
            self.answersSlider.setOrientation(QtCore.Qt.Horizontal)
            self.answersSlider.setObjectName("answersSlider")
            self.verticalLayout.addWidget(self.answersSlider)

        self.optLabel = QtWidgets.QLabel(Form)
        self.optLabel.setMaximumSize(QtCore.QSize(380, 64))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.optLabel.setFont(font)
        self.optLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.optLabel.setObjectName("optLabel")
        self.verticalLayout.addWidget(self.optLabel)
        self.optSlider = QtWidgets.QSlider(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.optSlider.sizePolicy().hasHeightForWidth())
        self.optSlider.setSizePolicy(sizePolicy)
        self.optSlider.setMaximumSize(QtCore.QSize(380, 17))
        self.optSlider.setMinimum(3)
        self.optSlider.setMaximum(15)
        self.optSlider.setOrientation(QtCore.Qt.Horizontal)
        self.optSlider.setObjectName("optSlider")
        self.verticalLayout.addWidget(self.optSlider)
        self.nameLabel = QtWidgets.QLabel(Form)
        self.nameLabel.setMaximumSize(QtCore.QSize(380, 64))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.nameLabel.setFont(font)
        self.nameLabel.setLineWidth(1)
        self.nameLabel.setMidLineWidth(0)
        self.nameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.nameLabel.setObjectName("nameLabel")
        self.verticalLayout.addWidget(self.nameLabel)
        self.nameSlider = QtWidgets.QSlider(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nameSlider.sizePolicy().hasHeightForWidth())
        self.nameSlider.setSizePolicy(sizePolicy)
        self.nameSlider.setMaximumSize(QtCore.QSize(380, 17))
        self.nameSlider.setMinimum(3)
        self.nameSlider.setMaximum(12)
        self.nameSlider.setOrientation(QtCore.Qt.Horizontal)
        self.nameSlider.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.nameSlider.setObjectName("nameSlider")
        self.verticalLayout.addWidget(self.nameSlider)
        self.extLabel = QtWidgets.QLabel(Form)
        self.extLabel.setMaximumSize(QtCore.QSize(380, 64))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.extLabel.setFont(font)
        self.extLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.extLabel.setObjectName("extLabel")
        self.verticalLayout.addWidget(self.extLabel)
        self.extSlider = QtWidgets.QSlider(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.extSlider.sizePolicy().hasHeightForWidth())
        self.extSlider.setSizePolicy(sizePolicy)
        self.extSlider.setMaximumSize(QtCore.QSize(380, 17))
        self.extSlider.setMinimum(3)
        self.extSlider.setMaximum(12)
        self.extSlider.setOrientation(QtCore.Qt.Horizontal)
        self.extSlider.setObjectName("extSlider")
        self.verticalLayout.addWidget(self.extSlider)
        self.starLabel = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.starLabel.sizePolicy().hasHeightForWidth())
        self.starLabel.setSizePolicy(sizePolicy)
        self.starLabel.setMaximumSize(QtCore.QSize(380, 96))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.starLabel.setFont(font)
        self.starLabel.setLineWidth(1)
        self.starLabel.setTextFormat(QtCore.Qt.AutoText)
        self.starLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.starLabel.setObjectName("starLabel")
        self.verticalLayout.addWidget(self.starLabel)
        self.starSlider = QtWidgets.QSlider(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.starSlider.sizePolicy().hasHeightForWidth())
        self.starSlider.setSizePolicy(sizePolicy)
        self.starSlider.setMaximumSize(QtCore.QSize(380, 17))
        self.starSlider.setMinimum(3)
        self.starSlider.setMaximum(6)
        self.starSlider.setOrientation(QtCore.Qt.Horizontal)
        self.starSlider.setObjectName("starSlider")
        self.verticalLayout.addWidget(self.starSlider)

        self.applyBtn = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.applyBtn.sizePolicy().hasHeightForWidth())
        self.applyBtn.setSizePolicy(sizePolicy)
        self.applyBtn.setMaximumSize(QtCore.QSize(380, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.applyBtn.setFont(font)
        self.applyBtn.setObjectName("applyBtn")
        self.verticalLayout.addWidget(self.applyBtn)
        self.backBtn = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.backBtn.sizePolicy().hasHeightForWidth())
        self.backBtn.setSizePolicy(sizePolicy)
        self.backBtn.setMaximumSize(QtCore.QSize(380, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.backBtn.setFont(font)
        self.backBtn.setObjectName("backBtn")
        self.verticalLayout.addWidget(self.backBtn)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.nameSlider.setValue(self.settings["MAX_NAME_LEN"])
        self.extSlider.setValue(self.settings["MAX_EXT_LEN"])
        self.starSlider.setValue(self.settings["MAX_STAR_LEN"])
        self.optSlider.setValue(self.settings["ANSWER_OPTS"])

        if self.test:
            self.answersSlider.setValue(self.settings["ANSWERS_COUNT"])


        self.nameSlider.valueChanged.connect(partial(self.updateValue, self.nameLabel, self.nameText, self.nameSlider))
        self.extSlider.valueChanged.connect(partial(self.updateValue, self.extLabel, self.extText, self.extSlider))
        self.starSlider.valueChanged.connect(partial(self.updateValue, self.starLabel, self.starText, self.starSlider))
        self.optSlider.valueChanged.connect(partial(self.updateValue, self.optLabel, self.optText, self.optSlider))
        
        if self.test:
            self.answersSlider.valueChanged.connect(partial(self.updateValue, self.answersLabel, self.answersText, self.answersSlider))
        
        self.applyBtn.clicked.connect(self.applySettings)
        self.backBtn.clicked.connect(self.parent().backToMenu)
        ##########################My changes
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.nameLabel.setText(_translate("Form", self.nameText % self.settings["MAX_NAME_LEN"]))
        self.extLabel.setText(_translate("Form", self.extText % self.settings["MAX_EXT_LEN"]))
        self.starLabel.setText(_translate("Form", self.starText % self.settings["MAX_STAR_LEN"]))
        self.optLabel.setText(_translate("Form", self.optText % self.settings["ANSWER_OPTS"]))
        self.titleLabel.setText(_translate("Form", "<html><head/><body><p style=\" font-weight:600;\" align=\"center\">Настройки</p></body></html>"))
        
        if self.test:
            self.answersLabel.setText(_translate("Form", self.answersText % self.settings["ANSWERS_COUNT"]))

        self.applyBtn.setText(_translate("Form", "Готово"))
        self.backBtn.setText(_translate("Form", "Вернуться в меню"))

    def applySettings(self):
        sets = {"MAX_NAME_LEN" : self.nameSlider.value(),
                "MAX_EXT_LEN" : self.extSlider.value(),
                "MAX_STAR_LEN" : self.starSlider.value(),
                "ANSWER_OPTS" : self.optSlider.value(),
                "ANSWERS_COUNT" : self.answersSlider.value() if self.test else 10}

        utils.writeSettings(sets)
        self.parent().stageGenerator = utils.StageGenerator(utils.readSettings())

        self.parent().newGame(self.test)


    def updateValue(self, label, text, slider):
        _translate = QtCore.QCoreApplication.translate
        label.setText(_translate("Form", text % slider.value()))
        pass


