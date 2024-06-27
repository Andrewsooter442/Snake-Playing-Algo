import random
import pygame
from pygame import Vector2 as Vector2


class Game:
    def __init__(self):
        pygame.init()

        # Game variable
        self.resoultion = 650
        self.screen = pygame.display.set_mode((self.resoultion, self.resoultion))
        self.clock = pygame.time.Clock()
        self.cell_size = 25
        self.grid_len = self.resoultion // self.cell_size - 1
        self.playmethod = None
        # self.game_state = "Playing" # the other one is "GameOver"

        # Snake
        self.body = [
            Vector2(0, self.grid_len - 1),
            Vector2(0, self.grid_len),
        ]
        self.direction = Vector2(0, -1)

        # Fruit
        self.fruit = Vector2(1, 1)
        self.fruit_eaten = False

        # Logs_Data
        self.moves = 0
        self.score = 0

    def set_playmethod(self, method: str):
        self.playmethod = method

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
        padding = 2
        border_radius = 4

        # Moving Vertically
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
        # Horizontal movements
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

        # Body Render
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
