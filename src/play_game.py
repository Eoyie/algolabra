import game_printer
from game_manager import GameManager

class PlayGame:
    def __init__(self):
        self.game_manager = GameManager()

    def start(self, command = None):
        ''' Starts up the game
        
            Temporary:
                given command because of tests'''
        game_printer.print_start()
        self.run_game(command)

    def run_game(self, command = None):
        ''' Runs game on loop and asks for input.
            Currently only moves one 2 around grid.
        
            Temporary:
                if not command check for a test. '''
        while True:
            game_printer.print_grid(self.game_manager.grid())
            if not command:
                command = input("Select command: ")

            if command == "w":
                self.game_manager.move("UP")
                command = None
            elif command == "s":
                self.game_manager.move("DOWN")
                command = None
            elif command == "a":
                self.game_manager.move("LEFT")
                command = None
            elif command == "d":
                self.game_manager.move("RIGHT")
                command = None
            elif command == "q":
                break
