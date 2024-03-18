from ball import *
from screen import *
from constants import *
from menu import *
from pause import *
from record import *
from gameover import *
from game_state import *
# from database import *


class Game:
    running = True

    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.reset()

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
                        # ускорение мячика
                        # if event.key == pygame.K_RIGHT and g_left > 0:
                        #     self.gad = 1
                        # if event.key == pygame.K_d and G_left > 0:
                        #     self.act = 1
                        if event.key == pygame.K_ESCAPE:
                            self.state = GameState.Pause
                    elif self.state == GameState.Menu:
                        self.menu.handle_press(self, event.key)
                    elif self.state == GameState.Pause:
                        self.pause.handle_press(self, event.key)
                    elif self.state == GameState.Record:
                        self.record.handle_press(self, event.key)
                    elif self.state == GameState.GameOver:
                        self.gameover.handle_press(self, event.key)

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
                # self.screen.draw_text(str("record: {}".format(self.rec)), x=80, y=10)
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
            elif self.state == GameState.GameOver:
                # show game over
                self.gameover.show(self)

        if not self.running:
            self.game_over()

    def tick(self):
        self.handle_movement()

    def handle_movement(self):
        self.left_paddle.move()
        self.right_paddle.move()
        # ball's movement controls
        # if (ball_y <= 0 + radius) or (ball_y >= HEIGHT - radius):
        #     vel_y *= -1
        # if ball_x >= WIDTH - radius:
        #     ball_x = WIDTH / 2 - radius
        #     ball_y = HEIGHT / 2 - radius
        #     vel_x = 0.5
        #     vel_y = 0.5
        #     vel_x *= -1
        # if ball_x <= 0 + radius:
        #     ball_x = WIDTH / 2 - radius
        #     ball_y = HEIGHT / 2 - radius
        #     vel_x = 0.5
        #     vel_y = 0.5
        #
        #     # paddle's movement controls
        # if paddle_y >= HEIGHT - paddle_height:
        #     paddle_y = HEIGHT - paddle_height
        # if paddle_y <= 0:
        #     paddle_y = 0
        # if paddle_y1 >= HEIGHT - paddle_height:
        #     paddle_y1 = HEIGHT - paddle_height
        # if paddle_y1 <= 0:
        #     paddle_y1 = 0
        #
        # if paddle_X <= ball_x <= paddle_X + paddle_width:
        #     if paddle_y <= ball_y <= paddle_y + paddle_height:
        #         ball_x = paddle_X
        #         vel_x *= -1
        #
        # if paddle_x <= ball_x <= paddle_x + paddle_width:
        #     if paddle_y1 <= ball_y <= paddle_y1 + paddle_height:
        #         ball_x = paddle_x + paddle_width
        #         vel_x *= -1
        #
        #         # gadget movement controls
        # if gad == 1:
        #     if paddle_X <= ball_x <= paddle_X + paddle_width:
        #         if paddle_y <= ball_y <= paddle_y + paddle_height:
        #             ball_x = paddle_X
        #             vel_x *= -3.5
        #             gad = 0
        #
        # if act == 1:
        #     if paddle_x <= ball_x <= paddle_x + paddle_width:
        #         if paddle_y1 <= ball_y <= paddle_y1 + paddle_height:
        #             ball_x = paddle_x + paddle_width
        #             vel_x *= -3.5
        #             act = 0
        #
        #             # raw movements
        # paddle_y += paddle_vel
        # paddle_y1 += paddle_vel1
        # ball_x += vel_x
        # ball_y += vel_y

    def handle_menu(self):
        self.menu.show(self)

    def handle_pause(self):
        self.pause.show(self)

    def game_over(self):
        self.state = GameState.GameOver

    def quit(self):
        # self.database.store({"Player1": self.rec})
        self.running = False

    def reset(self):
        self.screen = Screen()
        self.ball = Ball(WIDTH, HEIGHT, 15)
        self.left_paddle = Paddle(100 - Paddle.width / 2,
                                  HEIGHT / 2 - Paddle.height / 2)
        self.right_paddle = Paddle(WIDTH - (100 - Paddle.width / 2),
                                   HEIGHT / 2 - Paddle.height / 2)
        self.menu = Menu()
        self.pause = Pause()
        self.record = Record()
        self.gameover = GameOver()
        self.state = GameState.Menu
        self.speed = 1
        self.score1 = 0
        self.score2 = 0




