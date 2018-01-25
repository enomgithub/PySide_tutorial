#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

from PySide import QtGui, QtCore


class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.init_ui()

    def init_ui(self):
        self.progress_bar = QtGui.QProgressBar(self)
        self.progress_bar.setGeometry(30, 40, 200, 25)

        self.button = QtGui.QPushButton(u"開始", self)
        self.button.move(40, 80)
        self.button.clicked.connect(self.do_action)

        self.timer = QtCore.QBasicTimer()
        self.step = 0

        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle(u"QtGui.QProgressBar")
        self.show()

    def timerEvent(self, event):
        if self.step >= 100:
            self.timer.stop()
            self.button.setText(u"完了")
            return
        self.step = self.step + 1
        self.progress_bar.setValue(self.step)

    def do_action(self):
        if self.timer.isActive():
            self.timer.stop()
            self.button.setText(u"開始")
        else:
            self.timer.start(100, self)
            self.button.setText(u"停止")


def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    app.exec_()
    return 0


if __name__ == "__main__":
    sys.exit(main())
