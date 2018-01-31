#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

from PySide import QtGui, QtCore


WHITE = (255, 255, 255)
CREAM = (255, 255, 184)
PALE_RED = (255, 175, 175)


class Communicate(QtCore.QObject):
    """
    :type update_bw: QtCore.Signal
    """
    update_bw = QtCore.Signal(int)


class BurningWidget(QtGui.QWidget):
    """
    :type painter: QtGui.QPainter
    :type max_value: int
    :type value: int
    :type threshold: int
    :type div: int
    :type pen: QtGui.QPen
    :type num: [int]
    """
    def __init__(self, max_value=750, init_value=75, threshold=700,
                 min_width=300, min_height=30, div=10, font_size=7):
        """
        :return: None
        """
        assert init_value <= max_value and threshold < max_value,\
            u"init_value <= max_value and threshold < max_value are required."
        super(BurningWidget, self).__init__()
        self.painter = QtGui.QPainter()
        self.setMinimumSize(min_width, min_height)
        self.max_value = max_value
        self.value = init_value
        self.threshold = threshold
        self.div = div
        self.font = QtGui.QFont(u"Serif", font_size, QtGui.QFont.Light)
        self.pen = QtGui.QPen(QtGui.QColor(20, 20, 20), 1, QtCore.Qt.SolidLine)
        self.num = [self.max_value // self.div * (i + 1)
                    for i in range(self.div - 1)]

    def set_value(self, value):
        """
        :param value: int
        :return: None
        """
        self.value = value

    def paintEvent(self, event):
        """
        :param event: QtCore.QEvent
        :return: None
        """
        self.painter.begin(self)
        self.draw_widget()
        self.painter.end()

    def draw_widget(self):
        """
        :return: None
        """
        self.painter.setFont(self.font)

        size = self.size()
        width = size.width()
        height = size.height()

        step = int(round(width / float(self.div)))
        till = int((width / float(self.max_value)) * self.value)
        full = int((width / float(self.max_value)) * self.threshold)

        self.painter.setPen(QtGui.QColor(*WHITE))
        self.painter.setBrush(QtGui.QColor(*CREAM))
        if self.value >= self.threshold:
            self.painter.drawRect(0, 0, full, height)
            self.painter.setPen(QtGui.QColor(*PALE_RED))
            self.painter.setBrush(QtGui.QColor(*PALE_RED))
            self.painter.drawRect(full, 0, till - full, height)
        else:
            self.painter.drawRect(0, 0, till, height)

        self.painter.setPen(self.pen)
        self.painter.setBrush(QtCore.Qt.NoBrush)
        self.painter.drawRect(0, 0, width - 1, height - 1)

        j = 0
        for i in range(step, 10 * step, step):
            self.painter.drawLine(i, 0, i, 5)
            metrics = self.painter.fontMetrics()
            fw = metrics.width(str(self.num[j]))
            self.painter.drawText(i - fw / 2, height / 2, str(self.num[j]))
            j += 1


class Example(QtGui.QWidget):
    """
    :type slider: QtGui.QSlider
    :type widget: BurningWidget
    :type com: Communicate
    """
    def __init__(self):
        """
        :return: None
        """
        super(Example, self).__init__()
        max_value = 750
        init_value = 75
        threshold = 700

        self.slider = QtGui.QSlider(QtCore.Qt.Horizontal, self)
        self.slider.setFocusPolicy(QtCore.Qt.NoFocus)
        self.slider.setRange(1, max_value)
        self.slider.setValue(init_value)
        self.slider.setGeometry(30, 40, 150, 30)
        self.slider.valueChanged[int].connect(self.change_value)

        self.widget = BurningWidget(max_value=max_value, init_value=init_value,
                                    threshold=threshold)

        self.com = Communicate()
        self.com.update_bw[int].connect(self.widget.set_value)

        hbox = QtGui.QHBoxLayout()
        hbox.addWidget(self.widget)

        vbox = QtGui.QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        self.setLayout(vbox)
        self.setGeometry(300, 300, 390, 210)
        self.setWindowTitle(u"Burning widget")

    def change_value(self, value):
        """
        :param value: int
        :return: None
        """
        self.com.update_bw.emit(value)
        self.widget.repaint()


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
