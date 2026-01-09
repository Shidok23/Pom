import pygame
import random

pygame.init()

WIDTH, HEIGHT = 1980, 1080
CELL = 20

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Змейка")
clock = pygame.time.Clock()

def new_food(snake_cells):
    while True:
        x = random.randint(0, (WIDTH // CELL) - 1) * CELL
        y = random.randint(0, (HEIGHT // CELL) - 1) * CELL
        if (x, y) not in snake_cells:
            return x, y

running = True
game_over = False

snake = [(200, 140), (180, 140), (160, 140)]
prev_snake = snake.copy()
dx = 0
dy = 0
grow = 0

food_x, food_y = new_food(snake)

move_delay = 200
last_move_time = pygame.time.get_ticks()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_LEFT and dx != CELL:
                dx, dy = -CELL, 0
            elif event.key == pygame.K_RIGHT and dx != -CELL:
                dx, dy = CELL, 0
            elif event.key == pygame.K_UP and dy != CELL:
                dx, dy = 0, -CELL
            elif event.key == pygame.K_DOWN and dy != -CELL:
                dx, dy = 0, CELL

    now = pygame.time.get_ticks()
    if (not game_over) and (now - last_move_time >= move_delay):
        last_move_time = now

        if dx != 0 or dy != 0:
            head_x, head_y = snake[0]
            new_head = (head_x + dx, head_y + dy)

            if new_head[0] < 0 or new_head[0] >= WIDTH or new_head[1] < 0 or new_head[1] >= HEIGHT:
                game_over = True
            else:
                if new_head in snake:
                    game_over = True
                else:
                    snake.insert(0, new_head)

                    if snake[0] == (food_x, food_y):
                        food_x, food_y = new_food(snake)
                        grow += 1

                    if grow > 0:
                        grow -= 1
                    else:
                        snake.pop()

    screen.fill((0, 150, 0))
    pygame.draw.rect(screen, (200, 0, 0), (food_x, food_y, CELL, CELL))

    for x, y in snake:
        pygame.draw.rect(screen, (0, 0, 0), (x, y, CELL, CELL))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
