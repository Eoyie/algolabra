# Project specification

## My degree programme
Bachelor’s in computer science (CS)
## Documentation language
I have chosen to use English for this course. And so the code, game, and documentation will all be in English.

## Coding language
I will be using Python as it is generally the only coding language I am familiar with, 
having used it for all courses and projects in University so far. 
I do not think I'll be able to properly do code reviews on projects written in a different language.

## Data structures and algorithms: What problem am I solving
I will be using the suggested expectiminimax algorithm which is a variation of the minimax algorithm as it is more suited for this game. 
Expectiminimax should help keep more of the random chance part of the game than minimax would allow. 
This is also why I chose it, as I am very familiar with the original game and would like to be able to create a very similar experience.

I might also be extending the other algorithm with alpha-beta pruning, which is used to decrease the number of nodes that are being evaluated. 
I'm still unsure of the use of alpha-beta and expectiminimax as I didn't find much information on the topic, so, unfortunately, this is still an uncertainty for me. 
The wikipedia page for the game also mentions transposition tables and endgame tablebases. I'm not sure if these fit the question, but I still thought I should mention them.

The "problem" I am solving is the generation of new numbered tiles while keeping a random element of chance in the game as well as the player's skill. 

Generally, I had a lot of trouble deciding the expected time and space complexities. But if I haven't completely misunderstood the role of Alpha-beta pruning in this, I'm expecting the time complexity to be along the lines of O(b^d) or O(b^(d/2)) (Or if I'm not using Alpha-beta pruning then hopefully O(b^m) or O(b^m n^m)). Space complexity I'm even more unsure of, but perhaps O(bm).
## Program inputs
The program inputs are what the game 2048 requires to work:
1. Moving the tiles
  - The wasd keys and/or the arrow keys.
    - Will move all numbered tiles on the board to the given direction
      - Based on game rules tiles will or won't combine
    - Will generate a new random low-numbered tile somewhere on the top tiles.
2. General options
  - Most likely text based inputs such as Q to quit, S to start and maybe R to redo one move back.
## Sources
- [Wikipedia - 2048 (video game)](https://en.wikipedia.org/wiki/2048_(video_game))
- [Wikipedia - Expectiminimax](https://en.wikipedia.org/wiki/Expectiminimax)
- [Wikipedia - Alpha-beta pruning](https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning)
