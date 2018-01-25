#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

from PySide import QtGui, QtCore


class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.init_ui()

    def init_ui(self):
        self.col = QtGui.QColor(0, 0, 0)
        red_button = QtGui.QPushButton(u"赤", self)
        red_button.setCheckable(True)
        red_button.move(10, 10)
        red_button.clicked[bool].connect(self.set_color)
        
        green_button = QtGui.QPushButton(u"緑", self)
        green_button.setCheckable(True)
        green_button.move(10, 60)
        green_button.clicked[bool].connect(self.set_color)

        blue_button = QtGui.QPushButton(u"青", self)
        blue_button.setCheckable(True)
        blue_button.move(10, 110)
        blue_button.clicked[bool].connect(self.set_color)

        self.square = QtGui.QFrame(self)
        self.square.setGeometry(150, 20, 100, 100)
        self.square.setStyleSheet(u"QWidget { background-color: %s }"
                                  % self.col.name())
        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle(u"Toggle button")
        self.show()

    def set_color(self, pressed):
        source = self.sender()

        if pressed:
            val = 255
        else:
            val = 0

        if source.text() == u"赤":
            self.col.setRed(val)
        elif source.text() == u"緑":
            self.col.setGreen(val)
        else:
            self.col.setBlue(val)

        self.square.setStyleSheet(u"QFrame { background-color: %s }"
                                  % self.col.name())


def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    app.exec_()
    return 0


if __name__ == "__main__":
    sys.exit(main())
