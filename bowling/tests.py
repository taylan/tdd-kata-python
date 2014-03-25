from bowling import BowlingGame, GameStates
from unittest import TestCase, skip


class BowlingGameTestCaseBase(TestCase):
    def assertBetween(self, val, first, second, msg=None):
        self.assertTrue(first <= val <= second, msg)


class BowlingGameTest(BowlingGameTestCaseBase):
    def setUp(self):
        self.target = BowlingGame()

    def test_game_starts_at_frame_1(self):
        self.assertEqual(self.target.current_frame_number, 1)

    def test_game_starts_at_in_progress_state(self):
        self.assertEqual(self.target.game_state, GameStates.InProgress)

    def test_game_finishes_after_10_frames(self):
        for i in range(20):
            self.target.roll(1)

        self.assertEqual(self.target.current_frame_number, 10)
        self.assertEqual(self.target.game_state, GameStates.Finished)

    def test_game_remembers_last_knocked_down_pin_count(self):
        self.target.roll(1)
        self.assertEqual(self.target.last_throw_count, 1)

    def test_roll_without_specified_score_knocks_down_random_pins(self):
        self.target.roll()
        self.assertBetween(self.target.last_throw_count, 0, 10)

    def test_knock_down_less_than_10_pins_frame_does_not_change(self):
        self.target.roll(5)
        self.assertBetween(self.target.current_frame_number, 0, 10)

    def test_frame_advances_after_two_rolls(self):
        self.target.roll(5)
        self.target.roll(2)
        self.assertEqual(self.target.current_frame_number, 2)

    # def test_strike_increments_frame(self):
    #     self.target.roll(10)
    #     self.assertEqual(self.target.current_frame, 2)
