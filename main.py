import sys
from random import randrange, randint
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import QPointF


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.resize(500, 500)
        self.but.clicked.connect(self.draw)
        self.D = False

    def draw(self):
        self.D = True
        self.repaint()

    def paintEvent(self, event):
        if self.D:
            qp = QPainter()
            qp.begin(self)
            qp.setBrush(QColor(255, 255, 0))
            r = randint(10, 100)
            qp.drawEllipse(randrange(100, 400), randrange(100, 400), r, r)
            self.D = False
            qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
