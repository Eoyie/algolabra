# algolabra - 2048 Game
[![Pipeline](https://github.com/Eoyie/algolabra/actions/workflows/pipeline.yml/badge.svg)](https://github.com/Eoyie/algolabra/actions/workflows/pipeline.yml)
[![codecov](https://codecov.io/gh/Eoyie/algolabra/graph/badge.svg?token=8VRGDBTIUH)](https://codecov.io/gh/Eoyie/algolabra)

## Documentation
- [Project specification](documentation/Project_specification.md)
- [Testing document](documentation/Testing_document.md)
- [Implementation document](documentation/Implementation_document.md)
  
## Weekly reports

- [Week 1](documentation/Weekly_report_1.md)
- [Week 2](documentation/Weekly_report_2.md)
- [Week 3](documentation/Weekly_report_3.md)
- [Week 4](documentation/Weekly_report_4.md)
- [Week 5](documentation/Weekly_report_5.md)
- [Week 6](documentation/Weekly_report_6.md)

## Quick setup
1. After downloading your clone of the repository install dependencies with:

```
poetry install
```
or if that doesn't work then with:
```
PYTHON_KEYRING_BACKEND=keyring.backends.fail.Keyring poetry install --no-root
```

2. To start the game:
```
poetry run invoke start
```

### Other invoke commands

- Tests (Takes quite a while because of current slow AI!)
```
poetry run invoke test
```
- Coverage report to html
```
poetry run invoke coverage-report
```
- Pylint
```
poetry run invoke pylint
```

# User guide
## Starting a game
As mentioned before the game can be started with the command invoke:
```
poetry run invoke start
```
Though the game can also be started without invoke by this in the root directory:
```
python3 src/index.py
```

### Selecting default grid
```
#### 2048 game ####
Use default grid? (y/n):
```
If you wish to play with the normal default starting grid, input "y" and the game will open up.
### Selecting custom grid
By answering "n" to the previous question you can input a custom grid, but only valid grids will be allowed.
```
Give custom 4x4 game grid by row (seperated by space): 
```
How to make a valid custom grid:
- Inputs are treated as rows:
  - Input 4 numbers divided by spaces to create one row
  - Press "Enter" to move on to the next row and follow the same for all 4 rows
- Use 0s or powers of 2

If your grid is valid the game should open with your given grid as the game grid.

## Playing the game
Play the game as you would a normal 2048, with using the arrow keys to move. 
If you are unfamiliar with the game, here's the tutorial from the official 2048 site:
"HOW TO PLAY: Use your arrow keys to move the tiles. Tiles with the same number merge into one when they touch. Add them up to reach 2048!"

### Using AI
To enable AI in the game just press space. To disable just press space again.
