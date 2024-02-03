import game_printer
from game_manager import GameManager
from game_ai import GameExpectiminimax

class PlayGame:
    def __init__(self, game_manager = GameManager):
        self.game_manager = GameManager()
        self.game_ai = GameExpectiminimax(self.game_manager)
        self.ai_enabled = False
        self.stage = True
        self.score = 0

    def start(self, command = None):
        ''' Starts up the game
        
            Temporary:
                given command because of tests'''
        game_printer.print_start()
        self.run_game(command)

    def run_game(self, command = None):
        ''' Runs game on loop.
        
            Temporary:
                If not command check for a test. '''
        while self.stage:
            game_printer.print_grid(self.game_manager.grid())
            if self.ai_enabled:
                direction = self.game_ai.next_move(2)
                self.game_manager.move(direction)
            else:
                self.take_input(command)


    def take_input(self, command):
        ''' Takes the inputs
        
            Temporary:
                Will be changed with new ui.'''
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
            self.stage = False
        elif command == "enable":
            self.ai_enabled = True

    def game_score(self):
        ''' Temporary for tests, will involve printing in the future.'''
        self.score = self.game_manager.score
        return self.score
