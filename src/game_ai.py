from game_manager import GameManager
import copy

class GameExpectiminimax:
    def __init__(self, game_manager):
        self.game_manager = game_manager
        self.directions = ["UP", "DOWN", "LEFT", "RIGHT"]
        self.max_grid =[[2**4, 2**3, 2**2, 2],
                        [2**5, 2**6, 2**7, 2**8],
                        [2**12, 2**11,2**10,2**9],
                        [2**13,2**14,2**15,2**16]]
        
    #def expectminimax(self, depth, direction):
    #    if depth == 0:
    #        pass

    def next_move(self, depth):
        best_move = "RIGHT"
        best_score = float('-inf')

        for direction in self.directions:
            game_copy = copy.deepcopy(self.game_manager)
            score, moved = game_copy.move(direction)
            if not moved:
                continue
            
            score, move = self.expectiminimax(game_copy, depth, direction)
            if score >= best_score:
                best_score = score
                best_move = move

        return best_move


    def expectiminimax(self, game_copy, depth, direction):
        if depth < 0:
            return self.heuristic_evaluation(game_copy), direction

        score = 0
        if depth != int(depth):
            score = float('-inf')
            for direction in self.directions:
                game_copy_2 = copy.deepcopy(game_copy)
                score, moved = game_copy_2.move(direction)
                if moved:
                    result = self.expectiminimax(game_copy_2, depth-0.5, direction)[0]
                    if result > score: 
                        score = result
    
        elif depth == int(depth):
            score = 0
            free_tiles = game_copy.get_free_tiles()
            for free_tile in free_tiles:
                game_copy.add_game_tile_only_2s(free_tile)
                score += 1.0/len(free_tiles)*self.expectiminimax(game_copy, depth - 0.5, direction)[0]
                game_copy.add_game_tile_only_2s(free_tile)
                
        return (score, direction)

    def heuristic_evaluation(self, game_copy):
        result = 0
        for i in range(4):
            for j in range(4):
                result += game_copy.grid()[i][j] * self.max_grid[i][j]

        return result
