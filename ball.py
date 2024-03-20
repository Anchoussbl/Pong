import random
class Ball:

    def __init__(self, width, height, radius):
        self.y = height/2 - radius
        self.x = width/2 - radius
        self.radius = radius
        self.speed_x = random.choice([0.5, -0.5])
        self.speed_y = random.choice([0.5, -0.5])

