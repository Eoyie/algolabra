from random import randint
import game_printer

class Game:
    def __init__(self):
        self._game_grid = []
        self._new_grid()
        self.temporary_test_pos = (0,0) # Temporary, will eventually be changed
                                        # when moving will be changed to transpose etc.

    def start(self, command = None):
        ''' Starts up the game
        
            Temporary:
                given command because of tests'''
        game_printer.print_start()
        self.add_game_tile_only_2s()
        self._run_game(command)

    def _new_grid(self):
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

        self.temporary_test_pos = (row, column)
        self._game_grid[row][column] = 2

    def _run_game(self, command = None):
        ''' Runs game on loop and asks for input.
            Currently only moves one 2 around grid.
        
            Temporary:
                if not command check for a test. '''
        while True:
            game_printer.print_grid(self._game_grid)
            if not command:
                command = input("Select command: ")

            if command == "w":
                self.move_up()
                command = None
            elif command == "s":
                self.move_down()
                command = None
            elif command == "a":
                self.move_left()
                command = None
            elif command == "d":
                self.move_right()
                command = None
            elif command == "q":
                break

    def move_up(self):
        ''' Very simple temporary movement method based on input:
                Up '''
        row = self.temporary_test_pos[0]
        column = self.temporary_test_pos[1]
        self._game_grid[row][column] = 0
        self._game_grid[0][column] = 2
        self.temporary_test_pos = (0, column)

    def move_down(self):
        ''' Very simple temporary movement method based on input:
                Down '''
        row = self.temporary_test_pos[0]
        column = self.temporary_test_pos[1]
        self._game_grid[row][column] = 0
        self._game_grid[3][column] = 2
        self.temporary_test_pos = (3, column)

    def move_left(self):
        ''' Very simple temporary movement method based on input:
                Left '''
        row = self.temporary_test_pos[0]
        column = self.temporary_test_pos[1]
        self._game_grid[row][column] = 0
        self._game_grid[row][0] = 2
        self.temporary_test_pos = (row, 0)

    def move_right(self):
        ''' Very simple temporary movement method based on input:
                Right '''
        row = self.temporary_test_pos[0]
        column = self.temporary_test_pos[1]
        self._game_grid[row][column] = 0
        self._game_grid[row][3] = 2
        self.temporary_test_pos = (row, 3)
