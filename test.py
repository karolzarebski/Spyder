import sys, time, threading
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QGridLayout, QGroupBox, QLabel, QLCDNumber, QWidget, QSlider, QPushButton, QVBoxLayout, QTextEdit
from PyQt5 import QtCore, QtGui


class Window(QWidget):
	def __init__(self, parent=None):
		super(Window, self).__init__(parent)

		self.label = []
		self.lcd = []
		self.tab = []
		self.label1 = []

		self.monitor = QTextEdit(self)
		self.button = QPushButton("&START", self)
		
		self.button.clicked.connect(self.buttonF)

		self.y = QSlider(Qt.Vertical)
		self.y.setTickPosition(QSlider.TicksBelow)
		self.y.setTickInterval(10)

		grid = QGridLayout()
		grid.addWidget(self.createExampleGroup("Lewy Przód", 0, 3), 0, 0)
		grid.addWidget(self.createExampleGroup("Lewy Środek", 3, 6), 1, 0)
		grid.addWidget(self.createExampleGroup("Lewy Tył", 6, 9), 2, 0)
		grid.addWidget(self.createExampleGroup("Prawy Przód", 9, 12), 0, 1)
		grid.addWidget(self.createExampleGroup("Prawy Środek", 12, 15), 1, 1)
		grid.addWidget(self.createExampleGroup("Prawy Tył", 15, 18), 2, 1)

		g = QVBoxLayout()
		g.addWidget(self.y, 0)

		p = QGridLayout()

		p.addLayout(grid, 0, 0)
		p.addLayout(g, 0, 1)
		p.addWidget(self.monitor, 0, 2)
		p.addWidget(self.button, 2, 0)

		self.setLayout(p)

		self.setWindowTitle("PyQt5 Group Box")
		self.setGeometry(20, 20, 700, 400)

	def buttonF(self):
		self.thread = threading.Thread(target = self.thread)
		self.thread.start()
		
	def thread(self):
		i = 0
		while i <= 100:
			self.monitor.append(str(i))
			i += 1
			time.sleep(0.03)
			
	def createExampleGroup(self, nazwa, p, k):
		groupBox = QGroupBox(nazwa)

		vbox = QGridLayout()

		for i in range(p, k):
			self.tab.append(QSlider(Qt.Horizontal))
			self.label.append(QLabel(str(i + 1) + '.'))
			self.lcd.append(QLCDNumber())
			if i == 2 or i == 5 or i == 8 or i == 11 or i == 14 or i == 17:
				if i == 0: continue
				self.label1.append(QLabel("(Z)"))
			elif i % 3 == 0:
				self.label1.append(QLabel("(X)"))
			elif i == 1 or i == 4 or i == 7 or i == 10 or i == 13 or i == 16:
				self.label1.append(QLabel("(Y)"))
			vbox.addWidget(self.label[i], i, 1)
			vbox.addWidget(self.tab[i], i, 2)
			vbox.addWidget(self.lcd[i], i, 3)
			vbox.addWidget(self.label1[i], i, 3)
			self.tab[i].setRange(-180, 180)
			self.tab[i].valueChanged.connect(lambda value, segment=str(i): self.function(value, segment))
			self.tab[i].setTickPosition(QSlider.TicksBelow)
			self.tab[i].setTickInterval(10)
			self.tab[i].setToolTip(nazwa)

		groupBox.setLayout(vbox)
		return groupBox

	def function(self, value, segment):
		self.lcd[int(segment)].display(value)


if __name__  == '__main__':
	app = QApplication(sys.argv)
	clock = Window()
	clock.show()
	sys.exit(app.exec_())
