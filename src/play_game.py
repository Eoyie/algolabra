import game_printer
from game_manager import GameManager

class PlayGame:
    def __init__(self):
        self.game_manager = GameManager()
        self.start()

    def start(self, command = None):
        ''' Starts up the game
        
            Temporary:
                given command because of tests'''
        game_printer.print_start()
        self.add_game_tile_only_2s()
        self._run_game(command)

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
