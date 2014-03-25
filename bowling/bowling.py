from enum import Enum


class GameStates(Enum):
    Pending, InProgress, Finished = range(3)


class BowlingGame():
    def __init__(self):
        self._current_frame = 1
        self._game_state = GameStates.Pending

    @property
    def current_frame(self):
        return self._current_frame

    @property
    def game_state(self):
        return self._game_state

    def roll(self):
        if self._current_frame == 10:
            self._game_state = GameStates.Finished
        else:
            self._current_frame += 1
            self._game_state = GameStates.InProgress
