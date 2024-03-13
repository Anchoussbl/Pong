from game_state import *
from window import Window

class GameOver(Window):
    def __init__(self):
        self.entries = {"Start": self.begin_game,
                        "Bact to menu": self.back}
        self.static_texts = [""]
        super(GameOver, self).__init__()

    def show(self, game):
        self.static_texts[0] = "GAME OVER!"
        super(GameOver, self).show(game)

    def begin_game(self, game):
        game.reset()
        game.state = GameState.Running

    def back(self, game):
        game.state = GameState.Menu


