from game import Game
from pygame import Vector2 as Vector2


class Bfs(Game):
    # def __init__(self) -> None:
    #     super().__init__()

    def right_90_top(self):
        if self.body[0].y == 0 and self.direction == Vector2(0, -1):
            self.direction = Vector2(1, 0)
            self.snake_move()
            return

        elif self.body[0].y == 0 and self.direction == Vector2(1, 0):
            self.direction = Vector2(0, 1)
            self.snake_move()
            return

    def bfs_play(self):
        if self.body[0].y == 0 and self.direction == Vector2(0, -1):
            self.direction = Vector2(1, 0)
            self.snake_move()
            return

        elif self.body[0].y == 0 and self.direction == Vector2(1, 0):
            self.direction = Vector2(0, 1)
            self.snake_move()
            return

        if self.body[0].y == self.grid_len and self.body[0].x == self.grid_len:
            self.direction = Vector2(-1, 0)
            self.snake_move()
            return
        elif self.body[0].y == self.grid_len and self.body[0].x == 0:
            self.direction = Vector2(0, -1)
            self.snake_move()
            return

        elif (
            self.body[0].y == self.grid_len - 1
            and self.direction == Vector2(0, 1)
            and self.body[0].x != self.grid_len
        ):
            self.direction = Vector2(1, 0)
            self.snake_move()
            return

        elif (
            self.body[0].y == self.grid_len - 1
            and self.direction == Vector2(1, 0)
            and self.body[0].x != self.grid_len
        ):
            self.direction = Vector2(0, -1)
            self.snake_move()
            return

        self.snake_move()

    def Bfs(self):
        pass
