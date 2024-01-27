import unittest
from game import Game

class TestGame(unittest.TestCase):
    ''' Temporary tests for current game code '''
    def setUp(self):
        self.game = Game()

    def test_create_grid_blank(self):
        grid = self.game.grid()

        self.assertEqual(grid,[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])

    def test_starting_grid(self):
        self.game.start('q')
        start_grid = self.game.grid()

        self.assertEqual(sum(map(sum, start_grid)),2)

    def test_move_up(self):
        self.game.add_game_tile_only_2s()
        self.game.move_up()
        grid = self.game.grid()

        self.assertEqual(sum(grid[0]), 2)

    def test_move_down(self):
        self.game.add_game_tile_only_2s()
        self.game.move_down()
        grid = self.game.grid()

        self.assertEqual(sum(grid[3]), 2)

    def test_move_left(self):
        self.game.add_game_tile_only_2s()
        self.game.move_left()
        grid = self.game.grid()

        left_column_sum = 0
        for row in grid:
            left_column_sum += row[0]

        self.assertEqual(left_column_sum, 2)

    def test_move_right(self):
        self.game.add_game_tile_only_2s()
        self.game.move_right()
        grid = self.game.grid()

        right_column_sum = 0
        for row in grid:
            right_column_sum += row[3]

        self.assertEqual(right_column_sum, 2)
