import copy

class GameExpectiminimax:
    def __init__(self, game_manager):
        self.game_manager = game_manager
        self.directions = ["UP", "DOWN", "LEFT", "RIGHT"]
        self.max_grid =[[2**4, 2**3, 2**2, 2],
                        [2**5, 2**6, 2**7, 2**8],
                        [2**12, 2**11, 2**10, 2**9],
                        [2**13, 2**14, 2**15, 2**16]]

    def heuristic_evaluation(self, game_copy):
        ''' Heuristic evaluation of the game grid
        
            Args:
                game_copy: Copy of the game.
            Returns:
                The result of the evaluation
        '''
        result = 0
        for i in range(4):
            for j in range(4):
                result += game_copy.grid()[i][j] * self.max_grid[i][j]

        return result

    def next_move(self, depth):
        ''' Figures out the best next move with the help of Expectiminimax.
        
            Args:
                depth: Depth for algorithm search.
            Returns: 
                The found best next move.
        '''
        best_move = "RIGHT"
        best_score = float('-inf')

        # Creates a copy of the game to test the best direction with expectiminimax.
        for direction in self.directions:
            game_copy = copy.deepcopy(self.game_manager)
            score, moved = game_copy.move(direction, False)
            if not moved:
                continue
            score, _ = self.expectiminimax(game_copy, depth, direction)
            if score > best_score:
                best_score = score
                best_move = direction
        return best_move

    def expectiminimax(self, game_copy, depth, direction = None):
        ''' Expectiminimax algorithm, with the help of heuristic evaluation.
            Todo: add game end handling.
            
            Args:
                game_copy: Copy of the game the algorithm 
                can test best options on.
                depth: Depth for search.
                direction: Default direction for search.
            Returns:
                The reached score and end direction as a tuple.
        '''
        # If reached wanted depth.
        if depth < 0:
            return self.heuristic_evaluation(game_copy), direction

        total_score = 0
        # Player:
        if depth != int(depth):
            total_score = float('-inf')
            for direction_2 in self.directions:
                game_copy_2 = copy.deepcopy(game_copy)
                _ , moved = game_copy_2.move(direction_2, False)
                if moved:
                    result = self.expectiminimax(game_copy_2, depth - 0.5, \
                                                direction_2)[0]
                    if result > total_score:
                        total_score = result

        # Player: Nature
        elif depth == int(depth):
            total_score = 0
            free_tiles = game_copy.get_free_tiles()
            for free_tile in free_tiles:
                game_copy.add_game_tile(free_tile)
                total_score += 1.0/len(free_tiles) * self.expectiminimax(game_copy, \
                        depth - 0.5, direction)[0]
                game_copy.add_game_tile(free_tile)

        return (total_score, direction)
