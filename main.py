from widgets.gameWidget import GameWidget
from widgets.menuWidget import MenuWidget
from widgets.intermWidget import IntermWidget
from widgets.settingsWidget import SettingsWidget
from widgets.helpDialog import HelpDialog
from widgets.conclusionWidget import ConclusionWidget
from widgets.aboutDialog import AboutDialog
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import random as rand
import sys, utils
from functools import partial

class MainWindow(QMainWindow):
	def __init__(self):
		super(MainWindow, self).__init__()
		self.central_widget = QStackedWidget()
		self.setObjectName("centralWidget")
		self.stageGenerator = utils.StageGenerator(utils.readSettings())
		self.setCentralWidget(self.central_widget)

		self.menu_widget = MenuWidget(self)
		self.central_widget.addWidget(self.menu_widget)
		self.central_widget.backToMenu = self.backToMenu
		self.central_widget.stageGenerator = self.stageGenerator
		self.central_widget.newGame = self.newGame
		self.central_widget.nextStage = self.nextStage
		self.central_widget.conclusionWidget = self.conclusionWidget
		self.central_widget.incScore = self.incScore
		self.central_widget.getScore = self.getScore

		self.menu_widget.trainModeBtn.clicked.connect(partial(self.settingsWidget, test=False))
		self.menu_widget.testModeBtn.clicked.connect(partial(self.settingsWidget, test=True))
		self.menu_widget.helpBtn.clicked.connect(self.showHelpDialog)
		self.menu_widget.aboutBtn.clicked.connect(self.showAboutDialog)
		self.menu_widget.exitBtn.clicked.connect(self.close)
		
		self.helpShortcut = QShortcut(QKeySequence("f1"), self)

		self.setWindowTitle("MaskTrainer")
		self.setWindowIcon(QIcon("assets/icon.ico"))
		self.setGeometry(0, 0, 640, 540)

	def settingsWidget(self, test):
		settings_widget = SettingsWidget(test=test, parent=self)
		self.central_widget.addWidget(settings_widget)
		self.central_widget.setCurrentWidget(settings_widget)

	def newGame(self, test):
		if test:
			self.helpShortcut.activated.connect(self.nothing)
			self.question = 1
			self.stages = []
			self.total_questions = utils.readSettings()["ANSWERS_COUNT"]
		else:
			self.helpShortcut.activated.connect(self.showHelpDialog)

			self.score = 0

		stage = utils.Stage(self.central_widget.stageGenerator)
		game_widget = GameWidget(stage=stage, test=test, parent=self)

		self.central_widget.addWidget(game_widget)
		self.central_widget.setCurrentWidget(game_widget)

	def nextStage(self, test, stage=None, opts=None, last=False):
		if test:
			self.question += 1
			self.stages.append([stage, opts])
			last = (self.question == self.total_questions)

		stage = utils.Stage(self.central_widget.stageGenerator)
		game_widget = GameWidget(stage=stage, test=test, last=last, parent=self)
		self.central_widget.addWidget(game_widget)
		self.central_widget.setCurrentWidget(game_widget)

	def conclusionWidget(self, test, stage, opts):
		if test:
			self.stages.append([stage, opts])
			conclusion_widget = ConclusionWidget(stages=self.stages, parent=self)
		else:
			conclusion_widget = IntermWidget(stage=stage, opts=opts, parent=self)

		self.central_widget.addWidget(conclusion_widget)
		self.central_widget.setCurrentWidget(conclusion_widget)

	def showHelpDialog(self):
		helpDialog = HelpDialog(self)
		helpDialog.show()

	def showAboutDialog(self):
		aboutDialog = AboutDialog(self)
		aboutDialog.show()

	def backToMenu(self):
		self.central_widget.setCurrentWidget(self.menu_widget)

	def incScore(self):
		self.score += 1

	def getScore(self):
		return self.score
		
	def nothing(self):
		pass





