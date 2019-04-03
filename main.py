import sys, utils
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import random as rand

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.central_widget = QStackedWidget()
		self.setCentralWidget(self.central_widget)

		self.menu_widget = MenuWidget(self)
		self.central_widget.addWidget(self.menu_widget)
		self.menu_widget.exitBtn.clicked.connect(self.close)
		self.menu_widget.playBtn.clicked.connect(self.Play)

	def Play(self):
		game_widget = GameWidget(self)
		self.central_widget.addWidget(game_widget)
		self.central_widget.setCurrentWidget(game_widget)
		game_widget.backBtn.clicked.connect(self.backToMenu)

	def backToMenu(self):
		self.central_widget.setCurrentWidget(self.menu_widget)
		

class MenuWidget(QWidget):
	def __init__(self, parent=None):
		super(MenuWidget, self).__init__(parent)

		self.playBtn = QPushButton("Начать")
		self.settingsBtn = QPushButton("Настройки")
		self.exitBtn = QPushButton("Выход")

		self.layout = QVBoxLayout()
		self.layout.addWidget(self.playBtn)
		self.layout.addWidget(self.settingsBtn)
		self.layout.addWidget(self.exitBtn)
		self.setLayout(self.layout)

class GameWidget(QWidget):
	def __init__(self, parent=None):
		super().__init__()

		self.backBtn = QPushButton("Вернуться")

		self.replyBtn = QPushButton("Ответить")
		self.replyBtn.clicked.connect(self.Reply)

		self.layout = QVBoxLayout()

		self.stage = Stage()

		hbox = QHBoxLayout()
		hbox.addWidget(QLabel("Выберите имя файла подходящее под маску"))
		self.layout.addLayout(hbox)

		hbox = QHBoxLayout()
		hbox.addWidget(QLabel("Маска: " + self.stage.mask))
		self.layout.addLayout(hbox)

		hbox = QHBoxLayout()
		hbox.addWidget(QLabel("Варианты ответов:"))
		self.layout.addLayout(hbox)

		answ_options = QButtonGroup()
		for i, answ in enumerate(self.stage.answers):
			hbox = QHBoxLayout()
			opt = QCheckBox(answ)
			answ_options.addButton(opt)
			hbox.addWidget(opt)
			self.layout.addLayout(hbox)


		hbox = QHBoxLayout()
		hbox.addWidget(self.backBtn)
		hbox.addWidget(self.replyBtn)
		self.layout.addLayout(hbox)

		self.setLayout(self.layout)

	def Reply(self):
		pass

class Stage:
	def __init__(self):
		self.mask = utils.generate_mask()
		self.answers = [utils.get_invalid_txt_by_mask(self.mask) for i in range(3)]
		self.valid_answer = utils.get_valid_txt_by_mask(self.mask)
		self.answers.append(self.valid_answer)
		rand.shuffle(self.answers)






