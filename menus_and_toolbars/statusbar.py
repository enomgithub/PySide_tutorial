#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

from PySide import QtGui


class Example(QtGui.QMainWindow):
    def __init__(self):
        super(Example, self).__init__()
        self.init_ui()

    def init_ui(self):
        self.statusBar().showMessage(u"Ready")
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle(u"Status bar")
        self.show()


def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    app.exec_()
    return 0


if __name__ == "__main__":
    sys.exit(main())
