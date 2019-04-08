# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widgets/helpDialog.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class HelpDialog(QtWidgets.QDialog):
    def __init__(self, parent = None):
        super(HelpDialog, self).__init__(parent)
        self.setupUi(self)

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(537, 271)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.okBtn = QtWidgets.QPushButton(Dialog)
        self.okBtn.setMaximumSize(QtCore.QSize(128, 16777215))
        self.okBtn.setFocusPolicy(QtCore.Qt.TabFocus)
        self.okBtn.setCheckable(False)
        self.okBtn.setAutoDefault(False)
        self.okBtn.setDefault(True)
        self.okBtn.setFlat(False)
        self.okBtn.setObjectName("okBtn")
        self.gridLayout_3.addWidget(self.okBtn, 0, 0, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_3)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        self.okBtn.clicked.connect(Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:14pt;\">Для групповых операций с файлами используются маски имен файлов. <br/>Маска представляет собой последовательность букв, цифр и прочих <br/>допустимых в именах файлов символов, в которых также могут <br/>встречаться следующие символы:</span></p><p><span style=\" font-size:14pt;\">1. Символ «</span><span style=\" font-size:14pt; font-weight:600;\">?</span><span style=\" font-size:14pt;\">» </span><span style=\" font-size:14pt; font-style:italic;\">(вопросительный знак)</span><span style=\" font-size:14pt;\"> означает ровно один произвольный <br/>символ.</span></p><p><span style=\" font-size:14pt;\">2. Символ «</span><span style=\" font-size:14pt; font-weight:600;\">*</span><span style=\" font-size:14pt;\">» </span><span style=\" font-size:14pt; font-style:italic;\">(звездочка)</span><span style=\" font-size:14pt;\"> означает любую последовательность символов <br/>произвольной длины, в том числе «*» может задавать и пустую <br/>последовательность.</span></p><p><span style=\" font-weight:600; font-style:italic;\">(Во время игры, это окно можно открыть по нажатию клавиши F1)</span></p></body></html>"))
        self.okBtn.setText(_translate("Dialog", "Ок"))


