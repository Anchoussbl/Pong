from constants import HEIGHT, WIDTH
class Ball:

    def __init__(self, width, height, radius):
        self.y = height/2 - radius
        self.x = width/2 - radius
        self.radius = radius
        self.speed_x = 0.5
        self.speed_y = 0.5

    # def move(self):
    #     # calculating ball direction
    #     if (self.y <= 0 + self.radius) or (self.y >= HEIGHT - self.radius):
    #         self.speed_y = - self.speed_y
    #     elif (self.x >= WIDTH - self.radius) or self.x <= 0 + self.radius:
    #         self.speed_x = - self.speed_x
    #     # apply the speed vector
    #     self.x += self.speed_x
    #     self.y += self.speed_y
