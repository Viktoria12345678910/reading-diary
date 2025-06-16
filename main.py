# імпортую PyQt і subprocess
from PyQt5 import QtCore, QtGui, QtWidgets 
from PyQt5.QtWidgets import QGridLayout, QVBoxLayout, QHBoxLayout,QFormLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
import subprocess

# оголошую головний клас
class Ui_MainWindow(object):

	def setupUi(self, MainWindow):
		MainWindow.setObjectName("MainWindow")
		MainWindow.setWindowTitle("Читацький щоденник")
		MainWindow.resize(900, 500)
		font = QtGui.QFont()
		font.setFamily("Garamond")
		font.setPointSize(24)
		MainWindow.setFont(font)

		# Create central widget
		central_widget = QtWidgets.QWidget()
		MainWindow.setCentralWidget(central_widget)

		self.rd = QtWidgets.QLabel(MainWindow)
		self.rd.setObjectName("rd")
		self.rd.setText("Читацький щоденник")
		self.rd.setAlignment(Qt.AlignCenter)
		self.rd.setFont(QFont('AnastasiaScript', 30))

		self.new_record = QtWidgets.QPushButton(MainWindow)
		self.new_record.setObjectName("new_record")
		self.new_record.setText("Новий запис")
		self.new_record.setFont(QFont('AnastasiaScript', 30))
		self.new_record.clicked.connect(self.new_record_f)

		self.catalog = QtWidgets.QPushButton(MainWindow)
		self.catalog.setObjectName("catalog")
		self.catalog.setText("Каталог")
		self.catalog.setFont(QFont('AnastasiaScript', 30))
		self.catalog.clicked.connect(self.catalog_f)

		# create layout
		self.lay = QVBoxLayout(central_widget)
		self.lay.setAlignment(Qt.AlignCenter)
		self.lay.addWidget(self.rd)
		self.rd.setAlignment(Qt.AlignCenter)
		self.lay.addWidget(self.new_record)
		self.lay.addWidget(self.catalog)
		
	def new_record_f(self):
		subprocess.run(["python", "new_record.py"])
	def catalog_f(self):
		subprocess.run(["python", "catalog.py"])
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.showMaximized()
    with open("ReadingDiaryStyleSheet.qss", "r") as f:
        style = f.read()
        app.setStyleSheet(style)
    sys.exit(app.exec_())
