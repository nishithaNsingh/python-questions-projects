import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 640, 480
GRID_SIZE = 20
FPS = 5

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Snake class
class Snake:
    def __init__(self):
        self.length = 1
        self.positions = [((WIDTH // 2), (HEIGHT // 2))]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.color = RED

    def get_head_position(self):
        return self.positions[0]

    def update(self):
        current = self.get_head_position()
        x, y = self.direction
        new = (((current[0] + (x * GRID_SIZE)) % WIDTH), (current[1] + (y * GRID_SIZE)) % HEIGHT)
        if len(self.positions) > 2 and new in self.positions[2:]:
            self.reset()
        else:
            self.positions.insert(0, new)
            if len(self.positions) > self.length:
                self.positions.pop()

    def reset(self):
        self.length = 1
        self.positions = [((WIDTH // 2), (HEIGHT // 2))]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])

    def render(self, surface):
        for p in self.positions:
            pygame.draw.rect(surface, self.color, (p[0], p[1], GRID_SIZE, GRID_SIZE))

# Food class
class Food:
    def __init__(self):
        self.position = (0, 0)
        self.color = WHITE
        self.randomize_position()

    def randomize_position(self):
        self.position = (random.randint(0, (WIDTH // GRID_SIZE) - 1) * GRID_SIZE,
                         random.randint(0, (HEIGHT // GRID_SIZE) - 1) * GRID_SIZE)

    def render(self, surface):
        pygame.draw.rect(surface, self.color, (self.position[0], self.position[1], GRID_SIZE, GRID_SIZE))

# Directional constants
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Main function
def main():
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()

    snake = Snake()
    food = Food()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if snake.direction != DOWN:
                        snake.direction = UP
                elif event.key == pygame.K_DOWN:
                    if snake.direction != UP:
                        snake.direction = DOWN
                elif event.key == pygame.K_LEFT:
                    if snake.direction != RIGHT:
                        snake.direction = LEFT
                elif event.key == pygame.K_RIGHT:
                    if snake.direction != LEFT:
                        snake.direction = RIGHT

        snake.update()
        if snake.get_head_position() == food.position:
            snake.length += 1
            food.randomize_position()

        surface.fill(BLACK)
        snake.render(surface)
        food.render(surface)
        screen.blit(surface, (0, 0))
        pygame.display.update()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
