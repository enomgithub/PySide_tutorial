#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

from PySide import QtGui


class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.init_ui()

    def init_ui(self):
        QtGui.QToolTip.setFont(QtGui.QFont(u"SansSerif", 10))
        self.setToolTip(u"これは<b>QWidget</b>ウィジェットです")

        btn = QtGui.QPushButton(u"Button", self)
        btn.setToolTip(u"これは<b>QPushButtonウィジェットです")
        btn.resize(btn.sizeHint())
        btn.move(50, 50)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle(u"Tooltips")
        self.show()


def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    app.exec_()
    return 0


if __name__ == "__main__":
    sys.exit(main())
