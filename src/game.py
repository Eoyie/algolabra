from random import randint
import game_printer

class Game:
    def __init__(self):
        self._game_grid = []
        self._new_grid()
        self.temporary_test_pos = (0,0)
        
    def start(self, command = None):
        game_printer.print_start()
        self.add_game_tile_only_2s()
        self._run_game(command)

    def _new_grid(self):
        for i in range(4):
            self._game_grid.append([0]*4)

    def grid(self):
        return self._game_grid

    def add_game_tile_only_2s(self):
        row = randint(0, 3)
        column = randint(0, 3)

        while self._game_grid[row][column] != 0:
            row = randint(0, 3)
            column = randint(0, 3)

        self.temporary_test_pos = (row, column)
        self._game_grid[row][column] = 2

    def _run_game(self, command = None):
        while True:
            game_printer.print_grid(self._game_grid)
            if not command:
                command = input("Select command: ")
                
            if command == "w":
                self.move_up()
            elif command == "s":
                self.move_down()
            elif command == "a":
                self.move_left()
            elif command == "d":
                self.move_right()
            elif command == "q":
                break

    def move_up(self):
        row = self.temporary_test_pos[0]
        column = self.temporary_test_pos[1]
        self._game_grid[row][column] = 0
        self._game_grid[0][column] = 2
        self.temporary_test_pos = (0, column)

    def move_down(self):
        row = self.temporary_test_pos[0]
        column = self.temporary_test_pos[1]
        self._game_grid[row][column] = 0
        self._game_grid[3][column] = 2
        self.temporary_test_pos = (3, column)

    def move_left(self):
        row = self.temporary_test_pos[0]
        column = self.temporary_test_pos[1]
        self._game_grid[row][column] = 0
        self._game_grid[row][0] = 2
        self.temporary_test_pos = (row, 0)

    def move_right(self):
        row = self.temporary_test_pos[0]
        column = self.temporary_test_pos[1]
        self._game_grid[row][column] = 0
        self._game_grid[row][3] = 2
        self.temporary_test_pos = (row, 3)
