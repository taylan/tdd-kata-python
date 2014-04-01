from enum import Enum
from random import randrange


class BowlingGameFinishedException(Exception):
    pass


class GameStates(Enum):
    InProgress, Finished = range(2)


class FrameResults(Enum):
    InProgress, Open, Spare, Strike = range(4)


class BowlingFrame():
    def __init__(self, num):
        self._num = num
        self._rolls = []

    @property
    def is_complete(self):
        return sum(self._rolls) >= 10 or len(self._rolls) == 2

    @property
    def first_roll(self):
        return self._rolls[0] if self._rolls else None

    @property
    def last_roll(self):
        return self._rolls[-1] if self._rolls else None

    @property
    def rolls(self):
        return self._rolls

    @property
    def basic_score(self):
        return sum(self._rolls)

    @property
    def symbol(self):
        if self.state == FrameResults.Open:
            return '-'
        if self.state == FrameResults.Spare:
            return '/'
        if self.state == FrameResults.Strike:
            return 'X'

        return ''

    @property
    def state(self):
        if sum(self._rolls) < 10:
            return FrameResults.InProgress if len(self._rolls) in [0, 1] else \
                FrameResults.Open
        else:
            return FrameResults.Spare if len(self._rolls) == 2 else \
                FrameResults.Strike

    def do_roll(self, num):
        self._rolls.append(num)

    def __str__(self):
        return '<BowlingFrame({0}), rolls: {1}>'.format(self._num, self._rolls)


class BowlingGame():
    def __init__(self):
        self._frames = [BowlingFrame(1)]
        self._score = 0
        self._last_throw_count = None

    @property
    def current_frame_number(self):
        return len(self._frames)

    @property
    def game_state(self):
        return GameStates.InProgress if len(self._frames) != 10 \
            or [frm for frm in self._frames if not frm.is_complete] \
            else GameStates.Finished

    @property
    def last_throw_count(self):
        return self._last_throw_count

    @property
    def score(self):
        return self._calculate_score()

    def _calculate_score(self):
        total_score = 0
        for i, frm in enumerate(self._frames):
            if frm.state in [FrameResults.Open, FrameResults.InProgress]:
                total_score += frm.basic_score
            elif frm.state == FrameResults.Spare:
                if len(self._frames) > i:
                    next_throw = self._frames[i+1].first_roll
                    if next_throw:
                        total_score += frm.basic_score
                        total_score += next_throw
                    else:
                        continue
            elif frm.state == FrameResults.Strike:
                total_score += frm.basic_score
                if len(self._frames) > i:
                    next_throws = self._frames[i+1].rolls
                    if len(next_throws) < 2 and len(self._frames) > i+2:
                        next_throws.append(self._frames[i+2].rolls)
                    total_score += sum(next_throws[:2])

        return total_score

    def roll(self, pins=None):
        if self.game_state == GameStates.Finished:
            raise BowlingGameFinishedException()

        throw = pins if pins is not None else randrange(0, 11)
        self._frames[-1].do_roll(throw)
        self._score += throw
        self._last_throw_count = throw

        if self.game_state != GameStates.Finished and \
                self._frames[-1].is_complete:
            self._frames.append(BowlingFrame(len(self._frames) + 1))

    def __str__(self):
        return '<BowlingGame frm: {0}>'.format(self.current_frame_number)
