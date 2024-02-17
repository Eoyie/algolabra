import unittest
from game_manager import GameManager

class TestGameManager(unittest.TestCase):
    ''' Tests for current game code '''
    def setUp(self):
        self.game_manager = GameManager()

    def test_start_score(self):
        score = self.game_manager.score()

        self.assertEqual(score, 0)

    def test_start_free_tiles(self):
        free_tiles = len(self.game_manager.get_free_tiles())

        self.assertEqual(free_tiles, 14)

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

    def test_set_valid_grid(self):
        grid = [[2, 2, 2, 2],
                [2, 2, 2, 2],
                [2, 2, 2, 2],
                [2, 2, 2, 2]]
        self.assertTrue(self.game_manager.set_grid(grid))

    def test_set_invalid_not_grid(self):
        not_grid = 4
        self.assertFalse(self.game_manager.set_grid(not_grid))

    def test_set_invalid_row_grid(self):
        grid = [[2, 2, 2, 2],
                [2, 2, 2, 2],
                [2, 2, 2, 2],
                [2, 2, 2, 2],
                [2, 2, 2, 2]]
        self.assertFalse(self.game_manager.set_grid(grid))

    def test_set_invalid_column_grid(self):
        grid = [[2, 2, 2, 2, 2],
                [2, 2, 2, 2, 2],
                [2, 2, 2, 2, 2],
                [2, 2, 2, 2, 2]]
        self.assertFalse(self.game_manager.set_grid(grid))

    def test_set_invalid_empty_grid(self):
        grid = [[0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0]]
        self.assertFalse(self.game_manager.set_grid(grid))

    def test_set_invalid_odd_number_grid(self):
        grid = [[2, 1, 0, 0],
                [0, 0, 1, 0],
                [0, 2, 0, 0],
                [0, 0, 0, 0]]
        self.assertFalse(self.game_manager.set_grid(grid))

    def test_set_invalid_even_number_grid(self):
        grid = [[2, 6, 0, 0],
                [0, 0, 2, 0],
                [0, 2, 0, 0],
                [0, 0, 0, 0]]
        self.assertFalse(self.game_manager.set_grid(grid))
