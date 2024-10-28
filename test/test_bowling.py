import unittest

from bowling import BowlingGame
from bowling_error import BowlingError
from frame import Frame


class TestBowlingGame(unittest.TestCase):

    def test_game_created(self):
        f = Frame(1,5)
        game = BowlingGame()
        game.add_frame(f)
        self.assertEquals(f, game.get_frame_at(0))

    def test_raises_bowling_error(self):
        game = BowlingGame()
        self.assertRaises(BowlingError, game.get_frame_at, 0)

    def test_add_10_frames(self):
        game = BowlingGame()
        game.add_frame(Frame(1, 5))
        game.add_frame(Frame(3, 6))
        game.add_frame(Frame(7, 2))
        game.add_frame(Frame(3, 6))
        game.add_frame(Frame(4, 4))
        game.add_frame(Frame(5, 3))
        game.add_frame(Frame(3, 3))
        game.add_frame(Frame(4, 5))
        game.add_frame(Frame(8, 1))
        test_frame = Frame(2, 6)
        game.add_frame(test_frame)
        self.assertEquals(test_frame, game.get_frame_at(9))

    def test_add_11_frames(self):
        game = BowlingGame()
        game.add_frame(Frame(1, 5))
        game.add_frame(Frame(3, 6))
        game.add_frame(Frame(7, 2))
        game.add_frame(Frame(3, 6))
        game.add_frame(Frame(4, 4))
        game.add_frame(Frame(5, 3))
        game.add_frame(Frame(3, 3))
        game.add_frame(Frame(4, 5))
        game.add_frame(Frame(8, 1))
        game.add_frame(Frame(2, 6))
        self.assertRaises(BowlingError, game.add_frame, Frame(1, 5))

    def test_score_empty_game(self):
        game = BowlingGame()
        self.assertEquals(0, game.calculate_score())

    def test_score_10_frames(self):
        game = BowlingGame()
        game.add_frame(Frame(1, 5))
        game.add_frame(Frame(3, 6))
        game.add_frame(Frame(7, 2))
        game.add_frame(Frame(3, 6))
        game.add_frame(Frame(4, 4))
        game.add_frame(Frame(5, 3))
        game.add_frame(Frame(3, 3))
        game.add_frame(Frame(4, 5))
        game.add_frame(Frame(8, 1))
        game.add_frame(Frame(2, 6))
        self.assertEquals(81, game.calculate_score())

    def test_bonus_throw_score(self):
        game = BowlingGame()
        game.add_frame(Frame(1, 9))
        game.add_frame(Frame(3, 6))
        game.add_frame(Frame(7, 2))
        game.add_frame(Frame(3, 6))
        game.add_frame(Frame(4, 4))
        game.add_frame(Frame(5, 3))
        game.add_frame(Frame(3, 3))
        game.add_frame(Frame(4, 5))
        game.add_frame(Frame(8, 1))
        game.add_frame(Frame(2, 6))
        self.assertEquals(88, game.calculate_score())