#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

from PySide import QtGui, QtCore


class Communicate(QtCore.QObject):
    close_app = QtCore.Signal()


class Example(QtGui.QMainWindow):
    def __init__(self):
        super(Example, self).__init__()
        self.init_ui()

    def init_ui(self):
        self.c = Communicate()
        self.c.close_app.connect(self.close)

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle(u"Emit signal")
        self.show()

    def mousePressEvent(self, event):
        self.c.close_app.emit()


def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    app.exec_()
    return 0


if __name__ == "__main__":
    sys.exit(main())
