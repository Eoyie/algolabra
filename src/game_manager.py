from random import randint

class GameManager:
    def __init__(self):
        self._game_grid = []
        self.new_grid()
        
    def new_grid(self):
        ''' Creates blank grid '''
        for _ in range(4):
            self._game_grid.append([0]*4)

    def grid(self):
        ''' Returns game grid '''
        return self._game_grid

    def add_game_tile_only_2s(self):
        ''' Temporary:
                Adds randomly a single 2 to anywhere that's a free space.
                Will be changed when more game logic is created.'''
        row = randint(0, 3)
        column = randint(0, 3)

        while self._game_grid[row][column] != 0:
            row = randint(0, 3)
            column = randint(0, 3)

        self._game_grid[row][column] = 2

    def move(self, direction):
        pass

    def get_free_tiles(self):
        free_tiles = []

        for i in range(4):
            for j in range(4):
                if self._game_grid[i][j] == 0:
                    free_tiles.append((i,j))

        return free_tiles

    def get_game_stage(self):
        pass
