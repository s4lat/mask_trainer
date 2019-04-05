import sys, utils
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import random as rand
from widgets.gameWidget import GameWidget
from widgets.menuWidget import MenuWidget

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.central_widget = QStackedWidget()
		self.setCentralWidget(self.central_widget)

		self.menu_widget = MenuWidget(self)
		self.central_widget.addWidget(self.menu_widget)
		self.menu_widget.exitBtn.clicked.connect(self.close)
		self.menu_widget.playBtn.clicked.connect(self.Play)
		self.setGeometry(0, 0, 605, 506)

	def Play(self):
		game_widget = GameWidget(self)
		self.central_widget.addWidget(game_widget)
		self.central_widget.setCurrentWidget(game_widget)
		game_widget.backBtn.clicked.connect(self.backToMenu)

	def backToMenu(self):
		self.central_widget.setCurrentWidget(self.menu_widget)
		
class Stage:
	def __init__(self):
		self.mask = utils.generate_mask()
		self.answers = [utils.get_invalid_txt_by_mask(self.mask) for i in range(3)]
		self.valid_answer = utils.get_valid_txt_by_mask(self.mask)
		self.answers.append(self.valid_answer)
		rand.shuffle(self.answers)






