#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

from PySide import QtGui


class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.init_ui()

    def init_ui(self):
        col = QtGui.QColor(0, 0, 0)

        self.btn = QtGui.QPushButton(u"Dialog", self)
        self.btn.move(20, 20)
        self.btn.clicked.connect(self.show_dialog)

        self.frm = QtGui.QFrame(self)
        self.frm.setStyleSheet(u"QWidget { background-color: %s }"
                               % col.name())
        self.frm.setGeometry(130, 22, 100, 100)

        self.setGeometry(300, 300, 250, 180)
        self.setWindowTitle(u"Color dialog")
        self.show()

    def show_dialog(self):
        col = QtGui.QColorDialog.getColor()

        if col.isValid():
            self.frm.setStyleSheet(u"QWidget { background-color: %s }"
                                   % col.name())


def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    app.exec_()
    return 0


if __name__ == "__main__":
    sys.exit(main())
