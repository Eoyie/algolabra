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
### Game AI:
- Not working: Performance tests. Possibly to test in the future how much more optimized/fast could I make the algorithm comparing it to the current slow speed.
- Maybe to be changed:
  - Can't test much currently because of the slow speed. But there is a simple test for ai playing and losing in an impossible grid.

# TODO:
## What types of input were used (especially important for comparative analysis)
Todo: Don't know what this means yet!
- Still not sure what this means and if it applies to my tests.

## How can the tests be repeated
Todo: Don't know what this means yet!

## Results of empirical testing presented in graphical form
TODO
