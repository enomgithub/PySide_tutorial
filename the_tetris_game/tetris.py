#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
import sys

from PySide import QtGui, QtCore


class Communicate(QtCore.QObject):
    msg_to_sb = QtCore.Signal(str)


class Tetris(QtGui.QMainWindow):
    """
    :type board: Board
    :type status_bar: QtGui.QMainWindow.statusBar
    """
    def __init__(self):
        super(Tetris, self).__init__()
        self.setGeometry(300, 300, 180, 380)
        self.setWindowTitle(u"Tetris")
        self.board = Board(self)
        self.setCentralWidget(self.board)
        self.status_bar = self.statusBar()
        self.board.com.msg_to_sb[str].connect(self.status_bar.showMessage)
        self.board.start()

    def center(self):
        """
        :return: None
        """
        screen = QtGui.QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2,
                  (screen.height() - size.height()) / 2)


class Board(QtGui.QFrame):
    """
    :type board_width: int
    :type board_height: int
    :type speed: int
    :type timer: QtCore.QBasicTimer
    :type is_waiting_after_line: bool
    :type cur_piece: Shape
    :type next_piece: Shape
    :type cur_x: int
    :type cur_y: int
    :type num_lines_removed: int
    :type board: [int]
    :type is_started: bool
    :type is_paused: bool
    :type com: Communicate
    """
    board_width = 10
    board_height = 22
    speed = 300

    def __init__(self, parent):
        """
        :param parent: QtGui.QWidget
        """
        super(Board, self).__init__(parent)
        self.timer = QtCore.QBasicTimer()
        self.is_waiting_after_line = False
        self.cur_piece = Shape()
        self.next_piece = Shape()
        self.cur_x = 0
        self.cur_y = 0
        self.num_lines_removed = 0
        self.board = []
        self.is_started = False
        self.is_paused = False
        self.com = Communicate()
        self.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.clear_board()
        self.next_piece.set_random_shape()

    def shape_at(self, x, y):
        """
        :param x: int
        :param y: int
        :return: int
        """
        return self.board[(y * Board.board_width) + x]

    def set_shape_at(self, x, y, shape):
        """
        :param x: int
        :param y: int
        :param shape: int
        :return: None
        """
        self.board[(y * Board.board_width) + x] = shape

    def square_width(self):
        """
        :return: int
        """
        return self.contentsRect().width() / Board.board_width

    def square_height(self):
        """
        :return: int
        """
        return self.contentsRect().height() / Board.board_height

    def start(self):
        """
        :return: None
        """
        if self.is_paused:
            return
        self.is_started = True
        self.is_waiting_after_line = False
        self.num_lines_removed = 0
        self.clear_board()
        self.com.msg_to_sb.emit(str(self.num_lines_removed))
        self.new_piece()
        self.timer.start(Board.speed, self)

    def pause(self):
        """
        :return: None
        """
        if not self.is_started:
            return
        self.is_paused = not self.is_paused
        if self.is_paused:
            self.timer.stop()
            self.com.msg_to_sb.emit(u"paused")
        else:
            self.timer.start(Board.speed, self)
            self.com.msg_to_sb.emit(str(self.num_lines_removed))
        self.update()

    def paintEvent(self, event):
        """
        :param event: QtCore.QEvent
        :return: None
        """
        painter = QtGui.QPainter(self)
        rect = self.contentsRect()
        board_top = rect.bottom() - Board.board_height * self.square_height()
        for i in range(Board.board_height):
            for j in range(Board.board_width):
                shape = self.shape_at(j, Board.board_height - i - 1)
                if shape != Tetrominoes.no_shape:
                    self.draw_square(painter,
                                     rect.left() + j * self.square_width(),
                                     board_top + i * self.square_height(),
                                     shape)
        if self.cur_piece.shape() != Tetrominoes.no_shape:
            for i in range(4):
                x = self.cur_x + self.cur_piece.x(i)
                y = self.cur_y - self.cur_piece.y(i)
                self.draw_square(painter, rect.left() + x * self.square_width(),
                                 board_top + (Board.board_height - y - 1)
                                 * self.square_height(),
                                 self.cur_piece.shape())

    def keyPressEvent(self, event):
        """
        :param event: QtCore.QEvent
        :return: None
        """
        if not self.is_started \
                or self.cur_piece.shape() == Tetrominoes.no_shape:
            QtGui.QWidget.keyPressEvent(self, event)
            return

        key = event.key()
        if key == QtCore.Qt.Key_P:
            self.pause()
            return
        if self.is_paused:
            return
        elif key == QtCore.Qt.Key_Left:
            self.try_move(self.cur_piece, self.cur_x - 1, self.cur_y)
        elif key == QtCore.Qt.Key_Right:
            self.try_move(self.cur_piece, self.cur_x + 1, self.cur_y)
        elif key == QtCore.Qt.Key_Down:
            self.try_move(self.cur_piece.rotated_right(),
                          self.cur_x, self.cur_y)
        elif key == QtCore.Qt.Key_Up:
            self.try_move(self.cur_piece.rotated_left(),
                          self.cur_x, self.cur_y)
        elif key == QtCore.Qt.Key_Space:
            self.drop_down()
        elif key == QtCore.Qt.Key_D:
            self.one_line_down()
        else:
            QtGui.QWidget.keyPressEvent(self, event)

    def timerEvent(self, event):
        """
        :param event: QtCore.QEvent
        :return: None
        """
        if event.timerId() == self.timer.timerId():
            if self.is_waiting_after_line:
                self.is_waiting_after_line = False
                self.new_piece()
            else:
                self.one_line_down()
        else:
            QtGui.QFrame.timerEvent(self, event)

    def clear_board(self):
        """
        :return: None
        """
        for i in range(Board.board_height * Board.board_width):
            self.board.append(Tetrominoes.no_shape)

    def drop_down(self):
        """
        :return: None
        """
        new_y = self.cur_y
        while new_y > 0:
            if not self.try_move(self.cur_piece, self.cur_x, new_y - 1):
                break
            new_y -= 1
        self.piece_dropped()

    def one_line_down(self):
        """
        :return: None
        """
        if not self.try_move(self.cur_piece, self.cur_x, self.cur_y - 1):
            self.piece_dropped()

    def piece_dropped(self):
        """
        :return: None
        """
        for i in range(4):
            x = self.cur_x + self.cur_piece.x(i)
            y = self.cur_y - self.cur_piece.y(i)
            self.set_shape_at(x, y, self.cur_piece.shape())
        self.remove_full_lines()
        if not self.is_waiting_after_line:
            self.new_piece()

    def remove_full_lines(self):
        """
        :return: None
        """
        num_full_lines = 0
        rows_to_remove = []
        for i in range(Board.board_height):
            n = 0
            for j in range(Board.board_width):
                if not self.shape_at(j, i) == Tetrominoes.no_shape:
                    n += 1
            if n == 10:
                rows_to_remove.append(i)
        rows_to_remove.reverse()
        for m in rows_to_remove:
            for k in range(m, Board.board_height):
                for l in range(Board.board_width):
                    self.set_shape_at(l, k, self.shape_at(l, k + 1))
        num_full_lines += len(rows_to_remove)
        if num_full_lines > 0:
            self.num_lines_removed += num_full_lines
            print self.num_lines_removed
            self.com.msg_to_sb.emit(str(self.num_lines_removed))
            self.is_waiting_after_line = True
            self.cur_piece.set_shape(Tetrominoes.no_shape)
            self.update()

    def new_piece(self):
        """
        :return: None
        """
        self.cur_piece = self.next_piece
        self.next_piece.set_random_shape()
        self.cur_x = Board.board_width / 2 + 1
        self.cur_y = Board.board_height - 1 + self.cur_piece.min_y()
        if not self.try_move(self.cur_piece, self.cur_x, self.cur_y):
            self.cur_piece.set_shape(Tetrominoes.no_shape)
            self.timer.stop()
            self.is_started = False
            self.com.msg_to_sb.emit(u"Game over")

    def try_move(self, new_piece, new_x, new_y):
        """
        :param new_piece: Shape
        :param new_x: int
        :param new_y: int
        :return: bool
        """
        for i in range(4):
            x = new_x + new_piece.x(i)
            y = new_y - new_piece.y(i)
            if not 0 <= x < Board.board_width \
                    or not 0 <= y < Board.board_height:
                return False
            if self.shape_at(x, y) != Tetrominoes.no_shape:
                return False
        self.cur_piece = new_piece
        self.cur_x = new_x
        self.cur_y = new_y
        self.update()
        return True

    def draw_square(self, painter, x, y, shape):
        """
        :param painter: QtGui.QPainter
        :param x: int
        :param y: int
        :param shape: int
        :return: None
        """
        color_table = [0x000000, 0xCC6666, 0x66CC66, 0x6666CC,
                       0xCCCC66, 0xCC66CC, 0x66CCCC, 0xDAAA00]
        color = QtGui.QColor(color_table[shape])
        painter.fillRect(x + 1, y + 1, self.square_width() - 2,
                         self.square_height() - 2, color)
        painter.setPen(color.lighter())
        painter.drawLine(x, y + self.square_height() - 1, x, y)
        painter.drawLine(x, y, x + self.square_width() - 1, y)
        painter.setPen(color.darker())
        painter.drawLine(x + 1, y + self.square_height() - 1,
                         x + self.square_width() - 1,
                         y + self.square_height() - 1)
        painter.drawLine(x + self.square_width() - 1,
                         y + self.square_height() - 1,
                         x + self.square_width() - 1, y + 1)


class Tetrominoes(object):
    """
    :type no_shape: int
    :type z_shape: int
    :type s_shape: int
    :type line_shape: int
    :type t_shape: int
    :type square_shape: int
    :type l_shape: int
    :type mirror_shape: int
    """
    no_shape = 0
    z_shape = 1
    s_shape = 2
    line_shape = 3
    t_shape = 4
    square_shape = 5
    l_shape = 6
    mirror_shape = 7


class Shape(object):
    """
    :type coords_table: (((int, int)))
    :type coords: List[List[int, int]]
    :type piece_shape: int
    """
    coords_table = (((0, 0), (0, 0), (0, 0), (0, 0)),
                    ((0, -1), (0, 0), (-1, 0), (-1, 1)),
                    ((0, -1), (0, 0), (1, 0), (1, 1)),
                    ((0, -1), (0, 0), (0, 1), (0, 2)),
                    ((-1, 0), (0, 0), (1, 0), (0, 1)),
                    ((0, 0), (1, 0), (0, 1), (1, 1)),
                    ((-1, -1), (0, -1), (0, 0), (0, 1)),
                    ((1, -1), (0, -1), (0, 0), (0, 1)))

    def __init__(self):
        self.coords = [[0, 0] for _ in range(4)]
        self.piece_shape = Tetrominoes.no_shape
        self.set_shape(Tetrominoes.no_shape)

    def shape(self):
        """
        :return: int
        """
        return self.piece_shape

    def set_shape(self, shape):
        """
        :param shape: int
        :return: None
        """
        table = Shape.coords_table[shape]
        for i in range(4):
            for j in range(2):
                self.coords[i][j] = table[i][j]
        self.piece_shape = shape

    def set_random_shape(self):
        """
        :return: None
        """
        self.set_shape(random.randint(1, 7))

    def x(self, index):
        """
        :param index: int
        :return: int
        """
        return self.coords[index][0]

    def y(self, index):
        """
        :param index: int
        :return: int
        """
        return self.coords[index][1]

    def set_x(self, index, x):
        """
        :param index: int
        :param x: int
        :return: None
        """
        self.coords[index][0] = x

    def set_y(self, index, y):
        """
        :param index: int
        :param y: int
        :return: None
        """
        self.coords[index][1] = y

    def min_x(self):
        """
        :return: int
        """
        return min([self.coords[i][0] for i in range(4)])

    def max_x(self):
        """
        :return: int
        """
        return max([self.coords[i][0] for i in range(4)])

    def min_y(self):
        """
        :return: int
        """
        return min([self.coords[i][1] for i in range(4)])

    def max_y(self):
        """
        :return: int
        """
        return max([self.coords[i][1] for i in range(4)])

    def rotated_left(self):
        """
        :return: Shape
        """
        if self.piece_shape == Tetrominoes.square_shape:
            return self
        result = Shape()
        result.piece_shape = self.piece_shape
        for i in range(4):
            result.set_x(i, self.y(i))
            result.set_y(i, -self.x(i))
        return result

    def rotated_right(self):
        """
        :return: Shape
        """
        if self.piece_shape == Tetrominoes.square_shape:
            return self
        result = Shape()
        result.piece_shape = self.piece_shape
        for i in range(4):
            result.set_x(i, -self.y(i))
            result.set_y(i, self.x(i))
        return result


def main():
    """
    :return: int
    """
    app = QtGui.QApplication(sys.argv)
    tetris = Tetris()
    tetris.show()
    app.exec_()
    return 0


if __name__ == "__main__":
    sys.exit(main())
