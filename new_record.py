# імпортую PyQt
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QComboBox, QFileDialog
from PyQt5.QtWidgets import QFormLayout, QGridLayout, QHBoxLayout, QVBoxLayout, QSizePolicy, QAction
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QImage, QColor, QFont, QIcon
from PyQt5.QtCore import QDir, QMargins
import create_tabel
import sqlite3
import sys
import os

class ui_MainWindow(object):
	"""docstring for MainWindow"""
	def setupUi(self, MainWindow):
		MainWindow.setWindowTitle("Новий запис")
		MainWindow.setMinimumSize(600, 840)

# Create central widget
		central_widget = QtWidgets.QWidget()
		MainWindow.setCentralWidget(central_widget)
# img
		self.img = QtWidgets.QPushButton(MainWindow)
		self.img.setText("обкладинка")
		self.img.clicked.connect(self.image_f)
		self.img.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
# name
		self.name = QtWidgets.QLineEdit(MainWindow)
		self.name.setPlaceholderText("Назва книги")
		self.name.setAlignment(Qt.AlignCenter)
		self.name.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
# author
		self.author = QtWidgets.QLineEdit(MainWindow)
		self.author.setPlaceholderText("Автор")
		self.author.setAlignment(Qt.AlignCenter)
		self.author.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
# serie
		self.serie = QtWidgets.QLineEdit(MainWindow)
		self.serie.setPlaceholderText("Серія")
		self.serie.setAlignment(Qt.AlignCenter)
		self.serie.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
# genre
		self.genre = QtWidgets.QLineEdit(MainWindow)
		self.genre.setPlaceholderText("Жанр")
		self.genre.setAlignment(Qt.AlignCenter)
		self.genre.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
# fav pers
		self.fav = QtWidgets.QLineEdit(MainWindow)
		self.fav.setPlaceholderText("Улюблений персонаж")
		self.fav.setAlignment(Qt.AlignCenter)
		self.fav.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
# rate
		self.rate = QtWidgets.QComboBox(MainWindow)
		self.rate.addItems(["*************(S)", "*****(A)", "****(B)", "***(C)", "**(D)", "*(F)"])
		self.rate.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
# notes
		self.notes = QtWidgets.QTextEdit(MainWindow)
		self.notes.setPlaceholderText("Ваші роздуми про книгу")
# save button
		self.save = QtWidgets.QPushButton(MainWindow)
		self.save.setText("зберегти")
		self.save.clicked.connect(self.get_record)
# fonts
		self.img.setFont(QFont('AnastasiaScript', 30))
		self.name.setFont(QFont('AnastasiaScript', 30))
		self.author.setFont(QFont('AnastasiaScript', 30))
		self.serie.setFont(QFont('AnastasiaScript', 30))
		self.genre.setFont(QFont('AnastasiaScript', 30))
		self.fav.setFont(QFont('AnastasiaScript', 30))
		self.rate.setFont(QFont('AnastasiaScript', 30))
		self.notes.setFont(QFont('AnastasiaScript', 30))
		self.save.setFont(QFont('AnastasiaScript', 30))
# spaces
		self.s1 = " "
		self.s2 = " "
		self.s3 = " \n "
		for x in range(100):
			self.s3 += str(" \n ")


		self.space1 = QtWidgets.QLabel(MainWindow)
		self.space1.setText(self.s1)

		self.space2 = QtWidgets.QLabel(MainWindow)
		self.space2.setText(self.s3)

		self.space3 = QtWidgets.QLabel(MainWindow)
		self.space3.setText(self.s2)

		self.space4 = QtWidgets.QLabel(MainWindow)
		self.space4.setText(self.s2)

		self.space5 = QtWidgets.QLabel(MainWindow)
		self.space5.setText(self.s2)

		self.space6 = QtWidgets.QLabel(MainWindow)
		self.space6.setText(self.s2)

		self.space7 = QtWidgets.QLabel(MainWindow)
		self.space7.setText(" ")
# layou 3
		Lay3 = QVBoxLayout()
		Lay3.addWidget(self.name)
		Lay3.addWidget(self.space6)

		Lay3.addWidget(self.author)
		Lay3.addWidget(self.space5)
		
		Lay3.addWidget(self.genre)
		Lay3.addWidget(self.space4)

		Lay3.addWidget(self.serie)
		Lay3.addWidget(self.space3)

		Lay3.addWidget(self.fav)
		Lay3.addWidget(self.space7)

		Lay3.addWidget(self.rate)
# layout 4
		Lay4 = QVBoxLayout()
		Lay4.addWidget(self.img)
# layout 2
		Lay2 = QHBoxLayout()
		Lay2.addLayout(Lay4, stretch = 1)
		Lay2.addLayout(Lay3, stretch = 4)

# layout
		Lay = QVBoxLayout(central_widget)

		Lay.addLayout(Lay2, stretch = 2)

			
	

		Lay.addWidget(self.notes)
		Lay.addWidget(self.save)

		self.image = "no image was given"

# function
	def image_f(self):
		self.fname = QFileDialog.getOpenFileName()
		# creating pixmap
		self.icon = QIcon(self.fname[0])
		self.img.setIcon(self.icon)
		self.img.setIconSize(self.img.rect().size())
		self.img.setText("")
		# convert image into binary to insert in tabel
		with open(self.fname[0], 'rb') as self.i:
			image = self.i.read()
			return self.image

		return self.img
		return self.image			

# function
	def get_record(self):
		self.name2 = self.name.text()
		self.author2 = self.author.text()
		self.serie2 = self.serie.text()
		self.genre2 = self.genre.text()
		self.fav2 = self.fav.text()
		self.rate2 = self.rate.currentText()
		self.notes2 = self.notes.toPlainText()
	# create list to insert into tabel
		self.record = [(str(self.name2)), (str(self.author2)), (str(self.serie2)), (str(self.genre2)),
						(str(self.fav2)), (str(self.rate2)), (str(self.notes2)), (self.image)]
	# create database in memory
		self.conn = sqlite3.connect(':memory:')
		self.conn = sqlite3.connect('records.db')
	# create cursor
		self.c = self.conn.cursor()
	# creating table
		create_tabel.CreateTable()

	# insert
		self.c.execute("INSERT INTO records VALUES(?, ?, ?, ?, ?, ?, ?, ?)", self.record)
		
		self.conn.commit()
	#close connection
		self.conn.close()
		self.to_start()
# function
	def to_start(self):
		self.img.setText('обкладинка')
		self.img.setIcon(QIcon())
		self.name.clear()
		self.author.clear()
		self.notes.clear()
		self.serie.clear()
		self.genre.clear()
		self.fav.clear()
		self.rate.setCurrentIndex(0)

	
if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)
	ui = ui_MainWindow()
	MainWindow = QtWidgets.QMainWindow()
	ui.setupUi(MainWindow)
	MainWindow.showMaximized()
	with open("ReadingDiaryStyleSheet.qss", "r") as f:
		style = f.read()
		app.setStyleSheet(style)
	sys.exit(app.exec_())