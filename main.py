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
from functools import partial

class MainWindow(QMainWindow):
	def __init__(self):
		super(MainWindow, self).__init__()
		self.central_widget = QStackedWidget()
		self.stageGenerator = utils.StageGenerator(utils.readSettings())
		self.setCentralWidget(self.central_widget)

		self.menu_widget = MenuWidget(self)
		self.central_widget.addWidget(self.menu_widget)
		self.central_widget.backToMenu = self.backToMenu
		self.central_widget.stageGenerator = self.stageGenerator
		self.central_widget.settingsToTrain = self.settingsToTrain
		self.central_widget.settingsToTest = self.settingsToTest

		self.menu_widget.trainModeBtn.clicked.connect(partial(self.menuToSettings, test=False))
		self.menu_widget.testModeBtn.clicked.connect(partial(self.menuToSettings, test=True))
		self.menu_widget.helpBtn.clicked.connect(self.showHelpDialog)
		self.menu_widget.exitBtn.clicked.connect(self.close)

		self.helpShortcut = QShortcut(QKeySequence("f1"), self)
		self.helpShortcut.activated.connect(self.showHelpDialog)
		
		self.setGeometry(0, 0, 605, 506)

	def menuToSettings(self, test):
		settings_widget = SettingsWidget(test=test, parent=self)
		self.central_widget.addWidget(settings_widget)
		self.central_widget.setCurrentWidget(settings_widget)

	def settingsToTrain(self):
		self.score = 0
		stage = utils.Stage(self.central_widget.stageGenerator)
		game_widget = GameWidget(stage=stage, test=False, parent=self)
		self.central_widget.addWidget(game_widget)
		self.central_widget.setCurrentWidget(game_widget)

	def settingsToTest(self):
		self.question = 1
		self.stages = []
		self.total_questions = utils.readSettings()["ANSWERS_COUNT"]
		stage = utils.Stage(self.central_widget.stageGenerator)
		game_widget = GameWidget(stage=stage, test=True, parent=self)
		self.central_widget.addWidget(game_widget)
		self.central_widget.setCurrentWidget(game_widget)

	def testToTest(self, stage, checkboxes):
		self.question += 1
		self.stages.append([stage, checkboxes])
		stage = utils.Stage(self.central_widget.stageGenerator)
		game_widget = GameWidget(stage=stage, test=True, last=(self.question==self.total_questions), parent=self)
		self.central_widget.addWidget(game_widget)
		self.central_widget.setCurrentWidget(game_widget)

	def testToConclusion(self, stage, checkboxes):
		self.stages.append([stage, checkboxes])
		print(self.stages) ##Do conclusion draw


	def trainToInterm(self, stage, checkboxes):
		valid = False
		for checkbox in checkboxes:
			if checkbox.isChecked() and checkbox.text() == stage.valid_answer:
				self.score += 1
				valid = True

		interm_widget = IntermWidget(stage, checkboxes, valid, parent=self)		
		self.central_widget.addWidget(interm_widget)
		self.central_widget.setCurrentWidget(interm_widget)

	def intermToTrain(self):
		stage = utils.Stage(self.central_widget.stageGenerator)
		game_widget = GameWidget(stage=stage, test=False, parent=self)
		self.central_widget.addWidget(game_widget)
		self.central_widget.setCurrentWidget(game_widget)

	@pyqtSlot()
	def showHelpDialog(self):
		helpDialog = HelpDialog(self)
		helpDialog.show()


	def backToMenu(self):
		self.central_widget.setCurrentWidget(self.menu_widget)






