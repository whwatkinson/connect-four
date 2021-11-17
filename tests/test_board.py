from board import Board, Markers


class TestBoard:



    def test_clear_board(self):

        test_board = Board()

        for row in test_board.board[:5]:
            for marker in row:
                assert marker == Markers.CLEAR

