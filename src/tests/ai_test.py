import unittest
import timeit
from game_manager import GameManager
from game_ai import GameExpectiminimax

class TestGameManager(unittest.TestCase):
    ''' Tests for current game code '''
    def setUp(self):
        self.game = FakePlayGame()

    """
    def test_reach_100(self):
        time_reach_100 = timeit.timeit(lambda: self.game.game_loop(100),
                                       number = 1)

        self.assertAlmostEqual(time_reach_100, 10)
    """

    def test_reach_100(self):
        self.game.game_loop(10)
        score = self.game.get_game_score()

        self.assertGreaterEqual(score, 10)

class FakePlayGame:
    def __init__(self):
        self.game_manager = GameManager()
        self.game_ai = GameExpectiminimax(self.game_manager)

    def game_loop(self, mid_check: int):
        while True:
            if self.game_manager.score() >= mid_check:
                break
            if self.game_manager.check_game_end():
                print("GAME LOST")
                print(f"TOTAL SCORE: {self.game_manager.score()}")
                break
            direction = self.game_ai.next_move(2)
            self.game_manager.move(direction)

    def get_game_score(self):
        return self.game_manager.score()

    def set_ready_grid(self):
        pass
