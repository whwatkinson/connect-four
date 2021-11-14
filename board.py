from enum import Enum
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

    PLAYER_1 = "X"
    PLAYER_2 = "O"

    board = [
        [
            Markers.CLEAR,
            Markers.CLEAR,
            Markers.CLEAR,
            Markers.CLEAR,
            Markers.CLEAR,
            Markers.CLEAR,
        ],
        [
            Markers.CLEAR,
            Markers.CLEAR,
            Markers.CLEAR,
            Markers.CLEAR,
            Markers.CLEAR,
            Markers.CLEAR,
        ],
        [
            Markers.CLEAR,
            Markers.CLEAR,
            Markers.CLEAR,
            Markers.CLEAR,
            Markers.CLEAR,
            Markers.CLEAR,
        ],
        [
            Markers.CLEAR,
            Markers.CLEAR,
            Markers.CLEAR,
            Markers.CLEAR,
            Markers.CLEAR,
            Markers.CLEAR,
        ],
        [
            Markers.CLEAR,
            Markers.CLEAR,
            Markers.CLEAR,
            Markers.CLEAR,
            Markers.CLEAR,
            Markers.CLEAR,
        ],
        [
            Markers.CLEAR,
            Markers.CLEAR,
            Markers.CLEAR,
            Markers.CLEAR,
            Markers.CLEAR,
            Markers.CLEAR,
        ],
        [
            Markers.BOTTOM_0,
            Markers.BOTTOM_1,
            Markers.BOTTOM_2,
            Markers.BOTTOM_3,
            Markers.BOTTOM_4,
            Markers.BOTTOM_5,
        ],
    ]

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
        player_counter: Union[Markers.PLAYER_1, Markers.PLAYER_2],
        player_choice: int,
        free_column: int,
    ):

        self.board[free_column][player_choice] = player_counter
