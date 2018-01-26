#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

from PySide import QtGui, QtCore


class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.init_ui()

    def init_ui(self):
        self.label = QtGui.QLabel(self)
        self.label.move(60, 40)

        qline_edit = QtGui.QLineEdit(self)
        qline_edit.move(60, 100)
        qline_edit.textChanged[str].connect(self.on_changed)

        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle(u"QtGui.QLineEdit")
        self.show()

    def on_changed(self, text):
        # textはunicode型
        self.label.setText(text)
        self.label.adjustSize()


def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    app.exec_()
    return 0


if __name__ == "__main__":
    sys.exit(main())
