import sqlite3
import new_record
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QComboBox, QFileDialog
from PyQt5.QtWidgets import QFormLayout, QGridLayout, QHBoxLayout, QVBoxLayout, QSizePolicy, QAction
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QImage, QColor, QFont, QIcon
from PyQt5.QtCore import QDir, QMargins
# from PIL import Image
import sys
import io


class showRecord(object):

	"""docstring for ShowRecord"""
	def setupUi(self, MainWindow):
		MainWindow.setWindowTitle("Новий запис")
		MainWindow.setMinimumSize(600, 840)
# Create central widget
		central_widget = QtWidgets.QWidget()
		MainWindow.setCentralWidget(central_widget)
# img
		self.img = QtWidgets.QLabel(MainWindow)
		self.img.setText("обкладинка")
		# self.img.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
# name
		self.name = QtWidgets.QLabel(MainWindow)
		self.name.setText("Назва книги")
		self.name.setAlignment(Qt.AlignCenter)
		self.name.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
# author
		self.author = QtWidgets.QLabel(MainWindow)
		self.author.setText("Автор")
		self.author.setAlignment(Qt.AlignCenter)
		self.author.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
# serie
		self.serie = QtWidgets.QLabel(MainWindow)
		self.serie.setText("Серія")
		self.serie.setAlignment(Qt.AlignCenter)
		self.serie.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
# genre
		self.genre = QtWidgets.QLabel(MainWindow)
		self.genre.setText("Жанр")
		self.genre.setAlignment(Qt.AlignCenter)
		self.genre.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
# fav pers
		self.fav = QtWidgets.QLabel(MainWindow)
		self.fav.setText("Улюблений персонаж")
		self.fav.setAlignment(Qt.AlignCenter)
		self.fav.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
# rate
		self.rate = QtWidgets.QLabel(MainWindow)
		self.rate.setText("rate")
		self.rate.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
# notes
		self.notes = QtWidgets.QLabel(MainWindow)
		self.notes.setText("Ваші роздуми про книгу")
		# self.notes.wordWrap(True)
# back button
		self.back = QtWidgets.QPushButton(MainWindow)
		self.back.setText("Назад")
		# self.back.clicked.connect(self.ret_image)
# edit button
		self.edit = QtWidgets.QPushButton(MainWindow)
		self.edit.setText("Редагувати")
# delete button
		self.delete = QtWidgets.QPushButton(MainWindow)
		self.delete.setText("Видалити")
# fonts
		self.img.setFont(QFont('AnastasiaScript', 30))
		self.name.setFont(QFont('AnastasiaScript', 30))
		self.author.setFont(QFont('AnastasiaScript', 30))
		self.serie.setFont(QFont('AnastasiaScript', 30))
		self.genre.setFont(QFont('AnastasiaScript', 30))
		self.fav.setFont(QFont('AnastasiaScript', 30))
		self.rate.setFont(QFont('AnastasiaScript', 30))
		self.notes.setFont(QFont('AnastasiaScript', 30))
		self.back.setFont(QFont('AnastasiaScript', 30))
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
# layout 1
		Lay1 =QHBoxLayout()
		Lay1.addWidget(self.back)
		Lay1.addWidget(self.edit)
		Lay1.addWidget(self.delete)

# layout
		Lay = QVBoxLayout(central_widget)
		Lay.addLayout(Lay2, stretch = 2)
		Lay.addWidget(self.notes)
		Lay.addLayout(Lay1)

	def place(showRecord, record):
		i = record
		elements = []
		print(i)
		for x in i[0]:
			print(x)
			elements.append(x)
		print(elements)
		for y in elements[7]:
			print(y)
		if elements[7] == "no image was given":
			self.img.setText(elements[0])
		else:
			pic = io.BytesIO(elements[7])
			pix = QPixmap(pic)
			img.setPixmap(pix)
		self.name.setText(elements[0])
		self.author.setText(elements[1])
		self.serie.setText(elements[2])
		self.genre.setText(elements[3])
		self.fav.setText(elements[4])
		self.rete.setText(elements[5])
		self.notes.setText(elements[6])
	


if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv) #this one is neccessar
	# sys.argv
	ui = showRecord()
	MainWindow = QtWidgets.QMainWindow()#this one is neccessar
	ui.setupUi(MainWindow)
	MainWindow.showMaximized()#this one is neccessar
	with open("ReadingDiaryStyleSheet.qss", "r") as f:
		style = f.read()
		app.setStyleSheet(style)
	sys.exit(app.exec_())#this one is neccessar