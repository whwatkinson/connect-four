from enum import Enum
from re import compile
from typing import Union


class Markers(Enum):
    PLAYER_1 = "X"
    PLAYER_2 = "O"
    CLEAR = " "
    BOTTOM_0 = "0"
    BOTTOM_1 = "1"
    BOTTOM_2 = "2"
    BOTTOM_3 = "3"
    BOTTOM_4 = "4"
    BOTTOM_5 = "5"


class Board:
    def __init__(self, board_height: int = 5, board_width: int = 5):
        self.board_height = board_height
        self.board_height = board_width
        self.board = self.new_board(board_width, board_height)

    @staticmethod
    def new_board(board_width, board_height):

        board = [
            [Markers.CLEAR for _ in range(board_width)] for _ in range(board_height)
        ]
        board += [
            [
                Markers.BOTTOM_0,
                Markers.BOTTOM_1,
                Markers.BOTTOM_2,
                Markers.BOTTOM_3,
                Markers.BOTTOM_4,
                Markers.BOTTOM_5,
            ]
        ]
        return board

    def display_board(self):
        for row in self.board:
            print("|".join([square.value for square in row]))

    def to_bottom(self, player_choice: int):

        for column, row in enumerate(self.board, -1):

            square = row[player_choice]
            free_column = column
            if square != Markers.CLEAR:
                return free_column

    def place_counter(
        self,
        player_counter: Markers,
        player_choice: int,
        free_column: int,
    ):

        self.board[free_column][player_choice] = player_counter

    @staticmethod
    def win_check_re(player_counter: Markers) -> compile:
        pattern = compile(fr".?[{player_counter}]" + r"{4}.?")

        return pattern

    def win_check(self):

        player_1_pattern = self.win_check_re(Markers.PLAYER_1)
        player_2_pattern = self.win_check_re(Markers.PLAYER_2)

    def horizontal_win_check(self, pattern: compile) -> bool:

        for column, row in enumerate(self.board, -1):

            row_joined = "".join([square.value for square in row])

            if pattern.search(row_joined):
                return True

            else:
                return False
