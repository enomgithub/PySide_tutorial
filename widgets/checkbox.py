#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

from PySide import QtGui, QtCore


class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.init_ui()

    def init_ui(self):
        cb = QtGui.QCheckBox(u"タイトルを表示", self)
        cb.move(20, 20)
        cb.toggle()
        cb.stateChanged.connect(self.change_title)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle(u"QtGui.QCheckBox")
        self.show()

    def change_title(self, state):
        if state == QtCore.Qt.Checked:
            self.setWindowTitle(u"Checkbox")
        else:
            self.setWindowTitle(u"")


def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    app.exec_()
    return 0


if __name__ == "__main__":
    sys.exit(main())
