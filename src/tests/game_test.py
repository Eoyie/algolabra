import unittest
from game_manager import GameManager
from play_game import PlayGame

class TestGameManager(unittest.TestCase):
    ''' Temporary tests for current game code '''
    def setUp(self):
        self.game = PlayGame()
        self.game_manager = self.game.game_manager

    def test_start_score(self):
        self.game.start("q")
        score = self.game.game_score()

        self.assertEqual(score, 0)

    def test_move_up(self):
        self.game_manager.move("UP")
        grid = self.game_manager.grid()
        possible_sums = [4, 6]

        self.assertIn(sum(grid[0]), possible_sums)

    def test_move_down(self):
        self.game_manager.move("DOWN")
        grid = self.game_manager.grid()
        possible_sums = [4, 6]

        self.assertIn(sum(grid[3]), possible_sums)

    def test_move_left(self):
        self.game_manager.move("LEFT")
        grid = self.game_manager.grid()
        possible_sums = [4, 6]

        left_column_sum = 0
        for row in grid:
            left_column_sum += row[0]

        self.assertIn(left_column_sum, possible_sums)

    def test_move_right(self):
        self.game_manager.move("RIGHT")
        grid = self.game_manager.grid()
        possible_sums = [4, 6]

        right_column_sum = 0
        for row in grid:
            right_column_sum += row[3]

        self.assertIn(right_column_sum, possible_sums)
