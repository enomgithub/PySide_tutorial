#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

from PySide import QtGui, QtCore


class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.init_ui()

    def init_ui(self):
        calendar = QtGui.QCalendarWidget(self)
        calendar.setGridVisible(True)
        calendar.move(20, 20)
        calendar.clicked[QtCore.QDate].connect(self.show_date)

        self.label = QtGui.QLabel(self)
        date = calendar.selectedDate()
        self.label.setText(date.toString(u"yyyy年MM月dd日 (ddd)"))
        self.label.move(130, 260)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle(u"Calendar")
        self.show()

    def show_date(self, date):
        self.label.setText(date.toString(u"yyyy年MM月dd日 (ddd)"))


def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    app.exec_()
    return 0


if __name__ == "__main__":
    sys.exit(main())
