import unittest
from game_manager import GameManager

class TestGameManager(unittest.TestCase):
    ''' Temporary tests for current game code '''
    def setUp(self):
        self.game = GameManager()

    def test_start(self):
        score = self.game.score

        self.assertEqual(score, 0)

    def test_move_up(self):
        self.game.move("UP")
        grid = self.game.grid()
        possible_sums = [4, 6]

        self.assertIn(sum(grid[0]), possible_sums)

    def test_move_down(self):
        self.game.move("DOWN")
        grid = self.game.grid()
        possible_sums = [4, 6]

        self.assertIn(sum(grid[3]), possible_sums)

    def test_move_left(self):
        self.game.move("LEFT")
        grid = self.game.grid()
        possible_sums = [4, 6]

        left_column_sum = 0
        for row in grid:
            left_column_sum += row[0]

        self.assertIn(left_column_sum, possible_sums)

    def test_move_right(self):
        self.game.move("RIGHT")
        grid = self.game.grid()
        possible_sums = [4, 6]

        right_column_sum = 0
        for row in grid:
            right_column_sum += row[3]

        self.assertIn(right_column_sum, possible_sums)
