from enum import Enum

class GameState(Enum):
    Menu = 0
    Running = 1
    Pause = 2
    Record = 3
    GameOver = 4
