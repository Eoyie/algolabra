from random import randint

class GameManager:
    def __init__(self):
        self._game_grid = []
        self.score = 0
        self.new_grid()

    def new_grid(self):
        ''' Creates blank grid '''
        for _ in range(4):
            self._game_grid.append([0]*4)
        self.add_game_tile_only_2s()
        self.add_game_tile_only_2s()

    def grid(self):
        ''' Returns game grid '''
        return self._game_grid

    def add_game_tile_only_2s(self, position = None):
        ''' Temporary:
                Adds randomly a single 2 to anywhere that's a free space.
                Will be changed when more game logic is created.'''
        if not position:
            row = randint(0, 3)
            column = randint(0, 3)

            while self._game_grid[row][column] != 0:
                row = randint(0, 3)
                column = randint(0, 3)

            self._game_grid[row][column] = 2
        else:
            self._game_grid[position[0]][position[1]] = 2

    def move(self, direction):
        score = 0
        xmin = 0
        xmax = 4
        ymin = 0
        ymax = 4
        moved = False
        collision_grid = []

        for _ in range(4):
            collision_grid.append([False]*4)

        if direction == "UP":
            xy = (-1,0)
        if direction == "DOWN":
            xy = (1,0)
            ymin = 3
            ymax = -1
        if direction == "LEFT":
            xy = (0,-1)
        if direction == "RIGHT":
            xy = (0,1)
            xmin = 3
            xmax = -1

        for y in range(ymin, ymax, -1 if direction == "DOWN" else 1):
            for x in range(xmin, xmax, -1 if direction == "RIGHT" else 1):
                if self._game_grid[y][x] == 0:
                    continue

                x_next = x + xy[1]
                y_next = y + xy[0]

                while x_next >= 0 and x_next < 4 and y_next >= 0 \
                    and y_next < 4 and self._game_grid[y_next][x_next] == 0:
                    x_next += xy[1]
                    y_next += xy[0]

                if x_next < 0 or x_next >= 4 or y_next < 0 or y_next >= 4:
                    x_next -= xy[1]
                    y_next -= xy[0]

                if x_next == x and y_next == y:
                    continue

                if self._game_grid[y][x] == self._game_grid[y_next][x_next] \
                    and not collision_grid[y_next][x_next]:

                    moved = True
                    collision_grid[y_next][x_next] = True
                    score += self._game_grid[y_next][x_next]

                    self._game_grid[y_next][x_next] += self._game_grid[y][x]
                    self._game_grid[y][x] = 0
                elif self._game_grid[y_next][x_next] == 0:

                    moved = True
                    self._game_grid[y_next][x_next] = self._game_grid[y][x]
                    self._game_grid[y][x] = 0
                else:
                    y_next -= xy[0]
                    x_next -= xy[1]
                    if y_next == y and x_next == x:
                        continue

                    moved = True
                    temp = self._game_grid[y][x]
                    self._game_grid[y][x] = 0
                    self._game_grid[y_next][x_next] = temp

        self.score += score
        if moved:
            self.add_game_tile_only_2s()
        return score, moved

    def get_game_stage(self):
        pass

    def get_free_tiles(self):
        free_tiles = []

        for i in range(4):
            for j in range(4):
                if self._game_grid[i][j] == 0:
                    free_tiles.append((i,j))

        return free_tiles