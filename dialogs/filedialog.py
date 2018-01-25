#!/usr/bin/env python
# -*- coding: utf-8 -*-
import codecs
import sys

from PySide import QtGui


class Example(QtGui.QMainWindow):
    def __init__(self):
        super(Example, self).__init__()
        self.init_ui()

    def init_ui(self):
        self.text_edit = QtGui.QTextEdit()
        self.setCentralWidget(self.text_edit)
        self.statusBar()

        open_file = QtGui.QAction(QtGui.QIcon(u"../src/open24.png"),
                                  u"Open", self)
        open_file.setShortcut(u"Ctrl+O")
        open_file.setStatusTip(u"新規ファイルを開く")
        open_file.triggered.connect(self.show_dialog)

        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu(u"&File")
        file_menu.addAction(open_file)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle(u"File dialog")
        self.show()

    def show_dialog(self):
        fname, _ = QtGui.QFileDialog.getOpenFileName(self, u"ファイルを開く",
                                                     u"/home")

        with codecs.open(fname, mode=u"r", encoding=u"utf-8") as f:
            data = f.read()
            self.text_edit.setText(data)


def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    app.exec_()


if __name__ == "__main__":
    sys.exit(main())
