import pygame
from sys import exit
pygame.init()

clock = pygame.time.Clock()

window = pygame.display.set_mode((1400, 700))
pygame.display.set_caption('Testing Movement')

# Font used
test_font = pygame.font.Font('pixeloid-font/pixeloidSans.ttf', 50)

# Player Things
velocity = 7
gravity = 0
player_surf = pygame.image.load('cuty_frog.png').convert_alpha()
player_surf = pygame.transform.scale(player_surf, (100, 75))
player_rect = player_surf.get_rect(midbottom=(50, 500))

# Enemy Things
enemy_surf = pygame.image.load('dino.png').convert_alpha()
enemy_surf = pygame.transform.scale(enemy_surf, (50, 50))
enemy_x_pos = 1300
enemy_rect = enemy_surf.get_rect(midbottom=(1300, 575))


# Backdrop
backdrop_surf = pygame.image.load('backdrop.jpeg').convert_alpha()
backdrop_surf = pygame.transform.scale(backdrop_surf, (1400, 700))
backdrop_rect = backdrop_surf.get_rect(midbottom=(700, 350))

# Score text
score = 0
score_surf = test_font.render(f'{score}', True, 'Black')
score_rect = score_surf.get_rect(midbottom=(1200, 100))

game = True

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    if game:
        # Colour Window
        window.blit(backdrop_surf, backdrop_rect)

        # Create Enemy
        window.blit(enemy_surf, enemy_rect)

        # Create Player
        window.blit(player_surf, player_rect)

        # Enemy Collision
        player_rect = player_surf.get_rect(bottomleft=(50, 500))
        enemy_rect = enemy_surf.get_rect(bottomleft=(enemy_x_pos, 575))

        # Enemy Movement
        enemy_rect.x -= 5
        if enemy_rect.right <= 0:
            enemy_rect.x = 1400
            score += 1
            print(score)
        if score < 5:
            enemy_rect.x -= 5
        elif score < 10:
            enemy_rect.x -= 8
        elif score < 15:
            enemy_rect.x -= 12
        elif score < 20:
            enemy_rect.x -= 17
        elif score < 25:
            enemy_rect.x -= 21
        elif score < 30:
            enemy_rect.x -= 23
        elif score < 35:
            enemy_rect.x -= 27
        else:
            enemy_rect.x -= 30

        # Player Sideways Movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            player_rect.x -= velocity
        if keys[pygame.K_d]:
            player_rect.x += velocity

        # Player Gravity
        if player_rect.y >= 500:
            if keys[pygame.K_SPACE]:
                gravity = -20
        gravity += 1
        player_rect.y += gravity
        if player_rect.y >= 500:
            player_rect.y = 500

        # Print Score
        score_surf = test_font.render(f'{score}', True, 'Black')
        score_rect = score_surf.get_rect(midbottom=(1200, 100))
        window.blit(score_surf, score_rect)

    else:
        window.fill('Black')

    pygame.display.update()
    clock.tick(60)
