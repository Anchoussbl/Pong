import direction
from constants import HEIGHT
class Paddle:
    width = 20
    height = 120

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 0

    def stop_moving(self):
        self.speed = 0

    def start_moving(self, d):
        if d == direction.Up:
            self.speed = -1.7
        else:
            self.speed = 1.7

    def move(self):
        self.y += self.speed
        if self.y + self.height > HEIGHT:
            self.y = HEIGHT - self.height
        if self.y < 0:
            self.y = 0



