import unittest
from game import Game

class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = Game()
        
    def test_create_grid(self):
        grid = self.game.grid()
        
        self.assertEqual(grid,[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])