# Implementation
## The general structure of the program

### Game Manager
- Grid:
  - New Grid: Creates a starting grid
  - Set Grid: Sets a given custom grid
  - Check Valid Grid: Check validity of custom grid
- Tiles:
  - Add Game Tile: Adds 2 or 4 tiles or a given custom tiles to a given position
  - Get Free Tiles: Returns all blank tiles
- Move & move checks: Moves the grid in given direction based on various checks
- Check Game End

### Game UI
- Ask Grid: Asks if the player wants to use a custom grid or not
- Start: If a valid or default grid moves to the game loop
- Run Game: Game loop
- Take Input: Takes inputs of arrow keys, space and closing
- Draw Board: Updates the pygame visible board
- End Game: Prints the reached biggest tile and score
  
### AI
- Heuristic Evaluation: Snake heuristic evaluation of given board
- Next Move: Gets next best move by the help of Expectiminimax
- Expectiminimax

## The time and space complexities achieved
I remain to be uncertain of these, so estimates in the project estimation are the closest I have to an answer.

## Shortcomings
- AI sometimes frozes when almost full
- AI doesn't check for 4 tiles
## Use of extensive language models
None
## References
- [Wikipedia - 2048 (video game)](https://en.wikipedia.org/wiki/2048_(video_game))
- [Wikipedia - Expectiminimax](https://en.wikipedia.org/wiki/Expectiminimax#:~:text=The%20expectiminimax%20algorithm%20is%20a,elements%20such%20as%20dice%20rolls.)
- [Youtube - Python 2048 Expectiminimax](https://www.youtube.com/watch?v=0fOLkZJ-Q6I&ab_channel=MichaelSchrandt)
- [Preprint - Minimax and Expectimax Algorithm to Solve 2048](https://osf.io/preprints/osf/xfdsr)
  - For general understanding, though not influenced code other than trying to make minimax based on this, which I did not end up using.
- [Beginner’s guide to AI and writing your own bot for the 2048 game](https://medium.com/@bartoszzadrony/beginners-guide-to-ai-and-writing-your-own-bot-for-the-2048-game-4b8083faaf53)
  - For my minimax try and helped realize mistakes made in expectiminimax as well. 
