#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

from PySide import QtGui, QtCore


class Button(QtGui.QPushButton):
    def __init__(self, title, parent):
        """
        :param title: unicode
        :param parent: QWidget
        """
        super(Button, self).__init__(title, parent)

    def mouseMoveEvent(self, event):
        """
        :param event: QtCore.QEvent
        :return: None
        """
        if event.buttons() != QtCore.Qt.RightButton:
            return
        mime_data = QtCore.QMimeData()

        drag = QtGui.QDrag(self)
        drag.setMimeData(mime_data)
        drag.setHotSpot(event.pos() - self.rect().topLeft())
        drag.start(QtCore.Qt.MoveAction)

    def mousePressEvent(self, event):
        """
        :param event: QtCore.QEvent
        :return: None
        """
        QtGui.QPushButton.mousePressEvent(self, event)
        if event.buttons() == QtCore.Qt.LeftButton:
            print u"左クリック"
        elif event.buttons() == QtCore.Qt.MidButton:
            print u"センタークリック"


class Example(QtGui.QWidget):
    """
    :type button: Button
    """
    def __init__(self):
        super(Example, self).__init__()

        # init UI
        self.setAcceptDrops(True)
        self.button = Button(u"Button", self)
        self.button.move(100, 65)

        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle(u"Click or move")

    def dragEnterEvent(self, event):
        """
        :param event: QtCore.QEvent
        :return: None
        """
        event.accept()

    def dropEvent(self, event):
        """
        :param event: QtCore.QEvent
        :return: None
        """
        position = event.pos()
        self.button.move(position)

        event.setDropAction(QtCore.Qt.MoveAction)
        event.accept()


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
