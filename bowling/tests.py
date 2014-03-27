from unittest import TestCase

from bowling import BowlingGame, BowlingFrame, GameStates, FrameResults, \
    BowlingGameFinishedException


class BowlingGameTestCaseBase(TestCase):
    def assertBetween(self, val, first, second, msg=None):
        self.assertTrue(first <= val <= second, msg)


class BowlingGameTestCase(BowlingGameTestCaseBase):
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

    def test_cannot_roll_after_game_is_finished(self):
        for i in range(20):
            self.target.roll(1)
        self.assertEqual(self.target.game_state, GameStates.Finished)
        with self.assertRaises(BowlingGameFinishedException):
            self.target.roll()

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

    def test_bowling_game_str(self):
        self.assertEqual(str(self.target), '<BowlingGame frm: {0}>'.format(1))
        self.target.roll(1)
        self.target.roll(1)
        self.assertEqual(str(self.target), '<BowlingGame frm: {0}>'.format(2))


class BowlingGameScoringTestCase(TestCase):
    def setUp(self):
        self.target = BowlingGame()

    def test_all_gutter_rolls_result_in_zero_score(self):
        for i in range(20):
            self.target.roll(0)

        self.assertEqual(self.target.score, 0)

    def test_strike_in_first_roll_of_frame_ends_frame(self):
        self.target.roll(10)
        self.assertEqual(self.target.current_frame_number, 2)

    def test_all_1_rolls_result_in_20_score(self):
        for i in range(20):
            self.target.roll(1)

        self.assertEqual(self.target.score, 20)


class BowlingFrameTestCase(TestCase):
    def setUp(self):
        self.target = BowlingFrame(1)

    def test_frame_is_complete_after_two_rolls(self):
        self.assertFalse(self.target.is_complete)
        self.target.do_roll(3)
        self.assertFalse(self.target.is_complete)
        self.target.do_roll(5)
        self.assertTrue(self.target.is_complete)

    def test_frame_last_roll_returns_none_when_no_roll_is_made(self):
        self.assertIsNone(self.target.last_roll)

    def test_frame_last_roll_returns_correct_value(self):
        self.target.do_roll(2)
        self.assertEqual(self.target.last_roll, 2)
        self.target.do_roll(4)
        self.assertEqual(self.target.last_roll, 4)

    def test_frame_with_no_rolls_has_in_progress_state(self):
        self.assertEqual(FrameResults.InProgress, self.target.state)

    def test_frame_with_strike_has_strike_state(self):
        self.target.do_roll(10)
        self.assertEqual(FrameResults.Strike, self.target.state)

    def test_frame_with_two_rolls_and_less_than_10_score_has_spare_state(self):
        self.target.do_roll(3)
        self.target.do_roll(6)
        self.assertEqual(FrameResults.Spare, self.target.state)

    def test_bowling_frame_str(self):
        self.assertEqual(str(self.target),
                         '<BowlingFrame({0}), rolls: []>'.format(1))
        self.target.do_roll(2)
        self.assertEqual(str(self.target),
                         '<BowlingFrame({0}), rolls: [2]>'.format(1))

