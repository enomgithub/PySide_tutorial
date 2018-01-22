#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

from PySide import QtGui


class Example(QtGui.QMainWindow):
    def __init__(self):
        super(Example, self).__init__()
        self.init_ui()

    def init_ui(self):
        text_edit = QtGui.QTextEdit()
        self.setCentralWidget(text_edit)

        exit_action = QtGui.QAction(QtGui.QIcon(u"../src/exit24.png"),
                                    u"Exit", self)
        exit_action.setShortcut(u"Ctrl+Q")
        exit_action.setStatusTip(u"Exit application")
        exit_action.triggered.connect(self.close)

        self.statusBar()

        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu(u"&File")
        file_menu.addAction(exit_action)

        toolbar = self.addToolBar(u"Exit")
        toolbar.addAction(exit_action)

        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle(u"Main window")
        self.show()


def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    app.exec_()
    return 0


if __name__ == "__main__":
    sys.exit(main())
