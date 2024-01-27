def print_start():
    print("---- 2048 Game ----\n")
    print("The commands are:")
    print("'w' : Up")
    print("'s' : Down")
    print("'a' : Left")
    print("'d' : Right")
    print("'q' : To quit the game")
    
    
def print_grid(game_grid):
    for row in game_grid:
        print(row)
    print("")
