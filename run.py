from main import MainWindow
from PyQt5.QtWidgets import QApplication
import sys

if __name__ == '__main__':
	pyqt = os.path.dirname(PyQt5.__file__)
	QApplication.addLibraryPath(os.path.join(pyqt, "plugins"))
	
	app = QApplication(["MaskTrainer"])
	win = MainWindow()
	win.show()
	sys.exit(app.exec_())
