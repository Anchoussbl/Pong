import pygame

WIDTH = 1000
HEIGHT = 600
# colours
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (100, 100, 100)

# for paddles
paddle_width = 20  # ширина ракетки
paddle_height = 120  # длина ракетки
paddle_y = HEIGHT / 2 - paddle_height / 2
paddle_y1 = HEIGHT / 2 - paddle_height / 2
paddle_x = 100 - paddle_width / 2
paddle_X = WIDTH - (100 - paddle_width / 2)
paddle_vel = 0
paddle_vel1 = 0

# for the ball
radius = 15
ball_x = WIDTH / 2 - radius
ball_y = HEIGHT / 2 - radius
vel_x = 0.5
vel_y = 0.5

# for the gadgets
gad = 0
act = 0
g_left = G_left = 3

class Screen:
    def __init__(self):
        pygame.display.set_caption("Pong")
        self.display = pygame.display.set_mode((WIDTH, HEIGHT))

    def draw_ball(self):
        pygame.draw.circle(self.display, BLUE, (ball_x, ball_y), radius)

    def draw_paddles(self):
        pygame.draw.rect(self.display, RED, pygame.Rect(paddle_x, paddle_y1, paddle_width, paddle_height))
        pygame.draw.rect(self.display, RED, pygame.Rect(paddle_X, paddle_y, paddle_width, paddle_height))
        # отображение внутри палочки белого кружка, который придает скорость:
        # if gad == 1:
        #     pygame.draw.circle(self.display, WHITE, (paddle_X + 10, paddle_y + 10), 4)
        # if act == 1:
        #     pygame.draw.circle(self.display, WHITE, (paddle_x + 10, paddle_y1 + 10), 4)

    def reset(self):
        # Заливаем черным
        self.display.fill(BLACK)

    def update(self):
        # После отрисовки всего, отображаем
        pygame.display.update()

    def draw_text(self, text, x=WIDTH / 2, y=10, color=WHITE):
        size = 23
        font_name = pygame.font.match_font('arial')
        font = pygame.font.Font(font_name, size)
        text_display = font.render(text, True, color)
        text_rect = text_display.get_rect()
        text_rect.midtop = (x, y)
        self.display.blit(text_display, text_rect)




