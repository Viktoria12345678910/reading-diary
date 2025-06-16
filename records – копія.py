import sqlite3
import new_record
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QComboBox, QFileDialog
from PyQt5.QtWidgets import QFormLayout, QGridLayout, QHBoxLayout, QVBoxLayout, QSizePolicy, QAction
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QImage, QColor, QFont, QIcon
from PyQt5.QtCore import QDir, QMargins
import catalog
import sys

class ShowRecord(object):
	"""docstring for ShowRecord"""
	def setupUi(self, MainWindow):
		MainWindow.setWindowTitle("Новий запис")
		MainWindow.setMinimumSize(600, 840)

		ct = catalog.Class_catalog()
		importRecord = ct.exportRecord()
		print(importRecord)
		

if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)
	# sys.argv
	ui = ShowRecord()
	MainWindow = QtWidgets.QMainWindow()
	ui.setupUi(MainWindow)
	MainWindow.showMaximized()
	with open("ReadingDiaryStyleSheet.qss", "r") as f:
		style = f.read()
		app.setStyleSheet(style)
	sys.exit(app.exec_())