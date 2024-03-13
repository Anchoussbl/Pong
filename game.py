from ball import *
from screen import *
from paddle import *
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
        self.screen = Screen()
        self.ball = Ball()
        self.paddle = Paddle()
        self.menu = Menu()
        self.pause = Pause()
        self.record = Record()
        self.gameover = GameOver()
        self.state = GameState.Menu
        # self.database = DataBase()
        self.score1 = 0
        self.score2 = 0
        # self.rec = self.database.load()["Player1"]

    def run(self):
        while self.running:
            # for the inputs
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if self.state == GameState.Running:
                        if event.key == pygame.K_UP:
                            self.paddle_vel = -0.7
                        if event.key == pygame.K_DOWN:
                            self.paddle_vel = 0.7
                        if event.key == pygame.K_w:
                            self.paddle_vel1 = -0.7
                        if event.key == pygame.K_s:
                            self.paddle_vel1 = 0.7
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
                    self.paddle_vel = 0
                    self.paddle_vel1 = 0

            if self.state == GameState.Running:
                self.screen.reset()
                self.screen.draw_ball()
                self.screen.draw_paddles()
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
        self.ball = Ball()
        self.paddle = Paddle()
        self.menu = Menu()
        self.pause = Pause()
        self.record = Record()
        self.gameover = GameOver()
        self.state = GameState.Menu
        self.score1 = 0
        self.score2 = 0




    # gadget movement controls
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
    # # raw movements
    # paddle_y += paddle_vel
    # paddle_y1 += paddle_vel1
    # ball_x += vel_x
    # ball_y += vel_y




