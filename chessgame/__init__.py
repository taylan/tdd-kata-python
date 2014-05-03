class ChessBoard():
    _width = 8
    _height = 8

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height


class ChessPiece():
    RANKS = 'abcdefgh'
    FILES = list(range(1, 9))

    @staticmethod
    def get_position_from_notation(notation):
        if len(notation) != 2 or \
                notation[0].lower() not in ChessPiece.RANKS or \
                int(notation[1]) not in ChessPiece.FILES:
            raise InvalidNotationException('Algebraic Notation must be in '
                                           'format "AN" where A is'
                                           'the alpha rank, and N is'
                                           'the numeric file.')
        return notation[0], int(notation[1])

    def __init__(self, notation=None, rank=None, file=None):
        if notation:
            self._rank, self._file = self.get_position_from_notation(notation)
        else:
            self._rank, self._file = rank, file

        if self._rank and self._rank not in ChessPiece.RANKS:
            raise InvalidNotationException('Rank must be one of {0}'.format(
                ', '.join(ChessPiece.RANKS)))
        if self._file and self._file not in ChessPiece.FILES:
            raise InvalidNotationException('Files must be one of {0}'.format(
                ','.join(map(str, ChessPiece.FILES))))

    @property
    def position(self):
        return 'a' if self._rank and self._file else None


class InvalidNotationException(Exception): pass
