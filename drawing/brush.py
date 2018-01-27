#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

from PySide import QtGui, QtCore


BRUSH_PATTERNS = [QtCore.Qt.SolidPattern, QtCore.Qt.Dense1Pattern,
                  QtCore.Qt.Dense2Pattern, QtCore.Qt.Dense3Pattern,
                  QtCore.Qt.Dense4Pattern, QtCore.Qt.Dense5Pattern,
                  QtCore.Qt.Dense6Pattern, QtCore.Qt.Dense7Pattern,
                  QtCore.Qt.DiagCrossPattern, QtCore.Qt.HorPattern,
                  QtCore.Qt.VerPattern, QtCore.Qt.BDiagPattern]


class Example(QtGui.QWidget):
    """
    :type painter: QtGui.QPainter
    """
    def __init__(self):
        super(Example, self).__init__()

        self.painter = QtGui.QPainter()
        self.setGeometry(300, 300, 470, 275)
        self.setWindowTitle(u"Brushes")

    def paintEvent(self, event):
        """
        :param event: QtCore.QEvent
        :return: None
        """
        self.painter.begin(self)
        self.draw_brushes()
        self.painter.end()

    def draw_brushes(self):
        """
        :return: None
        """
        brush = QtGui.QBrush()
        for i, pattern in enumerate(BRUSH_PATTERNS):
            brush.setStyle(pattern)
            self.painter.setBrush(brush)
            self.painter.drawRect(10 + 120 * (i % 4), 15 + 95 * (i // 4),
                                  90, 60)


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
