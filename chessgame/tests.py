import unittest
from chessgame import (ChessBoard, ChessPiece, ChessSquare,
                       InvalidNotationException, InvalidPositionException)


class ChessBoardTestCase(unittest.TestCase):
    def test_chess_board_size_is_8_by_8(self):
        cb = ChessBoard()
        self.assertEqual(8, cb.width)
        self.assertEqual(8, cb.height)

    def test_can_retrieve_square_with_valid_position(self):
        cb = ChessBoard()
        self.assertIsNotNone(cb.get_square(rank='a', file=1))
        self.assertIsInstance(cb.get_square(rank='a', file=1), ChessSquare)

    def test_retrieving_square_with_invalid_position_raises_exception(self):
        cb = ChessBoard()
        with self.assertRaises(InvalidPositionException):
            cb.get_square(rank='x', file=9)


class ChessPieceTestCase(unittest.TestCase):
    def test_new_chess_piece_has_no_position(self):
        cp = ChessPiece()
        self.assertIsNone(cp.position)

    def test_chess_piece_can_be_initialized_with_rank_and_file(self):
        cp = ChessPiece(rank='a', file=1)
        self.assertIsNotNone(cp.position)

    def test_init_fails_with_invalid_rank(self):
        with self.assertRaises(InvalidPositionException):
            ChessPiece(rank='x', file=2)

    def test_init_fails_with_invalid_file(self):
        with self.assertRaises(InvalidPositionException):
            ChessPiece(rank='a', file=9)

    def test_chess_piece_can_be_initialized_with_algebraic_notation(self):
        cp = ChessPiece(notation='a1')
        self.assertIsNotNone(cp.position)

    def test_init_with_algebraic_notation_fails_with_invalid_rank(self):
        with self.assertRaises(InvalidNotationException):
            ChessPiece(notation='x1')

    def test_init_with_algebraic_notation_fails_with_invalid_file(self):
        with self.assertRaises(InvalidNotationException):
            ChessPiece(notation='a9')

    def test_init_with_algebraic_notation_fails_with_malformed_notation(self):
        with self.assertRaises(InvalidNotationException):
            ChessPiece(notation='A9l')

        with self.assertRaises(InvalidNotationException):
            ChessPiece(notation='a')

        with self.assertRaises(InvalidNotationException):
            ChessPiece(notation='8')
