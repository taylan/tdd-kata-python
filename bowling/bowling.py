from enum import Enum
from random import randrange


class GameStates(Enum):
    Pending, InProgress, Finished = range(3)


class BowlingGame():
    def __init__(self):
        self._current_frame = 1
        self._game_state = GameStates.Pending
        self._last_throw_count = None

    @property
    def current_frame(self):
        return self._current_frame

    @property
    def game_state(self):
        return self._game_state

    @property
    def last_throw_count(self):
        return self._last_throw_count

    def roll(self, pins=None):
        if self._current_frame == 10:
            self._game_state = GameStates.Finished
        else:
            self._last_throw_count = pins or randrange(0, 11)
            self._current_frame += 1
            self._game_state = GameStates.InProgress
