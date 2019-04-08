from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import random as rand
from widgets.gameWidget import GameWidget
from widgets.menuWidget import MenuWidget
from widgets.intermWidget import IntermWidget
from widgets.settingsWidget import SettingsWidget
from widgets.helpDialog import HelpDialog
import sys, utils

class MainWindow(QMainWindow):
	def __init__(self):
		super(MainWindow, self).__init__()
		self.central_widget = QStackedWidget()
		self.stageGenerator = utils.StageGenerator(utils.readSettings())
		self.setCentralWidget(self.central_widget)

		self.menu_widget = MenuWidget(self)
		self.central_widget.addWidget(self.menu_widget)
		self.central_widget.backToMenu = self.backToMenu
		self.central_widget.gameToInterm = self.gameToInterm
		self.central_widget.intermToGame = self.intermToGame
		self.central_widget.stageGenerator = self.stageGenerator


		self.menu_widget.playBtn.clicked.connect(self.menuToGame)
		self.menu_widget.settingsBtn.clicked.connect(self.menuToSettings)
		self.menu_widget.helpBtn.clicked.connect(self.showHelpDialog)
		self.menu_widget.exitBtn.clicked.connect(self.close)

		self.helpShortcut = QShortcut(QKeySequence("f1"), self)
		self.helpShortcut.activated.connect(self.showHelpDialog)
		
		self.setGeometry(0, 0, 605, 506)

	def menuToSettings(self):
		settings_widget = SettingsWidget(self)
		self.central_widget.addWidget(settings_widget)
		self.central_widget.setCurrentWidget(settings_widget)

	def menuToGame(self):
		self.score = 0
		stage = utils.Stage(self.central_widget.stageGenerator)
		game_widget = GameWidget(stage=stage, parent=self)
		self.central_widget.addWidget(game_widget)
		self.central_widget.setCurrentWidget(game_widget)

	def gameToInterm(self, stage, checkboxes):
		valid = False
		for checkbox in checkboxes:
			if checkbox.isChecked() and checkbox.text() == stage.valid_answer:
				self.score += 1
				valid = True

		interm_widget = IntermWidget(stage, checkboxes, valid, parent=self)		
		self.central_widget.addWidget(interm_widget)
		self.central_widget.setCurrentWidget(interm_widget)

	def intermToGame(self):
		stage = utils.Stage(self.central_widget.stageGenerator)
		game_widget = GameWidget(stage=stage, parent=self)
		self.central_widget.addWidget(game_widget)
		self.central_widget.setCurrentWidget(game_widget)

	@pyqtSlot()
	def showHelpDialog(self):
		helpDialog = HelpDialog(self)
		helpDialog.show()


	def backToMenu(self):
		self.central_widget.setCurrentWidget(self.menu_widget)






