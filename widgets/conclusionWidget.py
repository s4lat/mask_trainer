# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widgets/conclusionWidget.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class ConclusionWidget(QtWidgets.QWidget):
    def __init__(self, stages,  parent=None):
        super(ConclusionWidget, self).__init__(parent)
        self.stages = stages
        self.optText = "<p style=\"margin-left: 75px; margin-top: 0px; margin-bottom: 0px;\" align=\"justify\"><span style=\" font-size:15pt; color: %s;\"> %s </span></p>"
        self.stageText = "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:%s;\">Вопрос %s/%s - %s</span></p><p align=\"justify\"><span style=\" font-size:16pt; color:#000000;\">Маска: %s</span></p><p align=\"justify\"><span style=\" font-size:16pt; color:#000000;\">Ваш ответ: %s</span></p><p align=\"justify\"><span style=\" font-size:16pt; color:#000000;\">Верный ответ: %s</span></p><p align=\"justify\"><span style=\"font-size:14pt; color:#000000;\">Варианты ответов:</span></p>%s<hr/></body></html>"
        self.answers = []

        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setStyleSheet("""
#scrollAreaWidgetContents{
    background-color: rgb(230, 230, 230);
    border-style: outset;
    border-color: rgb(51, 51, 51);
    border-width: 1px;
}
#backBtn{
    font-size: 18px;
}""")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.scrollArea = QtWidgets.QScrollArea(Form)
        self.scrollArea.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 544, 400))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName("verticalLayout_3")

        for i, (stage, checkboxes) in enumerate(self.stages):
            label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
            label.setObjectName("label_%s" % (i+1))
            insert_vars = [i+1, len(self.stages)]

            valid = False
            opts = [checkbox.text() for checkbox in checkboxes]
            for j, checkbox in enumerate(checkboxes):
                if checkbox.isChecked() and checkbox.text() == stage.valid_answer:
                    valid = True

            self.answers.append(valid)

            insert_vars.append("Правильно" if valid else "Неправильно")
            insert_vars.insert(0, "rgb(0, 177, 0)" if valid else "rgb(206, 0, 0)")

            insert_vars.append(stage.mask)

            user_choose = [j for j, checkbox in enumerate(checkboxes) if checkbox.isChecked()][0]
            insert_vars.append(user_choose+1)

            valid_answer_ind = opts.index(stage.valid_answer)
            insert_vars.append(valid_answer_ind+1)

            for j, opt in enumerate(opts):
                if j == valid_answer_ind:
                    opts[j] = self.optText % ("rgb(0, 177, 0)", str(j+1) + ". " +  opt+"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&lt;&lt; Верный ответ")
                else:
                    opts[j] = self.optText % ("rgb(206, 0, 0)", str(j+1) + ". " + opt)

            insert_vars.append("".join(opts))

            label.setText(self.stageText % tuple(insert_vars))
            self.verticalLayout_3.addWidget(label)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.backBtn = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.backBtn.sizePolicy().hasHeightForWidth())
        self.backBtn.setMinimumSize(QtCore.QSize(0, 48))
        self.backBtn.setSizePolicy(sizePolicy)
        self.backBtn.setMaximumSize(QtCore.QSize(250, 75))
        self.backBtn.setObjectName("backBtn")
        self.verticalLayout.addWidget(self.backBtn)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.backBtn.clicked.connect(self.parent().backToMenu)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        
        qualityK = self.answers.count(True)/len(self.stages)*100
        mark = 5 if qualityK > 85 else 4 if qualityK > 65 else 3 if qualityK > 35 else 2
        valid_answers = self.answers.count(True)
        invalid_answers = self.answers.count(False)

        self.label.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600;\">Итог:</span></p><p align=\"center\"><span style=\" font-size:18pt;\">Качество выполнения: </span><span style=\" font-size:18pt; font-weight:600;\">%0.1f%s (%s)</span></p><p align=\"center\"><span style=\" font-size:18pt;\">Кол-во </span><span style=\" font-size:18pt; color:#00b100;\">верных</span><span style=\" font-size:18pt;\"> ответов: </span><span style=\" font-size:18pt; font-weight:600;\">%s</span></p><p align=\"center\"><span style=\" font-size:18pt;\">Кол-во </span><span style=\" font-size:18pt; color:#ce0000;\">неверных</span><span style=\" font-size:18pt;\"> ответов: </span><span style=\" font-size:18pt; font-weight:600;\">%s</span></p></body></html>"
            % (qualityK, "%", mark, valid_answers, invalid_answers)))
    
        self.backBtn.setText(_translate("Form", "Вернуться в меню"))


