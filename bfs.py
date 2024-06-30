from re import VERBOSE
from game import Game
from pygame import Vector2 as Vector2


class Bfs(Game):
    # def __init__(self) -> None:
    #     super().__init__()

    # Turn right on row y = 0
    def right_90_top(self):
        if self.body[0].y == 0 and self.direction == Vector2(0, -1):
            self.direction = Vector2(1, 0)
            self.snake_move()
            return

        elif self.body[0].y == 0 and self.direction == Vector2(1, 0):
            self.direction = Vector2(0, 1)
            self.snake_move()
            return

    def can_cut(self):
        # check if snake can jump from last row and cut the board without eating itself
        if self.body[0].y == self.grid_len and Vector2(self.body[0].x, 0) in self.body:
            if (
                Vector2(self.body[0].x, 0)
                in self.body[: len(self.body) - self.grid_len]
            ):
                return False
        if self.body[0].y == self.grid_len:
            for i in range(1, self.grid_len):
                if (
                    Vector2(self.body[0].x, self.grid_len - i)
                    in self.body[: len(self.body) - i - 1]
                ):
                    return False

        # check if the snake can take a right turn without killing itself
        if (
            self.direction == Vector2(0, 1)
            and Vector2(self.body[0].x, self.fruit.y - (int(self.fruit.y % 2) ^ 0))
            in self.body
        ):
            if (
                Vector2(self.body[0].x + 1, 0)
                in self.body
                # in self.body[: len(self.body) - (self.fruit.x - self.body[0].x)]
            ):
                return False

        if self.direction == Vector2(0, 1) and (
            Vector2(self.body[0].x + 1, self.body[0].y) in self.body
            or Vector2(self.body[0].x + 2, self.body[0].y) in self.body
        ):
            return False

        # check if the snake can continue on first row (y==0) without cannibalising itself
        if (
            self.body[0].y == 0
            and Vector2(0, self.fruit.y - (int(self.fruit.y % 2) ^ 0)) in self.body
        ):
            if (
                Vector2(self.body[0].x + 1, 0)
                in self.body
                # in self.body[: len(self.body) - (self.fruit.x - self.body[0].x)]
            ):
                return False
        if self.body[0].y == 0 and Vector2(self.body[0].x + 1, 0) in self.body:
            return False
        return True

    def smart_play(self):
        # it's a bug but i can't fucking find it so just another edge case
        # when the fruit spawns on the right next coloum the snake fucksup
        if (
            self.direction == Vector2(0, 1)
            and self.body[0].x == self.fruit.x - 1
            and self.body[0].y >= self.fruit.y
            and self.can_cut()
        ):
            self.direction = Vector2(1, 0)
            self.snake_move()
            return

        # Edge case when fruit is on an even coloum test is before all other
        if self.direction == Vector2(1, 0) and self.body[0].y != 0:
            self.direction = Vector2(0, -1)
            self.snake_move()
            return

        if (
            self.fruit.x % 2 == 0
            and self.fruit.x - 1 == self.body[0].x
            and self.direction == Vector2(0, 1)
        ):
            if self.fruit.y == self.body[0].y:
                self.direction = Vector2(1, 0)
                self.snake_move()
                return
            else:
                self.snake_move()
                return

        # If fruit is on a even coloum

        # Whether to cut the board and get the apple
        if (
            self.body[0].y == self.grid_len
            and self.fruit.x % 2 == 0
            and self.body[0].x == self.fruit.x
            # and Vector2(self.body[0].x, 0)
            # not in self.body[: len(self.body) - self.grid_len]
            # not in self.body
            and self.can_cut()
        ):
            self.direction = Vector2(0, -1)
            self.snake_move()
            return
        # If fruit is on a odd coloum
        elif (
            self.body[0].y == self.grid_len
            and self.fruit.x % 2 != 0
            and self.body[0].x == self.fruit.x - 1
            # and Vector2(self.body[0].x, 0)
            # not in self.body[: len(self.body) - self.grid_len]
            # not in self.body
            and self.can_cut()
        ):
            self.direction = Vector2(0, -1)
            self.snake_move()
            return

        # If fruit spawns on left decide wethere to cut the board
        if self.fruit.x < self.body[0].x:
            # Turn left of the last row if there is no body
            if (
                self.body[0].y == self.grid_len - 1
                and Vector2(self.body[0].x, self.grid_len) not in self.body
            ):
                self.snake_move()
                return

            if self.body[0].y == self.grid_len and self.direction == Vector2(0, 1):
                self.direction = Vector2(-1, 0)
                self.snake_move()
                return
        # When fruit is on Right
        if self.fruit.x > self.body[0].x:
            # if Snake is going down go to the row y=0
            if (
                self.direction == Vector2(1, 0)
                and self.body[0].y == 0
                and self.can_cut()
            ):
                self.snake_move()
                return

            if (
                self.direction == Vector2(0, 1)
                and self.can_cut()
                and self.fruit.x - 1 != self.body[0].x
            ):
                self.direction = Vector2(1, 0)
                self.snake_move()
                return
                # If fruit is on an even coloum ie. going up coloum
            if self.fruit.x % 2 == 0:
                if (
                    self.direction == Vector2(1, 0)
                    and self.body[0].y == 0
                    and self.body[0].x == self.fruit.x - 1
                ):
                    self.direction = Vector2(0, 1)
                    self.snake_move()
                    return
        self.play()

    def play(self):
        # Auto play on the hamiltonian path
        # When reach y=0 coloum turn right
        if self.body[0].y == 0 and self.direction == Vector2(0, -1):
            self.direction = Vector2(1, 0)
            self.snake_move()
            return

        # if on y = 0 coloum turn right and go down
        elif self.body[0].y == 0 and self.direction == Vector2(1, 0):
            self.direction = Vector2(0, 1)
            self.snake_move()
            return

        # When reach the last grid ie. bottom right corner Turn toward x=0 ie.Left
        if self.body[0].y == self.grid_len and self.direction == Vector2(0, 1):
            self.direction = Vector2(-1, 0)
            self.snake_move()
            return

        # When in y=last coloum and at x =0 turn toward the origin ie.right
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
