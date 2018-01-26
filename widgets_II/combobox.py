#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

from PySide import QtGui, QtCore


class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.init_ui()

    def init_ui(self):
        self.label1 = QtGui.QLabel(u"Linux ディストリビューション", self)
        self.label2 = QtGui.QLabel(u"Ubuntu", self)

        combo = QtGui.QComboBox(self)
        combo.addItem(u"Ubuntu")
        combo.addItem(u"Mandriva")
        combo.addItem(u"Fedora")
        combo.addItem(u"Red Hat")
        combo.addItem(u"Gentoo")
        combo.addItem(u"Debian")
        combo.addItem(u"Vine")
        combo.addItem(u"Void")

        self.label1.move(50, 20)
        combo.move(50 ,50)
        self.label2.move(50, 150)

        combo.activated[str].connect(self.on_activated)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle(u"QtGui.QComboBox")
        self.show()

    def on_activated(self, text):
        self.label2.setText(text)
        self.label2.adjustSize()


def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    app.exec_()
    return 0


if __name__ == "__main__":
    sys.exit(main())
