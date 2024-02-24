# Testing
## Coverage report
[![codecov](https://codecov.io/gh/Eoyie/algolabra/graph/badge.svg?token=8VRGDBTIUH)](https://codecov.io/gh/Eoyie/algolabra)

## What has been tested and how
### Game manager:
- Game starting: checks score is 0 and there are 14 free tiles.
- Movements: checks for every direction that tiles move correctly by checking the end "wall" of the direction contains at least the first 2 tiles or all 3.
- Set grid:
  - Grid invalidity: check non-valid grids such as ones containing numbers that are not powers of 2.
  - Grid validity: checks changing to valid grid works.
- TODO: Perhaps more movement tests with set grids.
### Game AI
- Questioning how much I should automatically test outside of the general tests I already have.I'd rather prioritize manual testing or make a longer separate test that does the manual test on it's own. Though this kind of test will take very long.

## Manual testing
### Current scores gotten on working?? expectiminimax:
| Total score | Biggest achieved tile |
| ----------- | --------------------- |
| 59982 | 8192? |
| 60222 | 8192? |
| 41364 | 4096? |
| 41134 | 4096? |
| 41800 | 4096? |
| 40932 | 4096? |
| ----- | ----- |
| 40932 | 4096 |
| 25892 | 4096 |
| 63174 | 8192 |
| 40998 | 4096 |

### Current highest achieved score: 63174
Will do more runs to get averages etc. The tiles with question marks are from before I added printing for the biggest tile, but generally, I can assume those tiles were the highest tiles.


# TODO:
## What types of input were used (especially important for comparative analysis)
Todo: Don't know what this means yet!
- Still not sure what this means and if it applies to my tests.

## How can the tests be repeated
With:
```
poetry run invoke test
```
Or manually running the game (Possibly to add an automatic test for playing many games automatically but this will take a long time.)

## Results of empirical testing presented in graphical form
TODO
