#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

from PySide import QtGui


class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.init_ui()

    def init_ui(self):
        vbox = QtGui.QVBoxLayout()

        btn = QtGui.QPushButton(u"Dialog", self)
        btn.setSizePolicy(QtGui.QSizePolicy.Fixed,
                          QtGui.QSizePolicy.Fixed)
        btn.move(20, 20)
        btn.clicked.connect(self.show_dialog)

        self.lbl = QtGui.QLabel(u"Knowledge only matters", self)
        self.lbl.move(130, 20)

        vbox.addWidget(btn)
        vbox.addWidget(self.lbl)
        self.setLayout(vbox)

        self.setGeometry(300, 300, 250, 180)
        self.setWindowTitle(u"Font dialog")
        self.show()

    def show_dialog(self):
        font, ok = QtGui.QFontDialog.getFont()
        if ok:
            self.lbl.setFont(font)


def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    app.exec_()
    return 0


if __name__ == "__main__":
    sys.exit(main())
