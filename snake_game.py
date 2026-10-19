import pygame
import random
import sys

#Configuration
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
CELL_SIZE = 20
GRID_WIDTH = WINDOW_WIDTH // CELL_SIZE
GRID_HEIGHT = WINDOW_HEIGHT // CELL_SIZE
FPS = 10 # Higher = faster snake

#Colors
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
DARK_GREEN = (0, 150, 0)
RED = (200, 0, 0)
WHITE = (255, 255, 255)
GRAY = (40, 40, 40)

#Directions
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

class SnakeGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Snake Game")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("arial", 28, bold=True)
        self.big_font = pygame.font.SysFont("arial", 48, bold=True)
        self.reset()

    def reset(self):
        """Reset the game to its starting state."""
        mid_x, mid_y = GRID_WIDTH // 2, GRID_HEIGHT // 2
        self.snake = [(mid_x, mid_y), (mid_x - 1, mid_y), (mid_x - 2, mid_y)]
        self.direction = RIGHT
        self.next_direction = RIGHT
        self.food = self.spawn_food()
        self.score = 0
        self.game_over = False

    def spawn_food(self):
        """Place food on a random empty cell."""
        while True:
            pos = (random.randint(0, GRID_WIDTH - 1),
                   random.randint(0, GRID_HEIGHT - 1))
            if pos not in self.snake:
                return pos

    def handle_input(self):
        """Process key presses and window events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if self.game_over:
                    if event.key == pygame.K_RETURN:
                        self.reset()
                    elif event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                else:
                    if event.key in (pygame.K_UP, pygame.K_w):
                        if self.direction != DOWN:
                            self.next_direction = UP
                    elif event.key in (pygame.K_DOWN, pygame.K_s):
                        if self.direction != UP:
                            self.next_direction = DOWN
                    elif event.key in (pygame.K_LEFT, pygame.K_a):
                        if self.direction != RIGHT:
                            self.next_direction = LEFT
                    elif event.key in (pygame.K_RIGHT, pygame.K_d):
                        if self.direction != LEFT:
                            self.next_direction = RIGHT

    def update(self):
        """Advance the game by one step."""
        if self.game_over:
            return

        self.direction = self.next_direction
        head_x, head_y = self.snake[0]
        new_head = (head_x + self.direction[0], head_y + self.direction[1])

        #wall collision
        if not (0 <= new_head[0] < GRID_WIDTH and 0 <= new_head[1] < GRID_HEIGHT):
            self.game_over = True
            return

        #self collision
        if new_head in self.snake:
            self.game_over = True
            return

        #move the snake: add new head first
        self.snake.insert(0, new_head)

        #eating food
        if new_head == self.food:
            self.score += 1
            self.food = self.spawn_food()
        else:
            self.snake.pop()

    def draw(self):
        self.screen.fill(BLACK)

        #Draw grid lines
        for x in range(0, WINDOW_WIDTH, CELL_SIZE):
            pygame.draw.line(self.screen, GRAY, (x,0), (x, WINDOW_HEIGHT))
        for y in range(0, WINDOW_HEIGHT, CELL_SIZE):
            pygame.draw.line(self.screen, GRAY, (0, y), (WINDOW_WIDTH, y))

        #draw food
        fx, fy = self.food
        pygame.draw.rect(self.screen, RED,
                         (fx * CELL_SIZE, fy * CELL_SIZE, CELL_SIZE, CELL_SIZE))

        #Draw snake
        for i, (x, y) in enumerate(self.snake):
            color = GREEN if i == 0 else DARK_GREEN
            pygame.draw.rect(self.screen, color,
                             (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

        #Draw score
        score_text = self.font.render(f"Score: {self.score}", True, WHITE)
        self.screen.blit(score_text, (10, 10))

        #Draw game-over overlay
        if self.game_over:
            overlay = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
            overlay.set_alpha(180)
            overlay.fill(BLACK)
            self.screen.blit(overlay, (0,0))

            over_text = self.big_font.render("GAME OVER", True, RED)
            score_display = self.font.render(f"Final score: {self.score}", True, WHITE)
            restart_text = self.font.render("Press ENTER to restart, ESC to quit", True, WHITE)

            self.screen.blit(over_text, (WINDOW_WIDTH // 2 - over_text.get_width() // 2, 220))
            self.screen.blit(score_display, (WINDOW_WIDTH // 2 - score_display.get_width() // 2, 290))
            self.screen.blit(restart_text, (WINDOW_WIDTH // 2 - restart_text.get_width() // 2, 340))

        pygame.display.flip()

    def run(self):
        while True:
            self.handle_input()
            self.update()
            self.draw()
            self.clock.tick(FPS)

if __name__ == "__main__":
    SnakeGame().run()

