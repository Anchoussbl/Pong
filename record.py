from game_state import *
from window import Window
class Record(Window):
    def __init__(self):
        self.entries = {"Back": self.back}
        self.static_texts = [""]
        super(Record, self).__init__()

    def show(self, game):
        self.static_texts[0] = "Current record: " "Player1: {}, Player2: {}".format(game.rec1, game.rec2)
        super(Record, self).show(game)

    def back(self, game):
        game.state = GameState.Menu
