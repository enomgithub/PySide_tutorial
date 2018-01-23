#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

from PySide import QtGui


class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.init_ui()

    def init_ui(self):
        label1 = QtGui.QLabel(u"Zetcode", self)
        label1.move(15, 10)

        label2 = QtGui.QLabel(u"Tutorials", self)
        label2.move(35, 40)

        label3 = QtGui.QLabel(u"for programmers", self)
        label3.move(55, 70)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle(u"Absolute")
        self.show()


def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    app.exec_()
    return 0


if __name__ == "__main__":
    sys.exit(main())
