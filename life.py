from random import randint
from time import sleep
import os


class Life:
    __board = []
    __board_height: int
    __board_width: int

    def __init__(self, board_height: int = 10, board_width: int = 10):
        self.__board_height = board_height
        self.__board_width = board_width
        self.__random_board()

    def __random_board(self):
        for i in range(self.__board_height):
            row = []
            for j in range(self.__board_width):
                row.append(randint(0, 1))
            self.__board.append(row)

    def __calc_neighbors(self, i: int, j: int) -> int:
        qty = 0

        if i - 1 >= 0:
            if j - 1 > 0 and self.__board[i - 1][j - 1] == 1:
                qty += 1
            if self.__board[i - 1][j] == 1:
                qty += 1
            if j + 1 < self.__board_width and self.__board[i - 1][j + 1] == 1:
                qty += 1

        if j - 1 > 0 and self.__board[i][j - 1] == 1:
            qty += 1
        if j + 1 < self.__board_width and self.__board[i][j + 1] == 1:
            qty += 1

        if i + 1 < self.__board_height:
            if j - 1 > 0 and self.__board[i + 1][j - 1] == 1:
                qty += 1
            if self.__board[i + 1][j] == 1:
                qty += 1
            if j + 1 < self.__board_width and self.__board[i + 1][j + 1] == 1:
                qty += 1

        return qty

    def __next_turn(self):
        new_board = []
        for i, row in enumerate(self.__board):
            new_row = []
            for j, col in enumerate(row):
                neighbors = self.__calc_neighbors(i, j)

                if (col == 0 and neighbors == 3) or (col == 1 and (neighbors == 2 or neighbors == 3)):
                    new_row.append(1)
                else:
                    new_row.append(0)

            new_board.append(new_row)
        self.__board = new_board

    @staticmethod
    def __clear_console():
        if os.name == 'posix':
            os.system('clear')
        else:
            os.system('cls')

    def __print(self):
        for row in self.__board:
            for col in row:
                if col == 1:
                    print('\x1b[6;30;42m' + '  ' + '\x1b[0m', end='')
                else:
                    print('\x1b[1;30;40m' + '  ' + '\x1b[0m', end='')
            print()

    def play(self):
        while True:
            self.__clear_console()
            self.__print()
            self.__next_turn()
            sleep(0.5)


life = Life(30, 60)
life.play()
