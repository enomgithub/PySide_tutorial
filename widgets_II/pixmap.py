#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

from PySide import QtGui, QtCore


class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.init_ui()

    def init_ui(self):
        hbox = QtGui.QHBoxLayout(self)
        pixmap = QtGui.QPixmap(u"../src/redrock24.png")

        label = QtGui.QLabel(self)
        label.setPixmap(pixmap)

        hbox.addWidget(label)
        self.setLayout(hbox)

        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle(u"Red Rock")
        self.show()


def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    app.exec_()
    return 0


if __name__ == "__main__":
    sys.exit(main())
