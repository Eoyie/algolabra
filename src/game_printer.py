# Currently separate file, because might change to tkinter from command line.
def print_start():
    ''' Prints starting information '''
    print("---- 2048 Game ----\n")
    print("The commands are:")
    print("'w' : Up")
    print("'s' : Down")
    print("'a' : Left")
    print("'d' : Right")
    print("'q' : To quit the game")

def print_grid(game_grid):
    ''' Prints grid '''
    for row in game_grid:
        print(row)
    print("")
