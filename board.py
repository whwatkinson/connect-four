

class Board:

    PLAYER_1 = "X"
    PLAYER_2 = "O"

    board = [
        [" ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " "],
        ["_", "_", "_", "_", "_"],
        ["0", "1", "2", "3", "4"],
    ]

    def display_board(self):
        for row in self.board:
            print("|".join(row))
