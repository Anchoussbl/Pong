from window import Window
from game_state import *
class Menu(Window):
    def __init__(self):
        self.entries = {"Start": self.begin_game,
                        "My record": self.record,
                        "Exit": self.exit}
        super(Menu, self).__init__()

    def begin_game(self, game):
        game.reset()
        game.state = GameState.Running

    def exit(self, game):
        game.quit()

    def record(self, game):
        game.state = GameState.Record
