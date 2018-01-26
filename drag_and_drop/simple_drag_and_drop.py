#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

from PySide import QtGui


class Button(QtGui.QPushButton):
    def __init__(self, title, parent):
        """
        :param title: unicode 
        :param parent: QtGui.QWidget
        """
        super(Button, self).__init__(title, parent)
        self.setAcceptDrops(True)
        
    def dragEnterEvent(self, event):
        """
        :param event: QtCore.QEvent
        :return: None
        """
        if event.mimeData().hasFormat(u"text/plain"):
            event.accept()
        else:
            event.ignore()
            
    def dropEvent(self, event):
        """
        :param event: QtCore.QEvent
        :return: None
        """
        # ボタンのラベルを変更
        self.setText(event.mimeData().text())
        

class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()

        # init UI
        qline_edit = QtGui.QLineEdit(u"", self)
        qline_edit.setDragEnabled(True)
        qline_edit.move(30, 65)

        button = Button(u"Button", self)
        button.move(190, 65)

        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle(u"Simple Drag and Drop")


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
