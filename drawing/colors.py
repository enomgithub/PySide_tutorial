#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

from PySide import QtGui


COLORS = [(200, 0, 0), (255, 80, 0, 160), (25, 0, 90, 200)]


class Example(QtGui.QWidget):
    """
    :type painter: QtGui.QPainter
    """
    def __init__(self):
        super(Example, self).__init__()

        self.painter = QtGui.QPainter()
        self.setGeometry(300, 300, 350, 100)
        self.setWindowTitle(u"Colors")

    def paintEvent(self, event):
        """
        :param event: QtCore.QEvent
        :return: None
        """
        self.painter.begin(self)
        self.draw_rectangles()
        self.painter.end()

    def draw_rectangles(self):
        """
        :return: None
        """
        color = QtGui.QColor(0, 0, 0)
        color.setNamedColor(u"#d4d4d4")
        self.painter.setPen(color)

        for i, col in enumerate(COLORS):
            self.painter.setBrush(QtGui.QColor(*col))
            self.painter.drawRect(10 + 120 * i, 15, 90, 60)


def main():
    """
    :return: int
    """
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    ex.show()
    app.exec_()
    return 0


if __name__ == '__main__':
    sys.exit(main())
