#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

from PySide import QtGui, QtCore


class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.init_ui()

    def init_ui(self):
        slider = QtGui.QSlider(QtCore.Qt.Horizontal, self)
        slider.setFocusPolicy(QtCore.Qt.NoFocus)
        slider.setGeometry(30, 40, 100, 30)
        slider.valueChanged[int].connect(self.change_value)

        self.label = QtGui.QLabel(self)
        self.label.setPixmap(QtGui.QPixmap(u"../src/mute24.png"))
        self.label.setGeometry(160, 40, 80, 30)

        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle(u"QtGui.QSlider")
        self.show()

    def change_value(self, value):
        if value == 0:
            self.label.setPixmap(QtGui.QPixmap(u"../src/mute24.png"))
        elif 0 < value <= 30:
            self.label.setPixmap(QtGui.QPixmap(u"../src/min24.png"))
        elif 30 < value < 80:
            self.label.setPixmap(QtGui.QPixmap(u"../src/med24.png"))
        else:
            self.label.setPixmap(QtGui.QPixmap(u"../src/max24.png"))


def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    app.exec_()
    return 0


if __name__ == "__main__":
    sys.exit(main())
