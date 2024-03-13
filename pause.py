from game_state import *
from window import Window
class Pause(Window):
    def __init__(self):
        self.entries = {"Continue": self.continue_game,
                        "Back to menu": self.back}
        super(Pause, self).__init__()

    def continue_game(self, game):
        game.state = GameState.Running

    def back(self, game):
        game.state = GameState.Menu
