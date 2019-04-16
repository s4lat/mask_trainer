from main import MainWindow
from PyQt5.QtWidgets import QApplication
import sys

if __name__ == '__main__':	
	app = QApplication(["MaskTrainer"])
	win = MainWindow()
	win.show()
	sys.exit(app.exec_())
