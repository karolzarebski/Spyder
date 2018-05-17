from PyQt5.QtWidgets import QPushButton, QTextEdit, QGridLayout, QWidget, QApplication
import time, threading, sys


class Okno(QWidget):

    def __init__(self, parent=None):
        super(Okno, self).__init__(parent)
        self.init()

    def init(self):

        self.button = QPushButton("&START", self)
        self.button.clicked.connect(self.buttonFunction)

        self.monitor = QTextEdit(self)

        layout = QGridLayout()

        layout.addWidget(self.monitor, 0, 0)
        layout.addWidget(self.button, 1, 0)

        self.setLayout(layout)

        self.setWindowTitle("Test")

        self.setGeometry(20, 20, 300, 300)

        self.show()

    def buttonFunction(self):
        self.thread = threading.Thread(target=self.threadFunction)
        self.thread.start()

    def threadFunction(self):
        i = 0
        while i <= 50:
            self.monitor.append(str(i))
            time.sleep(0.01)
            i += 1


if __name__ == '__main__':
    app = QApplication(sys.argv)
    clock = Okno()
    sys.exit(app.exec_())
