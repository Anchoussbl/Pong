from ball import *
from screen import *
from constants import *
from menu import *
from pause import *
from record import *
from game_state import *
from database import *


class Game:
    running = True

    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = Screen()
        self.ball = Ball(WIDTH, HEIGHT, 15)
        self.left_paddle = Paddle(100 - Paddle.width / 2,
                                  HEIGHT / 2 - Paddle.height / 2)
        self.right_paddle = Paddle(WIDTH - (100 - Paddle.width / 2),
                                   HEIGHT / 2 - Paddle.height / 2)
        self.state = GameState.Menu
        self.speed = 10
        self.menu = Menu()
        self.pause = Pause()
        self.record = Record()
        self.database = DataBase()
        data = self.database.load()
        self.rec1 = data["Player1"] if data else 0
        self.rec2 = data["Player2"] if data else 0
        self.score1 = 0
        self.score2 = 0

    def run(self):
        time_elapsed = 0
        while self.running:
            time_elapsed += self.clock.tick()
            # for the inputs
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if self.state == GameState.Running:
                        if event.key == pygame.K_DOWN:
                            self.right_paddle.start_moving(direction.Down)
                        elif event.key == pygame.K_UP:
                            self.right_paddle.start_moving(direction.Up)
                        elif event.key == pygame.K_s:
                            self.left_paddle.start_moving(direction.Down)
                        elif event.key == pygame.K_w:
                            self.left_paddle.start_moving(direction.Up)
                        if event.key == pygame.K_ESCAPE:
                            self.state = GameState.Pause
                    elif self.state == GameState.Menu:
                        self.menu.handle_press(self, event.key)
                    elif self.state == GameState.Pause:
                        self.pause.handle_press(self, event.key)
                    elif self.state == GameState.Record:
                        self.record.handle_press(self, event.key)

                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        self.right_paddle.stop_moving()
                    elif event.key == pygame.K_w or event.key == pygame.K_s:
                        self.left_paddle.stop_moving()

            if time_elapsed > self.speed:
                # Обновляем логику игры
                if self.state == GameState.Running:
                    self.tick()
                    time_elapsed = 0

            if self.state == GameState.Running:
                self.screen.reset()
                self.screen.draw_ball(self.ball)
                self.screen.draw_paddles(self.left_paddle, self.right_paddle)
                self.screen.draw_text(str(f"{self.score1} : {self.score2}"))
                self.screen.draw_text(str("record: {} : {}".format(self.rec1, self.rec2)), x=80, y=10)
                self.screen.update()
            elif self.state == GameState.Menu:
                # show menu
                self.handle_menu()
            elif self.state == GameState.Pause:
                # show pause
                self.handle_pause()
            elif self.state == GameState.Record:
                # show record
                self.record.show(self)

        if not self.running:
            self.game_over()

    def tick(self):
        self.handle_movement()
        self.check_up_down()
        self.check_right_paddle()
        self.check_left_paddle()
        self.check_walls()

    def handle_movement(self):
        self.left_paddle.move()
        self.right_paddle.move()

    def check_up_down(self):
        if (self.ball.y <= 0 + self.ball.radius) or (self.ball.y >= HEIGHT - self.ball.radius):
            self.ball.speed_y = - self.ball.speed_y
        self.ball.x += self.ball.speed_x
        self.ball.y += self.ball.speed_y

    def check_right_paddle(self):
        rect = pygame.Rect(self.right_paddle.x, self.right_paddle.y, Paddle.width, Paddle.height)
        if rect.collidepoint(self.ball.x + self.ball.radius, self.ball.y):
            self.ball.speed_x = - self.ball.speed_x
        self.ball.x += self.ball.speed_x
        self.ball.y += self.ball.speed_y

    def check_left_paddle(self):
        rect = pygame.Rect(self.left_paddle.x, self.left_paddle.y, Paddle.width, Paddle.height)
        if rect.collidepoint(self.ball.x - self.ball.radius, self.ball.y):
            self.ball.speed_x = - self.ball.speed_x
        self.ball.x += self.ball.speed_x
        self.ball.y += self.ball.speed_y

    def check_walls(self):
        if self.ball.x <= 0 + self.ball.radius:
            self.score2 += 1
            if self.score2 > self.rec2:
                self.rec2 += 1
            self.ball = Ball(WIDTH, HEIGHT, 15)
        elif self.ball.x >= WIDTH - self.ball.radius:
            self.score1 += 1
            if self.score1 > self.rec1:
                self.rec1 += 1
            self.ball = Ball(WIDTH, HEIGHT, 15)

    def handle_menu(self):
        self.menu.show(self)

    def handle_pause(self):
        self.pause.show(self)

    def game_over(self):
        self.state = GameState.GameOver

    def quit(self):
        # НЕ СОХРАНЯЕТСЯ РЕКОРД ПОСЛЕ ВЫХОДА ИЗ ИГРЫ
        self.database.store({"Player1": self.rec1, "Player2": self.rec2})
        self.running = False

    def reset(self):
        self.screen = Screen()
        self.ball = Ball(WIDTH, HEIGHT, 15)
        self.left_paddle = Paddle(100 - Paddle.width / 2,
                                  HEIGHT / 2 - Paddle.height / 2)
        self.right_paddle = Paddle(WIDTH - (100 - Paddle.width / 2),
                                   HEIGHT / 2 - Paddle.height / 2)
        self.state = GameState.Menu
        self.score1 = 0
        self.score2 = 0
        self.speed = 10


