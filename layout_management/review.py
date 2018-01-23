#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

from PySide import QtGui


class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.init_ui()

    def init_ui(self):
        title = QtGui.QLabel(u"Title")
        author = QtGui.QLabel(u"Author")
        review = QtGui.QLabel(u"Review")

        title_edit = QtGui.QLineEdit()
        author_edit = QtGui.QLineEdit()
        review_edit = QtGui.QTextEdit()

        grid = QtGui.QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(title, 0, 0)
        grid.addWidget(title_edit, 0, 1)

        grid.addWidget(author, 1, 0)
        grid.addWidget(author_edit, 1, 1)

        grid.addWidget(review, 2, 0)
        grid.addWidget(review_edit, 2, 1, 4, 1)

        self.setLayout(grid)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle(u"Review")
        self.show()


def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    app.exec_()
    return 0


if __name__ == "__main__":
    sys.exit(main())
