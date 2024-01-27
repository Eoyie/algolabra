class Game:
    def __init__(self):
        self.game_grid = []
        self.new_grid()
        
    def start(self):
        print(self.game_grid)
        return self.game_grid

    def new_grid(self):
        self.game_grid.append([0]*4)
        self.game_grid = self.game_grid*4