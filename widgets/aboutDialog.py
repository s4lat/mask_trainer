# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widgets/aboutDialog.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class AboutDialog(QtWidgets.QDialog):
    def __init__(self, parent = None):
        super(AboutDialog, self).__init__(parent)
        self.setupUi(self)

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.label = QtWidgets.QLabel()
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
        self.gridLayout.addLayout(self.verticalLayout_2, 1, 0, 1, 1)

        self.header = QtWidgets.QLabel(Dialog)
        self.header.setObjectName("header")
        header_pixmap = QtGui.QPixmap("assets/header_nobg.png")
        header_pixmap = header_pixmap.scaled(400, 200)
        self.header.setPixmap(header_pixmap)

        self.gridLayout.addWidget(self.header, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        self.okBtn.clicked.connect(Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">MaskTrainer v1.0</span></p><p align=\"center\"><span style=\" font-size:18pt;\">Тренажер сопоставления маски и имени файла</span></p><p align=\"center\"><span style=\" font-size:18pt;\">Распространяется бесплатно</span></p><p align=\"center\"><span style=\" font-size:18pt;\">Email: zakazchikm@gmail.com</span></p><p align=\"center\"><span style=\" font-size:18pt;\">Автор программы: Заказчик М.Н</span></p><p align=\"center\"><a href=\"https://github.com/s4lat/mask_trainer\"><span style=\"font-size:18pt; text-decoration: underline; color:#0000ff;\">Репозиторий</span></a></p><p align=\"right\"><span style=\" font-family:\'AppleSDGothicNeo-Regular,lucida grande,tahoma,verdana,arial,sans-serif,AppleColorEmoji,Apple Color Emoji,Segoe UI Emoji,Segoe UI Symbol,NotoColorEmoji,EmojiSymbols,Symbola,Noto,Android Emoji,AndroidEmoji,Arial Unicode MS,Zapf Dingbats\'; font-size:12px; color:#000000;\">Copyright © 2019 Заказчик М.Н.</span></p></body></html>"))
        
        self.okBtn.setText(_translate("Dialog", "Ок"))
        


