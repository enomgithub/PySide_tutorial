#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

from PySide import QtGui


class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.init_ui()

    def init_ui(self):
        names = [u"Cls", u"Bck", u"", u"Close",
                 u"7", u"8", u"9", u"/",
                 u"4", u"5", u"6", u"*",
                 u"1", u"2", u"3", u"-",
                 u"0", u".", u"=", u"+"]

        grid = QtGui.QGridLayout()

        pos = [(i, j) for i in range(5) for j in range(4)]

        for (i, j), name in zip(pos, names):
            button = QtGui.QPushButton(name)
            if (i, j) == (0, 2):
                grid.addWidget(QtGui.QLabel(""), i, j)
            else:
                grid.addWidget(button, i, j)

        self.setLayout(grid)

        self.move(300, 150)
        self.setWindowTitle(u"Calculator")
        self.show()


def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    app.exec_()
    return 0


if __name__ == "__main__":
    sys.exit(main())
