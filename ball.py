class Ball:
    def __init__(self, width, height, radius):
        self.y = height/2 - radius
        self.x = width/2 - radius
        self.radius = radius

    def move(self):
        pass
