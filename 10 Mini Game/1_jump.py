import pygame
import random

pygame.init()

WIDTH = 600
HEIGHT = 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("跳跃小方块 - 最终版")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 100, 255)
RED = (255, 50, 50)  # 新增：蓄力时的颜色
GRAY = (150, 150, 150) 

player_x = 300
player_y = 310
player_size = 40
scroll = 0
player_speed = 5
game_active = True

# 字体初始化（用于显示死亡文字）
pygame.font.init()
FONT = pygame.font.SysFont("arial", 20)

# --- 跳跃与蓄力变量 ---
jump = False
gravity = 0.5
y_speed = 0
ground_y = 310

is_charging = False    # 是否正在蓄力
charge_power = 0       # 当前蓄力值
MAX_CHARGE = 15        # 最大额外动力（加上基础跳跃力，总跳跃高度限制）
CHARGE_SPEED = 0.2     # 蓄力增加的速度

obstacles = [800, 1300, 1800] 
obs_width = 30
obs_height = 50

def reset_game():
    global scroll, player_y, y_speed, jump, is_charging, charge_power, obstacles, game_active
    scroll = 0
    player_y = 310
    y_speed = 0
    jump = False
    is_charging = False
    charge_power = 0
    obstacles = [800, 1300, 1800]
    game_active = True

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if game_active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not jump:
                    is_charging = True
                    charge_power = 0
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE and is_charging:
                    jump = True
                    is_charging = False
                    y_speed = -(8 + charge_power)
        else:
            # --- 死亡后按 R 重启 ---
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                reset_game()
    # 3. 左右移动逻辑

    if game_active:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            scroll += player_speed
        if keys[pygame.K_a]:
            scroll -= player_speed 

        if obstacles[-1] - scroll < WIDTH:
            new_obs_x = obstacles[-1] + random.randint(400, 700)
            obstacles.append(new_obs_x)
        if obstacles[0] - scroll < -200:
            obstacles.pop(0)

        # 4. 蓄力值增加逻辑
        if is_charging and not jump:
            if charge_power < MAX_CHARGE:
                charge_power += CHARGE_SPEED

        # 5. 跳跃物理逻辑
        if jump:
            player_y += y_speed
            y_speed += gravity
            if player_y >= ground_y:
                player_y = ground_y
                jump = False
                y_speed = 0

    # 6. 绘图部分
    screen.fill(BLACK)
    
    # 画地平线和移动刻度
    pygame.draw.line(screen, WHITE, (0, 350), (WIDTH, 350), 10)
    for i in range(-100, WIDTH + 100, 100): 
        mark_x = (i - scroll) % WIDTH
        pygame.draw.line(screen, WHITE, (mark_x, 350), (mark_x, 360), 2)

    player_rect = pygame.Rect(player_x, player_y, player_size, player_size)# 玩家矩形，用于碰撞检测

    # 画障碍物并检测碰撞
    for obs_x in obstacles:
        screen_x = obs_x - scroll
        if -50 < screen_x < WIDTH + 50:
            obs_rect = pygame.Rect(screen_x, 350 - obs_height, obs_width, obs_height)
            pygame.draw.rect(screen, GRAY, obs_rect)
            
            # 检测碰撞：一旦撞上，game_active 变 False
            if player_rect.colliderect(obs_rect):
                game_active = False # 立马停止！

    # 画玩家：如果是蓄力状态，改变颜色和形状
    if is_charging:
        # 蓄力时方块稍微变矮（像被压缩了），颜色变红
        shrink_amount = charge_power * 1.2
        pygame.draw.rect(screen, RED, (player_x, player_y + shrink_amount, player_size, player_size - shrink_amount))
    else:
        # 正常状态
        pygame.draw.rect(screen, BLUE, (player_x, player_y, player_size, player_size))

    if not game_active:
        text_surf = FONT.render("GAME OVER! Press R to Restart", True, WHITE)
        screen.blit(text_surf, (WIDTH // 2 - 160, HEIGHT // 2 -120 ))

    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()