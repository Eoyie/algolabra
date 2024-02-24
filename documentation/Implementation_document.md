# Implementation
## The general structure of the program

### Game Manager
- Grid:
  - New Grid
  - Set Grid
  - Check Valid Grid
- Tiles:
  - Add Game Tile
  - Get Free Tiles
- Move
- Check Game End

### Game UI
- Start
- Run Game
- Take Input
- Draw Board
  
### AI
- Heuristic Evaluation
- Next Move
- Expectiminimax
  
Todo:
Add class picture? Either change completely to a text-based explanation or keep bullet points, but add all the needed info.

## The time and space complexities achieved (e.g., Big O analyses from pseudocode).
### Potentially, performance and Big O analysis comparison (if applicable to the topic).
Need to double check. Otherwise same as mentioned in project specification?

## Shortcomings
To see, but might generally actually work now? If so will add to this later.
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
- Todo: Add more!
