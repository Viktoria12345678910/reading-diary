from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QComboBox, QFileDialog, QGridLayout, QVBoxLayout
from PyQt5.QtWidgets import QHBoxLayout, QStackedWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QImage, QFont, QIcon
from PyQt5.QtCore import QDir
import FlowLayout
import subprocess
import records
import test2
import sqlite3
import sys
# accessing db
conn = sqlite3.connect('records.db')
c = conn.cursor()

class Class_catalog(object):
	record = None
	"""docstring for MainWindow"""
	Name = None
	def setupUi(self, MainWindow):
		MainWindow.setWindowTitle("Каталог")
# Create central widget
		central_widget = QtWidgets.QWidget()
		MainWindow.setCentralWidget(central_widget)
# 
		c.execute("SELECT * FROM records")
		data = c.fetchall()
		rows = len(data)
		
		print(len(data))
# create layout
		lay = FlowLayout.FlowLayout(central_widget)

		count = -1
		count2 = -1
		self.books = []
		lays = []
		texts = []
		
		row = int(rows/7)
		print(row)	
		screen_width = QApplication.desktop().screenGeometry().width()
		width = int(screen_width/8)
#  Preferred
		c.execute("""SELECT name FROM records""")
		names = c.fetchall()

		
		for i in range(rows):
			for x in names:
				text1 = x[0]
				texts.append(text1)
		
			count += 1
			text = texts[count]
			book = QtWidgets.QPushButton(str(text))
			book.setObjectName(str(i))	
			# book.setFixedWidth(width)
			book.setFont(QFont('AnastasiaScript', 30))
			book.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
			book.clicked.connect(lambda ch, name = book.text(): self.GetRecordName(str(name)) )
			# book.clicked.connect(lambda ch, name = book.text(): name)
			# name = book.clicked.connect(lambda ch : print(book.text()) )
			book.clicked.connect(self.OpenRecord)
			self.books.append(book)
			self.imp = self.books[count]
			lay.addWidget(self.imp)
			if i > rows:
				return name

		

	# function
	def GetRecordName(self, name):
		self.recordName = name
		c.execute("""SELECT name, 
			author,
			serie, 
			genre, 
			favourite character,
			rate,
			notes,
			image FROM records WHERE name = ?""", (self.recordName, ))
		self.record = c.fetchall()
		test2.showRecord2.setupUi(test2.showRecord2, MainWindow, self.record)
		return self.record

		
	def OpenRecord(self):
		subprocess.run(["python", "test2.py"])
		# print(self.record)

	# def exportRecord(self):
		# if self.record is not None:  # Check if record exists before printing or exporting
			# print(self.record)
			# return self.record
		# else:
			# print("No record retrieved yet. Please call GetRecordName first.")
			# return None


	
		
	
		

if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)
	ui = Class_catalog()
	MainWindow = QtWidgets.QMainWindow()
	ui.setupUi(MainWindow)
	MainWindow.showMaximized()
	with open("ReadingDiaryStyleSheet.qss", "r") as f:
		style = f.read()
		app.setStyleSheet(style)
	sys.exit(app.exec_())