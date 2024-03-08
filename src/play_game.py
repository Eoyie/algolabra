import sys
from time import sleep
import pygame
from game_manager import GameManager
from game_ai import GameExpectiminimax

class PlayGame:
    def __init__(self):
        self.game_manager = GameManager()
        self.game_ai = GameExpectiminimax(self.game_manager)
        self.ai_enabled = False
        self.stage = True
        self.score = 0
        self.invalid = False

        self.ask_grid()

        pygame.init()
        self.screen = pygame.display.set_mode((500, 550))
        self.font = pygame.font.SysFont(None, 48)
        pygame.display.set_caption("2048")

    def start(self):
        ''' Starts up the game unless given grid was invalid. '''
        if self.invalid:
            return
        self.run_game()

    def ask_grid(self):
        ''' Asks for optional given grid or default'''
        print("")
        print("#### 2048 game ####")
        answer = input("Use default grid? (y/n): ")
        print("")
        if answer == "y": # Continue with default
            return
        if answer == "n": # Ask for grid by row
            print("Give custom 4x4 game grid by row (seperated by space): ")
            grid = []
            for _ in range(4):
                grid.append(list(map(int, input().split())))

            if self.game_manager.set_grid(grid): # Check for valid grid
                print("Valid grid, continue to game")
                print("")
                return

            print("Invalid grid")
        else:
            print("Invalid answer")
        self.invalid = True

    def run_game(self):
        ''' Runs game on loop. '''
        timer = pygame.time.Clock()
        while True:
            if self.game_manager.check_game_end():
                self.end_game()
                sleep(2)
                break
            for event in pygame.event.get():
                self.take_input(event)
            if self.ai_enabled:
                direction = self.game_ai.next_move(2)
                self.game_manager.move(direction)

            self.draw_board()
            pygame.display.flip()
            timer.tick(60)


    def take_input(self, event):
        ''' Takes the inputs. '''
        if event.type == pygame.QUIT:
            self.end_game()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.game_manager.move("UP")
            elif event.key == pygame.K_DOWN:
                self.game_manager.move("DOWN")
            elif event.key == pygame.K_LEFT:
                self.game_manager.move("LEFT")
            elif event.key == pygame.K_RIGHT:
                self.game_manager.move("RIGHT")
            elif event.key == pygame.K_SPACE:
                self.ai_enabled = not self.ai_enabled

    def game_score(self):
        ''' Returns game score. '''
        self.score = self.game_manager.score()
        return self.score

    def draw_board(self):
        ''' Draws the pygame view of the board. '''
        self.screen.fill((0,0,0))
        game_grid = self.game_manager.grid()
        x = 0
        for i in range(4):
            y = 50
            for j in range(4):
                rect = pygame.Rect(x, y, 125, 125)
                if game_grid[j][i] != 0:
                    number_text = str(game_grid[j][i])
                    number = self.font.render(number_text, True, (200, 200, 200))
                    number_rect = number.get_rect(center=(x+125/2, y+125/2))
                    self.screen.blit(number, number_rect)
                pygame.draw.rect(self.screen, (200, 200, 200), rect, 1)
                y += 125
            x += 125

        self.game_score()
        score_text = self.font.render(f"Score: {self.score}", True, (200, 200, 200))
        self.screen.blit(score_text, (5,5))

        if self.ai_enabled:
            ai_text = self.font.render("AI enabled", True, (200, 200, 200))
            self.screen.blit(ai_text, (320,5))

    def end_game(self):
        ''' Prints the end score and biggest tile when game is lost or ended'''
        biggest_tile = self.game_manager.biggest_tile()
        print("####################")
        print("GAME END")
        print(f"TOTAL SCORE: {self.game_manager.score()}")
        print(f"BIGGEST TILE: {biggest_tile}")
        print("####################")
