import pygame
from os.path import join
import random

pygame.init()
clock = pygame.time.Clock()

# 1. 初始化星星数据
# 每个元素包含：[frect对象, 速度]
stars_far = []   # 远景：小、暗、慢
stars_mid = []   # 中景：中、亮一点、中速
stars_near = []  # 近景：大、最亮、最快

def create_stars(list_name, count, size_range, speed_range):
    for _ in range(count):
        size = random.uniform(*size_range)
        # 使用 frect 确保移动平滑
        rect = pygame.FRect(random.randint(0, 1280), random.randint(0, 720), size, size)
        speed = random.uniform(*speed_range)
        list_name.append([rect, speed])

# 生成背景：远、中、近三层
create_stars(stars_far, 100, (1, 2), (10, 30))
create_stars(stars_mid, 50, (2, 3), (40, 70))
create_stars(stars_near, 20, (3, 4), (80, 120))

def update_and_draw_stars(surface, star_list, color, dt):
    for star in star_list:
        rect, speed = star
        # 2. 更新位置（向下移动）
        rect.y += speed * dt
        
        # 3. 循环滚动：飞出底部后回到顶部
        if rect.top > 720:
            rect.bottom = 0
            rect.x = random.randint(0, 1280)
            
        # 4. 绘制星星
        pygame.draw.ellipse(surface, color, rect)

WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Shooter")

player_surf = pygame.image.load(join("Game-in-Python", "images", "player_ship.png")).convert_alpha()
player_rect = player_surf.get_frect(center = (WIDTH / 2, HEIGHT - 100))
player_direction = pygame.math.Vector2(0, 0)
player_speed = 100 

enemy_surf = pygame.image.load(join("Game-in-Python", "images", "enemy_ship.png")).convert_alpha()
enemy_rect = enemy_surf.get_frect(center = (WIDTH / 2, 100))

running = True
while running:
    
    dt = clock.tick(60) / 1000  
    print(f"FPS: {clock.get_fps():.2f}")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                player_direction.x = -1
            if event.key == pygame.K_d:
                player_direction.x = 1
            if event.key == pygame.K_w:
                player_direction.y = -1
            if event.key == pygame.K_s:
                player_direction.y = 1

    player_rect.clamp_ip(screen.get_rect())

    screen.fill((5, 5, 15))
    update_and_draw_stars(screen, stars_far, (100, 100, 120), dt) # 灰色暗星
    update_and_draw_stars(screen, stars_mid, (180, 180, 200), dt) # 银色中星
    update_and_draw_stars(screen, stars_near, (255, 255, 255), dt) # 白色亮星

    player_rect.center += player_direction * player_speed * dt
    screen.blit(enemy_surf, enemy_rect)
    screen.blit(player_surf, player_rect)
    

    
    
    pygame.display.update()

pygame.quit()