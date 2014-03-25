from unittest import TestCase
from bowling import BowlingGame, GameStates


class BowlingGameTest(TestCase):
    def setUp(self):
        self.target = BowlingGame()

    def test_game_starts_at_frame_1(self):
        self.assertEqual(self.target.current_frame, 1)

    def test_game_starts_at_pending_state(self):
        self.assertEqual(self.target.game_state, GameStates.Pending)

    def test_first_roll_updates_game_state_to_in_progress(self):
        self.target.roll()
        self.assertEqual(self.target.game_state, GameStates.InProgress)

    def test_one_roll_increments_frame_by_one(self):
        self.target.roll()
        self.assertEqual(self.target.current_frame, 2)

    def test_game_finishes_after_10_frames(self):
        for i in range(10):
            self.target.roll()

        self.assertEqual(self.target.current_frame, 10)
        self.assertEqual(self.target.game_state, GameStates.Finished)

