#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

from PySide import QtGui, QtCore


LINES = [QtCore.Qt.SolidLine, QtCore.Qt.DashLine, QtCore.Qt.DashDotLine,
         QtCore.Qt.DotLine, QtCore.Qt.DashDotLine, QtCore.Qt.CustomDashLine]


class Example(QtGui.QWidget):
    """
    :type painter: QtGui.QPainter
    """
    def __init__(self):
        super(Example, self).__init__()

        # init UI
        self.painter = QtGui.QPainter()
        self.setGeometry(300, 300, 280, 270)
        self.setWindowTitle(u"Pen styles")

    def paintEvent(self, event):
        """
        :param event: QtCore.QEvent
        :return: None
        """
        self.painter.begin(self)
        self.draw_lines()
        self.painter.end()

    def draw_lines(self):
        """
        :return: None
        """
        pen = QtGui.QPen(QtCore.Qt.black, 2)
        for i, line in enumerate(LINES):
            pen.setStyle(line)
            if repr(line) == "PySide.QtCore.Qt.PenStyle.CustomDashLine":
                pen.setDashPattern([1, 4, 5, 4])
            self.painter.setPen(pen)
            self.painter.drawLine(20, 40 * (i + 1), 250, 40 * (i + 1))


def main():
    """
    :return: int
    """
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    ex.show()
    app.exec_()
    return 0


if __name__ == "__main__":
    sys.exit(main())
