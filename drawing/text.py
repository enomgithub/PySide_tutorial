#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

from PySide import QtGui, QtCore


class Example(QtGui.QWidget):
    """
    :type painter: QtGui.QPainter
    :type text: unicode
    """
    def __init__(self):
        super(Example, self).__init__()

        self.painter = QtGui.QPainter()
        self.text = u"こんにちは、世界！"
        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle(u"Draw text")

    def paintEvent(self, event):
        """
        :param event: QtCore.QEvent
        :return: None
        """
        self.painter.begin(self)
        self.draw_text(event)
        self.painter.end()

    def draw_text(self, event):
        """
        :param event: QtCore.QEvent
        :return: None
        """
        self.painter.setPen(QtGui.QColor(168, 34, 3))
        self.painter.setFont(QtGui.QFont(u"MS Mincho", 10))
        self.painter.drawText(event.rect(), QtCore.Qt.AlignCenter, self.text)


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
