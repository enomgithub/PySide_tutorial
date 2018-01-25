#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

from PySide import QtGui


class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.init_ui()

    def init_ui(self):
        self.btn = QtGui.QPushButton(u"Dialog", self)
        self.btn.move(20, 20)
        self.btn.clicked.connect(self.show_dialog)

        self.le = QtGui.QLineEdit(self)
        self.le.move(130, 22)

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle(u"Input dialog")
        self.show()

    def show_dialog(self):
        text, ok = QtGui.QInputDialog.getText(self, u"Input Dialog",
                                              u"名前を入力してください:")
        if ok:
            # str型ではなくunicode型を引数として渡す
            # (元のコードではstr(text)を渡している)
            self.le.setText(text)


def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    app.exec_()


if __name__ == "__main__":
    sys.exit(main())
