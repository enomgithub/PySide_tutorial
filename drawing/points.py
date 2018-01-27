#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
import sys

from PySide import QtGui, QtCore


class Example(QtGui.QWidget):
    """
    :type painter: QtGui.QPainter
    """
    def __init__(self):
        super(Example, self).__init__()

        self.painter = QtGui.QPainter()
        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle(u"Points")

    def paintEvent(self, event):
        """
        :param event: QtCore.QEvent
        :return: None
        """
        self.painter.begin(self)
        self.draw_points()
        self.painter.end()

    def draw_points(self):
        """
        :return: None
        """
        self.painter.setPen(QtCore.Qt.red)
        size = self.size()

        try:
            for i in range(1000):
                x = random.randint(1, size.width() - 1)
                y = random.randint(1, size.height() - 1)
                self.painter.drawPoint(x, y)
        except ValueError:
            print(u"描画失敗: size({0}, {1})".format(size.width(),
                                                     size.height()))
            return


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
