import sys
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

        pygame.init()
        self.screen = pygame.display.set_mode((500, 550))
        self.font = pygame.font.SysFont(None, 48)
        pygame.display.set_caption("2048")

    def start(self):
        ''' Starts up the game
        
            Temporary:
                given command because of tests'''
        self.run_game()

    def run_game(self):
        ''' Runs game on loop.
        
            Temporary:
                If not command check for a test. '''
        timer = pygame.time.Clock()
        while True:
            for event in pygame.event.get():
                self.take_input(event)
            if self.ai_enabled:
                direction = self.game_ai.next_move(2)
                self.game_manager.move(direction)

            self.draw_board()
            pygame.display.flip()
            timer.tick(60)


    def take_input(self, event):
        ''' Takes the inputs
        
            Temporary:
                Will be changed with new ui.'''

        if event.type == pygame.QUIT:
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
        ''' Temporary for tests, will involve printing in the future.'''
        self.score = self.game_manager.score()
        return self.score

    def draw_board(self):
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
