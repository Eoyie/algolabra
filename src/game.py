from random import randint
import game_printer
class Game:
    def __init__(self):
        self._game_grid = []
        self._new_grid()
        
    def _start(self):
        game_printer.print_start()
        game_printer.print_grid(self._game_grid)
        return self._game_grid

    def _new_grid(self):
        self._game_grid.append([0]*4)
        self._game_grid = self._game_grid*4
        
    def grid(self):
        return self._game_grid
        
    def _add_game_tile_only_2s(self):
        row = randint(0, 3)
        column = randint(0, 3)
 
        while self._game_grid[row] != 0:
            row = randint(0, 3)
            column = randint(0, 3)

        self._game_grid[row][column] = 2

