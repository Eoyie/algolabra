# algolabra - 2048 Game
[![Pipeline](https://github.com/Eoyie/algolabra/actions/workflows/pipeline.yml/badge.svg)](https://github.com/Eoyie/algolabra/actions/workflows/pipeline.yml)
[![codecov](https://codecov.io/gh/Eoyie/algolabra/graph/badge.svg?token=8VRGDBTIUH)](https://codecov.io/gh/Eoyie/algolabra)

## Quick game commands
- Arrow keys to mode
- Space to enable or stop AI

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

