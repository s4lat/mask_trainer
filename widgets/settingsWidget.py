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
    def __init__(self,  parent=None):
        super(SettingsWidget, self).__init__(parent)

        self.nameText = "<html><head/><body><p align=\"center\">Макс. длина имени маски:</p><p align=\"center\"><span style=\" font-weight:600;\">%s</span></p></body></html>"
        self.extText = "<html><head/><body><p align=\"center\">Макс. длина расширения маски:</p><p align=\"center\"><span style=\" font-weight:600;\">%s</span></p></body></html>"
        self.starText = "<html><head/><body><p align=\"center\"><span>Макс. длина последовательности</span></p><p align=\"center\"><span\">на месте &quot;</span><span style=\"font-weight:600;\">*</span><span>&quot;:</span></p><p align=\"center\"><span style=\" font-weight:600;\">%s</span></p></body></html>"
        self.optText = "<html><head/><body><p align=\"center\">Кол-во вариантов ответа:</p><p align=\"center\"><span style=\" font-weight:600;\">%s</span></p></body></html>"
        self.settings = utils.readSettings()
        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(605, 506)
        Form.setMaximumSize(QtCore.QSize(864, 608))
        Form.setStyleSheet("\n"
"QPushButton{\n"
"border-width: 2px;\n"
"border-color: blue;\n"
"border-radius: 24px;\n"
"border-style: outset;\n"
"}\n"
"QPushButton::hover{\n"
"border-color: red;\n"
"}\n"
"")
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.nameLabel = QtWidgets.QLabel(Form)
        self.nameLabel.setMaximumSize(QtCore.QSize(312, 64))
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
        self.nameSlider.setMaximumSize(QtCore.QSize(312, 17))
        self.nameSlider.setMinimum(3)
        self.nameSlider.setMaximum(15)
        self.nameSlider.setOrientation(QtCore.Qt.Horizontal)
        self.nameSlider.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.nameSlider.setObjectName("nameSlider")
        self.verticalLayout.addWidget(self.nameSlider)
        self.extLabel = QtWidgets.QLabel(Form)
        self.extLabel.setMaximumSize(QtCore.QSize(312, 64))
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
        self.extSlider.setMaximumSize(QtCore.QSize(312, 17))
        self.extSlider.setMinimum(3)
        self.extSlider.setMaximum(15)
        self.extSlider.setOrientation(QtCore.Qt.Horizontal)
        self.extSlider.setObjectName("extSlider")
        self.verticalLayout.addWidget(self.extSlider)
        self.starLabel = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.starLabel.sizePolicy().hasHeightForWidth())
        self.starLabel.setSizePolicy(sizePolicy)
        self.starLabel.setMaximumSize(QtCore.QSize(312, 96))
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
        self.starSlider.setMaximumSize(QtCore.QSize(312, 17))
        self.starSlider.setMinimum(3)
        self.starSlider.setMaximum(15)
        self.starSlider.setOrientation(QtCore.Qt.Horizontal)
        self.starSlider.setObjectName("starSlider")
        self.verticalLayout.addWidget(self.starSlider)
        self.optLabel = QtWidgets.QLabel(Form)
        self.optLabel.setMaximumSize(QtCore.QSize(312, 64))
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
        self.optSlider.setMaximumSize(QtCore.QSize(312, 17))
        self.optSlider.setMinimum(3)
        self.optSlider.setMaximum(15)
        self.optSlider.setOrientation(QtCore.Qt.Horizontal)
        self.optSlider.setObjectName("optSlider")
        self.verticalLayout.addWidget(self.optSlider)
        self.applyBtn = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.applyBtn.sizePolicy().hasHeightForWidth())
        self.applyBtn.setSizePolicy(sizePolicy)
        self.applyBtn.setMaximumSize(QtCore.QSize(312, 50))
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
        self.backBtn.setMaximumSize(QtCore.QSize(312, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.backBtn.setFont(font)
        self.backBtn.setObjectName("backBtn")
        self.verticalLayout.addWidget(self.backBtn)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)


        ##########################My changes
        self.nameSlider.setValue(self.settings["MAX_NAME_LEN"])
        self.extSlider.setValue(self.settings["MAX_EXT_LEN"])
        self.starSlider.setValue(self.settings["MAX_STAR_LEN"])
        self.optSlider.setValue(self.settings["ANSWER_OPTS"])


        self.nameSlider.valueChanged.connect(partial(self.updateValue, self.nameLabel, self.nameText, self.nameSlider))
        self.extSlider.valueChanged.connect(partial(self.updateValue, self.extLabel, self.extText, self.extSlider))
        self.starSlider.valueChanged.connect(partial(self.updateValue, self.starLabel, self.starText, self.starSlider))
        self.optSlider.valueChanged.connect(partial(self.updateValue, self.optLabel, self.optText, self.optSlider))

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
        self.applyBtn.setText(_translate("Form", "Применить"))
        self.backBtn.setText(_translate("Form", "Вернуться в меню"))

    def applySettings(self):
        sets = {"MAX_NAME_LEN" : self.nameSlider.value(),
                "MAX_EXT_LEN" : self.extSlider.value(),
                "MAX_STAR_LEN" : self.starSlider.value(),
                "ANSWER_OPTS" : self.optSlider.value()}

        utils.writeSettings(sets)
        self.parent().stageGenerator = utils.StageGenerator(utils.readSettings())


    def updateValue(self, label, text, slider):
        _translate = QtCore.QCoreApplication.translate
        label.setText(_translate("Form", text % slider.value()))
        pass


