from collections import OrderedDict


class ChessSquare():
    def __init__(self, rank, file):
        self._rank = rank
        self._file = file

    def __repr__(self):
        return '<ChessSquare: rank={0} file={1}>'.format(self._rank,
                                                         self._file)


class ChessBoard():
    _width = 8
    _height = 8

    def __init__(self):
        self._board = OrderedDict()
        for rank in ChessPiece.RANKS:
            self._board[rank] = {}
            for file in ChessPiece.FILES:
                self._board[rank][file] = ChessSquare(rank=rank, file=file)

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    def get_square(self, rank=None, file=None):
        ChessPiece.validate_rank_and_file(rank, file)
        return self._board[rank][file]


class ChessPiece():
    RANKS = 'abcdefgh'
    FILES = list(range(1, 9))

    @staticmethod
    def validate_rank_and_file(rank, file):
        if rank and rank not in ChessPiece.RANKS:
            raise InvalidPositionException('Rank must be one of {0}'.format(
                ', '.join(ChessPiece.RANKS)))
        if file and file not in ChessPiece.FILES:
            raise InvalidPositionException('Files must be one of {0}'.format(
                ','.join(map(str, ChessPiece.FILES))))

    @staticmethod
    def get_position_from_notation(notation):
        if len(notation) != 2 or \
                notation[0].lower() not in ChessPiece.RANKS or \
                int(notation[1]) not in ChessPiece.FILES:
            raise InvalidNotationException('Algebraic Notation must be in '
                                           'format "AN" where A is'
                                           'the rank (a-h), and N is'
                                           'the file (1-8).')
        return notation[0], int(notation[1])

    def __init__(self, notation=None, rank=None, file=None):
        if notation:
            self._rank, self._file = self.get_position_from_notation(notation)
        else:
            self._rank, self._file = rank, file

        self.validate_rank_and_file(self._rank, self._file)

    @property
    def position(self):
        return 'a' if self._rank and self._file else None


class InvalidNotationException(Exception):
    pass


class InvalidPositionException(Exception):
    pass
