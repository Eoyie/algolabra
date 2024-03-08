from random import randint

class GameManager:
    def __init__(self):
        self._game_grid = []
        self._score = 0
        self._biggest_tile = 2
        self._moved = False
        self._move_score = 0
        self.new_grid()

    def grid(self):
        ''' Returns game grid. '''
        return self._game_grid

    def score(self):
        ''' Returns score. '''
        return self._score

    def biggest_tile(self):
        ''' Returns biggest tile. '''
        return self._biggest_tile

    def new_grid(self):
        ''' Creates starting grid for the game. '''
        for _ in range(4):
            self._game_grid.append([0]*4)
        self.add_game_tile()
        self.add_game_tile()

    def set_grid(self, new_grid):
        ''' Sets game grid to given grid.
        
            Args:
                new_grid: grid that'll replace the old one
            Returns:
                Result of if change was successful'''
        if self.check_valid_grid(new_grid):
            self._game_grid = new_grid
            return True
        return False

    def check_valid_grid(self, grid):
        ''' Checks if given grid is a valid 4x4 grid.
        
            Args:
                grid: grid that'll be checked
            Returns:
                Result of check'''
        if not isinstance(grid, list):
            return False
        if len(grid) != 4:
            return False

        check_0 = 0
        for column in grid:
            check_0 += sum(column)
            if len(column) != 4:
                return False

            # Check if not powers of 2
            for n in column:
                if n != 0:
                    if not (n > 0 and (n & (n - 1)) == 0):
                        return False
                    if n == 1:
                        return False
        if check_0 == 0:
            return False
        return True

    def add_game_tile(self, position = None, num = None):
        ''' Adds randomly a single 2 to anywhere that's a free space 
            or to a given position with given number.
            
            Args:
                position: Possible given position where 
                the new tile will be placed.
                num: Possible given num to be placed for ai
        '''
        if not position:
            row = randint(0, 3)
            column = randint(0, 3)

            while self._game_grid[row][column] != 0:
                row = randint(0, 3)
                column = randint(0, 3)

            if randint(0,100) <= 90:
                self._game_grid[row][column] = 2
            else:
                self._game_grid[row][column] = 4
        else:
            self._game_grid[position[0]][position[1]] = num

    def move(self, direction, add_tile = True):
        ''' Moves tiles on the game grid by given direction.
        
            Args:
                direction: Direction the tiles will be merged/moved based on.
            Returns: 
                Gotten score and information on if anything was moved.
        '''
        self._move_score = 0
        self._moved = False
        # Base values of max grid rows and columns to be checked
        xmin = 0
        xmax = 4
        ymin = 0
        ymax = 4
        collision_grid = []

        for _ in range(4):
            collision_grid.append([False]*4)

        # Based on moving direction change base values and determine the moving direction in xy
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

        # Check whole grid with opposite order if down or right
        for y in range(ymin, ymax, -1 if direction == "DOWN" else 1):
            for x in range(xmin, xmax, -1 if direction == "RIGHT" else 1):
                self.move_checks(x, y, xy, collision_grid)

        self._score += self._move_score

        if self._moved and add_tile:
            self.add_game_tile()

        return self._move_score, self._moved

    def move_checks(self, x, y, xy, collision_grid):
        ''' Does checks for moving tiles in given direction
            and changes the grid based on that. '''
        # if blank tile no moving required
        if self._game_grid[y][x] == 0:
            return

        # Next x and y based on direction
        x_next = x + xy[1]
        y_next = y + xy[0]

        # Move over blank tiles
        while 0 <= x_next < 4 and 0 <= y_next < 4 and \
            self._game_grid[y_next][x_next] == 0:
            x_next += xy[1]
            y_next += xy[0]

        # If out of bounds will be moved back
        if x_next < 0 or x_next >= 4 or y_next < 0 or y_next >= 4:
            x_next -= xy[1]
            y_next -= xy[0]

        # If no movement possible
        if x_next == x and y_next == y:
            return

        # Updating grid:
        # Equal to next tile and not already combined, will be combined
        if self._game_grid[y][x] == self._game_grid[y_next][x_next] \
            and not collision_grid[y_next][x_next]:

            self._moved = True
            collision_grid[y_next][x_next] = True
            self._move_score += self._game_grid[y_next][x_next]

            self._game_grid[y_next][x_next] += self._game_grid[y][x]
            if self._biggest_tile < self._game_grid[y_next][x_next]:
                self._biggest_tile = self._game_grid[y_next][x_next]
            self._game_grid[y][x] = 0

        # Next tile is empty, will be moved to empty tile
        elif self._game_grid[y_next][x_next] == 0:

            self._moved = True
            self._game_grid[y_next][x_next] = self._game_grid[y][x]
            self._game_grid[y][x] = 0

        # If neihter (for example next to already combined tile)
        # move back
        else:
            y_next -= xy[0]
            x_next -= xy[1]
            if y_next == y and x_next == x:
                return

            self._moved = True
            temp = self._game_grid[y][x]
            self._game_grid[y][x] = 0
            self._game_grid[y_next][x_next] = temp

    def check_game_end(self):
        ''' Checks if the game is in a end state. '''
        for i in range(4):
            for j in range(4):
                # Any blank tiles, not over
                if self._game_grid[i][j] == 0:
                    return False

                # Any possible combinations, not over
                if i < 3:
                    if self._game_grid[i][j] == self._game_grid[i+1][j]:
                        return False
                if j < 3:
                    if self._game_grid[i][j] == self._game_grid[i][j+1]:
                        return False
        return True

    def get_free_tiles(self):
        ''' Returns all tiles that are currently free.'''
        free_tiles = []

        for i in range(4):
            for j in range(4):
                if self._game_grid[i][j] == 0:
                    free_tiles.append((i,j))

        return free_tiles
