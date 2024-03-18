import pygame
from constants import *
from paddle import *

class Screen:
    def __init__(self):
        pygame.display.set_caption("Pong")
        self.display = pygame.display.set_mode((WIDTH, HEIGHT))

    def draw_ball(self, ball):
        pygame.draw.circle(self.display, BLUE, (ball.x, ball.y), ball.radius)

    def draw_paddles(self, left_paddle, right_paddle):
        pygame.draw.rect(self.display, RED, pygame.Rect(left_paddle.x, left_paddle.y,
                                                        Paddle.width, Paddle.height))
        pygame.draw.rect(self.display, RED, pygame.Rect(right_paddle.x, right_paddle.y,
                                                        Paddle.width, Paddle.height))

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




