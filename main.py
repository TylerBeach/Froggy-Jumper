import pygame
from sys import exit

pygame.init()  # starting the car
screen = pygame.display.set_mode((1400, 700))  # creates window
game_active = True
# Title of window
pygame.display.set_caption('Frog Jumper')

# CLOCK OBJECT
clock = pygame.time.Clock()

# Backdrop (?)
backdrop_surf = pygame.image.load('backdrop.jpeg').convert_alpha()
backdrop_surf = pygame.transform.scale(backdrop_surf, (1400, 700))
backdrop_rect = backdrop_surf.get_rect(center=(700, 350))

# Button
button_surf = pygame.image.load('trim.png').convert_alpha()
button_surf = pygame.transform.scale(button_surf, (600, 150))
button_rect = button_surf.get_rect(midbottom=(700, 150))

# Text
test_font = pygame.font.Font('pixeloid-font/pixeloidSans.ttf', 50)
text_surf = test_font.render('Frog Jumper', True, 'Black')
text_rect = text_surf.get_rect(center=(700, 75))

# Start button and Rectangle
# start_button = pygame.image.load('start_button2:png.png').convert_alpha()
# start_button = pygame.transform.scale(start_button, (200, 75))
# start_but_rect = start_button.get_rect(midtop=(400, 75))

# Enemy surface and rectangle
enemy_surf = pygame.image.load('robin.png').convert_alpha()
enemy_surf = pygame.transform.scale(enemy_surf, (50, 50))
enemy_x_pos = 1300
enemy_rect = enemy_surf.get_rect(midbottom=(enemy_x_pos, 600))

# Character surface and rectangle
player_surface = pygame.image.load('cuty_frog.png').convert_alpha()
player_surface = pygame.transform.scale(player_surface, (100, 75))
player_x_pos = 200
player_rectangle = player_surface.get_rect(midbottom=(player_x_pos, 600))
player_gravity = 0
velocity = 5
# Score
score = 0
score_surface = test_font.render(f'{score}', True, 'Black')
score_rect = score_surface.get_rect(midbottom=(1200, 100))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # if user closes window
            pygame.quit()
            exit()  # sys module function
        if game_active:
            if player_rectangle.bottom >= 600:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        player_gravity = -20

        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                enemy_rect.left = 1500
                score = 0
                score_surface = test_font.render(f'{score}', True, 'Black')
                score_rect = score_surface.get_rect(midbottom=(1200, 100))

    if game_active:
        # Updating/creating Sky, Grass and Start Button
        point_line = pygame.draw.line(screen, 'red', (140, 0), (140, 800))

        screen.blit(backdrop_surf, backdrop_rect)
        pygame.draw.rect(screen, 'orange', text_rect)
        pygame.draw.rect(screen, 'orange', text_rect, 20)
        screen.blit(button_surf, button_rect)
        screen.blit(text_surf, text_rect)
        screen.blit(score_surface, score_rect)

        # pygame.draw.rect(screen, 'orange', start_but_rect, border_radius=20)
        # screen.blit(start_button, start_but_rect)

        # Frog Hit box with Rectangle
        screen.blit(enemy_surf, enemy_rect)

        x_speed = 0
        if score < 10:
            x_speed = 20
            enemy_rect.x -= x_speed
        elif score < 20:
            x_speed = 25
            enemy_rect.x -= x_speed
        elif score < 30:
            x_speed = 30
            enemy_rect.x -= x_speed
        elif score < 40:
            x_speed = 35
            enemy_rect.x -= x_speed
        elif score < 50:
            x_speed = 40
            enemy_rect.x -= x_speed
        elif score < 60:
            x_speed = 45
            enemy_rect.x -= x_speed
        elif score < 70:
            x_speed = 50
            enemy_rect.x -= x_speed
        elif score < 80:
            x_speed = 55
            enemy_rect.x -= x_speed

        if enemy_rect.right <= 0:
            enemy_rect.left = 1500
        screen.blit(enemy_surf, enemy_rect)

        # Player
        player_gravity += 1
        player_rectangle.y += player_gravity
        if player_rectangle.bottom >= 600:
            player_rectangle.bottom = 600
        screen.blit(player_surface, player_rectangle)

        # Collisions
        if point_line.left in range(enemy_rect.right, enemy_rect.right + x_speed):
            score += 1
            score_surface = test_font.render(f'{score}', True, 'Black')
            score_rect = score_surface.get_rect(midbottom=(1200, 100))
        screen.blit(score_surface, score_rect)
        if enemy_rect.colliderect(player_rectangle):
            game_active = False

        # Player Movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            player_x_pos -= velocity
        if keys[pygame.K_d]:
            player_x_pos += velocity

    else:
        screen.fill('Orange')
        final_score_surf = test_font.render(f'Your score was {score}', True, 'Black')
        final_score_rect = final_score_surf.get_rect(midbottom=(700, 100))
        screen.blit(final_score_surf, final_score_rect)
        play_again_surf = test_font.render('Press space to play again.', True, 'Black')
        play_again_rect = play_again_surf.get_rect(midbottom=(700, 200))
        screen.blit(play_again_surf, play_again_rect)

    # Update game and FPS
    pygame.display.update()
    clock.tick(60)  # 60 frames per second
