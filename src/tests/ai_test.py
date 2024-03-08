import unittest
import timeit
from game_manager import GameManager
from game_ai import GameExpectiminimax

class TestGameManager(unittest.TestCase):
    ''' Tests for current game code '''
    def setUp(self):
        self.game = FakePlayGame()

    def test_ai_runs(self):
        self.game.game_loop(4)
        score = self.game.get_game_score()

        self.assertGreaterEqual(score, 2)

    def test_game_loop_2(self):
        game_loop_2 = timeit.timeit(lambda: self.game.game_loop(2),
                                       number = 1)

        self.assertGreaterEqual(game_loop_2, 0.7)

    def test_ai_reach_2048(self):
        grid = [[128, 128, 128, 128],
                [128, 128, 128, 128],
                [128, 128, 128, 128],
                [128, 128, 128, 128]]
        self.assertTrue(self.game.set_grid(grid))

        game_state = self.game.game_loop(9)
        biggest_tile = self.game.biggest_tile()

        self.assertEqual(biggest_tile, 2048)
        self.assertTrue(game_state)

    def test_ai_lose(self):
        grid = [[2, 128, 2, 128],
                [128, 2, 128, 2],
                [2, 128, 2, 128],
                [128, 2, 128, 2]]
        self.assertTrue(self.game.set_grid(grid))

        game_state = self.game.game_loop(2)
        self.assertFalse(game_state)

class FakePlayGame:
    def __init__(self):
        self.game_manager = GameManager()
        self.game_ai = GameExpectiminimax(self.game_manager)

    def game_loop(self, mid_check: int):
        while True:
            if self.game_manager.check_game_end():
                return False
            if mid_check == 0:
                break

            direction = self.game_ai.next_move(2)
            self.game_manager.move(direction)
            mid_check -= 1

        return True

    def get_game_score(self):
        return self.game_manager.score()

    def set_grid(self, grid):
        return self.game_manager.set_grid(grid)

    def biggest_tile(self):
        return self.game_manager.biggest_tile()
