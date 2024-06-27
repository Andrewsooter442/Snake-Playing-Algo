from bfs import Bfs
import pygame, sys
from pygame import Vector2 as Vector2


class Run(Bfs):

    def run_game(self):
        pygame.display.set_caption("Snake game")
        while True:
            self.screen.fill((0, 0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN and self.playmethod == "Manual":
                    if event.key == pygame.K_UP and self.direction != Vector2(0, 1):
                        self.direction = Vector2(0, -1)
                    if event.key == pygame.K_DOWN and self.direction != Vector2(0, -1):
                        self.direction = Vector2(0, 1)
                    if event.key == pygame.K_LEFT and self.direction != Vector2(1, 0):
                        self.direction = Vector2(-1, 0)
                    if event.key == pygame.K_RIGHT and self.direction != Vector2(-1, 0):
                        self.direction = Vector2(1, 0)

            if self.playmethod == "Manual":
                self.snake_move()
            else:
                self.bfs_play()

            self.snake_render()
            pygame.display.update()
            self.clock.tick()


game = Run()
game.set_playmethod("auto")
game.run_game()
