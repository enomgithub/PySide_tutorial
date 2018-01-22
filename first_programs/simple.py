#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

from PySide import QtGui


def main():
    app = QtGui.QApplication(sys.argv)
    wid = QtGui.QWidget()
    wid.resize(250, 150)
    wid.setWindowTitle(u"Simple")
    wid.show()
    app.exec_()
    return 0


if __name__ == "__main__":
    sys.exit(main())
