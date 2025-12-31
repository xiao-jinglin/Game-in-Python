import pygame
import random

pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake")

BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

snake_block = 20
snake_head = [WIDTH // 2, HEIGHT // 2]

x_speed = 0
y_speed = 0 
block_speed = 20

snake_list = []
snake_length = 1
food_x = random.randrange(0, WIDTH - snake_block, snake_block)
food_y = random.randrange(0, HEIGHT - snake_block, snake_block)
score = 0

game_over = False

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a and x_speed != block_speed:
                x_speed = -block_speed
                y_speed = 0
            elif event.key == pygame.K_d and x_speed != -block_speed:
                x_speed = block_speed
                y_speed = 0
            elif event.key == pygame.K_w and y_speed != block_speed:
                x_speed = 0
                y_speed = -block_speed
            elif event.key == pygame.K_s and y_speed != -block_speed:
                x_speed = 0
                y_speed = block_speed
            elif event.key == pygame.K_SPACE and game_over:
                snake_head = [WIDTH // 2, HEIGHT // 2]
                x_speed = 0
                y_speed = 0
                snake_list = []
                snake_length = 1
                food_x = random.randrange(0, WIDTH - snake_block, snake_block)
                food_y = random.randrange(0, HEIGHT - snake_block, snake_block)
                score = 0
                game_over = False

    screen.fill(BLACK)
    
    if not game_over:
        snake_head[0] += x_speed
        snake_head[1] += y_speed

        if snake_head[0] >= WIDTH or snake_head[0] < 0 or snake_head[1] >= HEIGHT or snake_head[1] < 0:
            game_over = True
        for block in snake_list[:-1]:
            if block == snake_head:
                game_over = True
                break

        snake_head_copy = list(snake_head)
        snake_list.append(snake_head_copy)
        if len(snake_list) > snake_length:
            del snake_list[0]

        if snake_head[0] == food_x and snake_head[1] == food_y:
            snake_length += 1
            score += 1
            while True:
                food_x = random.randrange(0, WIDTH - snake_block, snake_block)
                food_y = random.randrange(0, HEIGHT - snake_block, snake_block)
                overlap = False
                for block in snake_list:
                    if block[0] == food_x and block[1] == food_y:
                        overlap = True
                        break
                if not overlap:
                    break

        
    for block in snake_list:
        pygame.draw.rect(screen, GREEN, (block[0], block[1], snake_block, snake_block))
        font = pygame.font.SysFont(None, 50)
        score_text = font.render("Score: " + str(score), True, WHITE)
        screen.blit(score_text, (10, 10))
    
    
    pygame.draw.rect(screen, RED, (food_x, food_y, snake_block, snake_block))
    if game_over:
        over_text = font.render("GAME OVER", True, WHITE)
        screen.blit(over_text, (WIDTH // 2 - 120, HEIGHT // 2 - 50))
        restart_text = font.render("Press SPACE to Restart", True, WHITE)
        screen.blit(restart_text, (100, HEIGHT // 2 ))
    pygame.display.flip()
    pygame.time.Clock().tick(10)
    
pygame.quit()