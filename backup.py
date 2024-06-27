import random
import pygame, sys
from pygame import QUIT, Vector2 as Vector2


class game:
    def __init__(self):
        pygame.init()

        # Game variable
        self.resoultion = 625
        self.screen = pygame.display.set_mode((self.resoultion, self.resoultion))
        self.clock = pygame.time.Clock()
        self.cell_size = 25
        # self.game_state = "Playing" # the other one is "GameOver"

        # Snake
        self.body = [
            Vector2(20, 20),
            Vector2(20, 21),
            Vector2(20, 22),
            Vector2(20, 23),
            Vector2(20, 24),
            Vector2(20, 25),
            Vector2(20, 26),
            Vector2(20, 27),
        ]
        self.direction = Vector2(0, -1)

        # Fruit
        self.fruit = Vector2(1, 1)
        self.fruit_eaten = False

        # Logs_Data
        self.moves = 0
        self.score = 0

    def end_game(self):
        pass

    def fruit_spawn(self):
        self.fruit_eaten = False
        while True:
            loc = Vector2(
                random.randint(0, self.resoultion // self.cell_size - 1),
                random.randint(0, self.resoultion // self.cell_size - 1),
            )
            if loc not in self.body:
                self.fruit = loc
                break

    def snake_move(self):
        self.moves += 1
        # check if the fruit is eaten
        if self.body[0] + self.direction == self.fruit:
            self.score += 1
            self.fruit_eaten = True

        # check for collision
        if (
            0 > (self.body[0] + self.direction).x
            or (self.body[0] + self.direction).x > self.resoultion // self.cell_size
            or 0 > (self.body[0] + self.direction).y
            or (self.body[0] + self.direction).y > self.resoultion // self.cell_size
            or (self.body[0] + self.direction) in self.body
        ):
            pygame.quit()

        # Snake movement
        if self.fruit_eaten:
            body = [self.body[0] + self.direction]
            body.extend(self.body)
            self.body = body
            self.fruit_spawn()
        else:
            body = [self.body[0] + self.direction]
            body.extend(self.body[:-1])
            self.body = body

    def snake_render(self):
        # Render the fruit
        pygame.draw.circle(
            self.screen,
            (0, 130, 0),
            (
                self.fruit.x * self.cell_size + self.cell_size // 2,
                self.fruit.y * self.cell_size + self.cell_size // 2,
            ),
            self.cell_size // 2 - 1,
        )

        # Render grid lines
        for i in range(self.resoultion // self.cell_size):
            rect_hor = pygame.Rect(0, i * self.cell_size, self.resoultion, 1)
            pygame.draw.rect(self.screen, (40, 40, 40), rect_hor)
            rect_ver = pygame.Rect(i * self.cell_size, 0, 1, self.resoultion)
            pygame.draw.rect(self.screen, (40, 40, 40), rect_ver)

        # Render Snake
        # for i in self.body:
        #     rect = pygame.Rect(i.x*self.cell_size,i.y*self.cell_size, self.cell_size,self.cell_size )
        #     pygame.draw.rect(self.screen,(200,0,0),rect)
        padding = 2
        border_radius = 4

        # Head
        # Up
        # if self.direction == Vector2(0, -1) and self.body[1].x == self.body[0].x:
        #     rect = pygame.Rect(
        #         self.body[0].x * self.cell_size + padding,
        #         self.body[0].y * self.cell_size,
        #         self.cell_size - padding * 2,
        #         self.cell_size,
        #     )
        #     pygame.draw.rect(
        #         self.screen,
        #         (200, 0, 0),
        #         rect,
        #         border_top_left_radius=border_radius,
        #         border_top_right_radius=border_radius,
        #     )
        #
        # # Down
        # if self.direction == Vector2(0, 1) and self.body[1].x == self.body[0].x:
        #     rect = pygame.Rect(
        #         self.body[0].x * self.cell_size + padding,
        #         self.body[0].y * self.cell_size,
        #         self.cell_size - padding * 2,
        #         self.cell_size,
        #     )
        #     pygame.draw.rect(
        #         self.screen,
        #         (200, 0, 0),
        #         rect,
        #         border_bottom_left_radius=border_radius,
        #         border_bottom_right_radius=border_radius,
        #     )
        #
        # Moving Vertically

        # This is redundent code.
        # Right with no body to the back
        # if (
        #     self.direction == Vector2(1, 0)
        #     and (self.body[0] + Vector2(-1, 0)) != self.body[1]
        # ):
        #     rect = pygame.Rect(
        #         self.body[0].x * self.cell_size + padding,
        #         self.body[0].y * self.cell_size + padding,
        #         self.cell_size - padding,
        #         self.cell_size - padding * 2,
        #     )
        #     pygame.draw.rect(
        #         self.screen,
        #         (200, 0, 0),
        #         rect,
        #         border_top_left_radius=border_radius,
        #         border_top_right_radius=border_radius,
        #         border_bottom_right_radius=border_radius,
        #     )
        #
        # # Left with no body on the back
        # if self.direction == Vector2(-1, 0) and (
        #     self.body[0] + Vector2(1, 0) != self.body[1]
        # ):
        #     rect = pygame.Rect(
        #         self.body[0].x * self.cell_size,
        #         self.body[0].y * self.cell_size + padding,
        #         self.cell_size - padding,
        #         self.cell_size - padding * 2,
        #     )
        #     pygame.draw.rect(
        #         self.screen,
        #         (200, 0, 0),
        #         rect,
        #         border_top_left_radius=border_radius,
        #         border_top_right_radius=border_radius,
        #         border_bottom_left_radius=border_radius,
        #     )
        #

        # This part starts the FuckUp
        # Right with body on the back going Up
        if (
            self.direction == Vector2(1, 0)
            and self.body[1].x == self.body[0].x
            and self.body[0].y == self.body[1].y - 1
        ):
            rect = pygame.Rect(
                self.body[0].x * self.cell_size + padding,
                self.body[0].y * self.cell_size + padding,
                self.cell_size - padding,
                self.cell_size - padding,
            )
            pygame.draw.rect(
                self.screen,
                (200, 0, 0),
                rect,
                border_top_right_radius=border_radius,
                border_bottom_right_radius=border_radius,
            )
        # Left with body on the back going Up
        elif (
            self.direction == Vector2(-1, 0)
            and self.body[0].x == self.body[1].x
            and self.body[0].y == self.body[1].y - 1
        ):
            rect = pygame.Rect(
                self.body[0].x * self.cell_size,
                self.body[0].y * self.cell_size + padding,
                self.cell_size - padding,
                self.cell_size,
            )
            pygame.draw.rect(
                self.screen,
                (200, 0, 0),
                rect,
                border_top_left_radius=border_radius,
                border_bottom_left_radius=border_radius,
            )

        elif (  # Correct conditions
            self.direction == Vector2(1, 0)
            and self.body[1].x == self.body[0].x
            and self.body[1].y + 1 == self.body[0].y
        ):
            rect = pygame.Rect(
                self.body[0].x * self.cell_size + padding,
                self.body[0].y * self.cell_size,
                self.cell_size - padding,
                self.cell_size,
            )
            pygame.draw.rect(
                self.screen,
                (200, 0, 0),
                rect,
                border_top_right_radius=border_radius,
                border_bottom_right_radius=border_radius,
            )

            # Going straight Right
        elif self.direction == Vector2(1, 0):
            rect = pygame.Rect(
                self.body[0].x * self.cell_size,
                self.body[0].y * self.cell_size + padding,
                self.cell_size,
                self.cell_size - padding * 2,
            )
            pygame.draw.rect(
                self.screen,
                (200, 0, 0),
                rect,
                border_top_right_radius=border_radius,
                border_bottom_right_radius=border_radius,
            )
            # Left with body on the back going Down
        # Tested works fine
        elif (
            self.direction == Vector2(-1, 0)
            and self.body[0].x == self.body[1].x
            and self.body[0].y == self.body[1].y + 1
        ):
            rect = pygame.Rect(
                self.body[0].x * self.cell_size,
                self.body[0].y * self.cell_size,
                self.cell_size - padding,
                self.cell_size - padding,
            )
            pygame.draw.rect(
                self.screen,
                (200, 0, 0),
                rect,
                border_top_left_radius=border_radius,
                border_bottom_left_radius=border_radius,
            )
        elif self.direction == Vector2(-1, 0):
            rect = pygame.Rect(
                self.body[0].x * self.cell_size + padding,
                self.body[0].y * self.cell_size + padding,
                self.cell_size - padding,
                self.cell_size - padding * 2,
            )
            pygame.draw.rect(
                self.screen,
                (200, 0, 0),
                rect,
                border_top_left_radius=border_radius,
                border_bottom_left_radius=border_radius,
            )

        #
        # Right with body on the back going Down
        # Vertical movements
        # Up with body on the back going Right
        if (
            self.direction == Vector2(0, -1)
            and self.body[1].x + 1 == self.body[0].x
            and self.body[0].y == self.body[1].y
        ):
            rect = pygame.Rect(
                self.body[0].x * self.cell_size,
                self.body[0].y * self.cell_size,
                self.cell_size - padding,
                self.cell_size - padding,
            )
            pygame.draw.rect(
                self.screen,
                (200, 0, 0),
                rect,
                border_top_right_radius=border_radius,
                border_top_left_radius=border_radius,
            )
            # Up with body on the back going Left
        elif (
            self.direction == Vector2(0, -1)
            and self.body[1].x - 1 == self.body[0].x
            and self.body[0].y == self.body[1].y
        ):
            rect = pygame.Rect(
                self.body[0].x * self.cell_size + padding,
                self.body[0].y * self.cell_size,
                self.cell_size - padding,
                self.cell_size - padding,
            )
            pygame.draw.rect(
                self.screen,
                (200, 0, 0),
                rect,
                border_top_right_radius=border_radius,
                border_top_left_radius=border_radius,
            )
        elif self.direction == Vector2(0, -1):
            rect = pygame.Rect(
                self.body[0].x * self.cell_size + padding,
                self.body[0].y * self.cell_size + padding,
                self.cell_size - padding * 2,
                self.cell_size,
            )
            pygame.draw.rect(
                self.screen,
                (200, 0, 0),
                rect,
                border_top_right_radius=border_radius,
                border_top_left_radius=border_radius,
            )

        # Down with body on the back going Rigth
        if (
            self.direction == Vector2(0, 1)
            and self.body[1].x + 1 == self.body[0].x
            and self.body[1].y == self.body[0].y
        ):
            rect = pygame.Rect(
                self.body[0].x * self.cell_size,
                self.body[0].y * self.cell_size + padding,
                self.cell_size - padding,
                self.cell_size - padding,
            )
            pygame.draw.rect(
                self.screen,
                (200, 0, 0),
                rect,
                border_bottom_right_radius=border_radius,
                border_bottom_left_radius=border_radius,
            )
            # Down with body on the back going Left
        elif (
            self.direction == Vector2(0, 1)
            and self.body[0].x + 1 == self.body[1].x
            and self.body[0].y == self.body[1].y
        ):
            rect = pygame.Rect(
                self.body[0].x * self.cell_size + padding,
                self.body[0].y * self.cell_size + padding,
                self.cell_size - padding,
                self.cell_size - padding,
            )
            pygame.draw.rect(
                self.screen,
                (200, 0, 0),
                rect,
                border_bottom_left_radius=border_radius,
                border_bottom_right_radius=border_radius,
            )
        elif self.direction == Vector2(0, 1):
            rect = pygame.Rect(
                self.body[0].x * self.cell_size + padding,
                self.body[0].y * self.cell_size,
                self.cell_size - padding * 2,
                self.cell_size,
            )
            pygame.draw.rect(
                self.screen,
                (200, 0, 0),
                rect,
                border_bottom_left_radius=border_radius,
                border_bottom_right_radius=border_radius,
            )

        # Body
        for i in range(1, len(self.body) - 1):

            # Vertical straight line
            if self.body[i].x == self.body[i - 1].x == self.body[i + 1].x:
                rect = pygame.Rect(
                    self.body[i].x * self.cell_size + padding,
                    self.body[i].y * self.cell_size,
                    self.cell_size - padding * 2,
                    self.cell_size,
                )
                pygame.draw.rect(self.screen, (200, 0, 0), rect)

            # Horizontal straight line
            if self.body[i].y == self.body[i - 1].y == self.body[i + 1].y:
                rect = pygame.Rect(
                    self.body[i].x * self.cell_size,
                    self.body[i].y * self.cell_size + padding,
                    self.cell_size,
                    self.cell_size - padding * 2,
                )
                pygame.draw.rect(self.screen, (200, 0, 0), rect)

            # When going Vertical
            # Right Upwards Turn
            if (
                self.body[i].y == self.body[i - 1].y
                and self.body[i].x + 1 == self.body[i - 1].x
                and self.body[i].x == self.body[i + 1].x
                and self.body[i].y + 1 == self.body[i + 1].y
            ):
                rect = pygame.Rect(
                    self.body[i].x * self.cell_size + padding,
                    self.body[i].y * self.cell_size + padding,
                    self.cell_size,
                    self.cell_size - padding,
                )
                pygame.draw.rect(self.screen, (200, 0, 0), rect)
            # Left Upwards Turn
            if (
                self.body[i].y == self.body[i - 1].y
                and self.body[i].x - 1 == self.body[i - 1].x
                and self.body[i].x == self.body[i + 1].x
                and self.body[i].y + 1 == self.body[i + 1].y
            ):
                rect = pygame.Rect(
                    self.body[i].x * self.cell_size,
                    self.body[i].y * self.cell_size + padding,
                    self.cell_size - padding,
                    self.cell_size,
                )
                pygame.draw.rect(self.screen, (200, 0, 0), rect)

            # Right Downward Turn
            if (
                self.body[i].y == self.body[i - 1].y
                and self.body[i].x + 1 == self.body[i - 1].x
                and self.body[i].x == self.body[i + 1].x
                and self.body[i].y - 1 == self.body[i + 1].y
            ):
                rect = pygame.Rect(
                    self.body[i].x * self.cell_size + padding,
                    self.body[i].y * self.cell_size,
                    self.cell_size - padding,
                    self.cell_size - padding,
                )
                pygame.draw.rect(self.screen, (200, 0, 0), rect)

            # Left Downwards Turn
            if (
                self.body[i].y == self.body[i - 1].y
                and self.body[i].x - 1 == self.body[i - 1].x
                and self.body[i].x == self.body[i + 1].x
                and self.body[i].y - 1 == self.body[i + 1].y
            ):
                rect = pygame.Rect(
                    self.body[i].x * self.cell_size,
                    self.body[i].y * self.cell_size,
                    self.cell_size - padding,
                    self.cell_size - padding,
                )
                pygame.draw.rect(self.screen, (200, 0, 0), rect)

            # When going Horizontal
            # Right Upwards Turn
            if (
                self.body[i].y - 1 == self.body[i - 1].y
                and self.body[i].x == self.body[i - 1].x
                and self.body[i].x + 1 == self.body[i + 1].x
                and self.body[i].y == self.body[i + 1].y
            ):
                rect = pygame.Rect(
                    self.body[i].x * self.cell_size + padding,
                    self.body[i].y * self.cell_size,
                    self.cell_size - padding,
                    self.cell_size - padding,
                )
                pygame.draw.rect(self.screen, (200, 0, 0), rect)
            # Left Upwards Turn
            if (
                self.body[i].y - 1 == self.body[i - 1].y
                and self.body[i].x == self.body[i - 1].x
                and self.body[i].x - 1 == self.body[i + 1].x
                and self.body[i].y == self.body[i + 1].y
            ):
                rect = pygame.Rect(
                    self.body[i].x * self.cell_size,
                    self.body[i].y * self.cell_size,
                    self.cell_size - padding,
                    self.cell_size - padding,
                )
                pygame.draw.rect(self.screen, (200, 0, 0), rect)

            # Left Downward Turn
            if (
                self.body[i].y + 1 == self.body[i - 1].y
                and self.body[i].x == self.body[i - 1].x
                and self.body[i].x - 1 == self.body[i + 1].x
                and self.body[i].y == self.body[i + 1].y
            ):
                rect = pygame.Rect(
                    self.body[i].x * self.cell_size,
                    self.body[i].y * self.cell_size + padding,
                    self.cell_size - padding,
                    self.cell_size,
                )
                pygame.draw.rect(self.screen, (200, 0, 0), rect)

            # Right Downwards Turn
            if (
                self.body[i].y + 1 == self.body[i - 1].y
                and self.body[i].x == self.body[i - 1].x
                and self.body[i].x + 1 == self.body[i + 1].x
                and self.body[i].y == self.body[i + 1].y
            ):
                rect = pygame.Rect(
                    self.body[i].x * self.cell_size + padding,
                    self.body[i].y * self.cell_size + padding,
                    self.cell_size,
                    self.cell_size,
                )
                pygame.draw.rect(self.screen, (200, 0, 0), rect)

    def run(self):
        pygame.display.set_caption("Snake game")
        while True:
            self.screen.fill((0, 0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP and self.direction != Vector2(0, 1):
                        self.direction = Vector2(0, -1)
                    if event.key == pygame.K_DOWN and self.direction != Vector2(0, -1):
                        self.direction = Vector2(0, 1)
                    if event.key == pygame.K_LEFT and self.direction != Vector2(1, 0):
                        self.direction = Vector2(-1, 0)
                    if event.key == pygame.K_RIGHT and self.direction != Vector2(-1, 0):
                        self.direction = Vector2(1, 0)

            self.snake_render()
            self.snake_move()
            pygame.display.update()
            self.clock.tick(10)


game().run()
