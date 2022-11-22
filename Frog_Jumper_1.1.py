import pygame
from sys import exit
import time
import random
from Froggy_Jumper_Functions import random_object

# BASIC SETUP
pygame.init()
screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption('Froggy Jumper 1.1')
clock = pygame.time.Clock()
main_menu = True
froggy_alive = False
lose_screen = False
daytime_level = False
nighttime_level = False

# CLOUD 1
cloud1_surf = pygame.image.load('cloud.png')
cloud1_surf = pygame.transform.scale(cloud1_surf, (200, 130))
cloud1_x = 50
cloud1_rect = cloud1_surf.get_rect(topleft=(cloud1_x, 10))

# CLOUD 2
cloud2_surf = pygame.image.load('cloud.png')
cloud2_surf = pygame.transform.scale(cloud2_surf, (200, 130))
cloud2_x = 400
cloud2_rect = cloud2_surf.get_rect(topleft=(cloud2_x, 40))

# CLOUD 3
cloud3_surf = pygame.image.load('cloud.png')
cloud3_surf = pygame.transform.scale(cloud3_surf, (200, 130))
cloud3_x = 770
cloud3_rect = cloud3_surf.get_rect(topleft=(cloud3_x, 25))

# GROUND
ground_surf = pygame.image.load('groundmaybe.png').convert_alpha()
ground_surf = pygame.transform.scale(ground_surf, (2000, 700))
ground_x = 0
ground_rect = ground_surf.get_rect(topleft=(ground_x, 450))

# PLAYER
player_x = 0
player_y = 450
player_surf = pygame.image.load('thefroggy.png').convert_alpha()
player_surf = pygame.transform.scale(player_surf, (100, 100))
player_rect = player_surf.get_rect(bottomleft=(player_x, player_y))
velocity = 0

# SNAKE
snake_surf = pygame.image.load('flatsnake.png').convert_alpha()
snake_surf = pygame.transform.scale(snake_surf, (170, 50))
snake_x = 800
snake_rect = snake_surf.get_rect(bottomleft=(snake_x, 450))

# FLY
fly_surf = pygame.image.load('fly.png').convert_alpha()
fly_surf = pygame.transform.scale(fly_surf, (100, 100))
fly_x = 1000
fly_rect = fly_surf.get_rect(bottomleft=(fly_x, 250))

# OBJECT PICKED
snake_object = False
fly_object = False
object_picked = random_object()

# SCORE
score = 0
test_font = pygame.font.Font('pixeloid-font/pixeloidSans.ttf', 50)
score_surf = test_font.render(f'Score: {score}', False, 'Black')
score_rect = score_surf.get_rect(bottomleft=(10, 600))

# YOU LOST SCREEN
lost_screen_surf = test_font.render('Froggy died to the snake', False, 'Black')
lost_screen_rect = lost_screen_surf.get_rect(midbottom=(500, 100))

# DEADFROG
dead_frog_surf = pygame.image.load('deadfroggy.png').convert_alpha()
dead_frog_surf = pygame.transform.scale(dead_frog_surf, (400, 400))
dead_frog_rect = dead_frog_surf.get_rect(bottomleft=(350, 425))

# PRESS SPACE TO PLAY AGAIN
play_again_text_surf = test_font.render('Press Space to revive froggy!', False, 'Black')
play_again_text_rect = play_again_text_surf.get_rect(midbottom=(500, 500))

# MENU TEXT
menu_text_surf = test_font.render('FROGGY JUMPER', False, 'Black')
menu_text_surf = pygame.transform.scale(menu_text_surf, (500, 100))
menu_text_rect = menu_text_surf.get_rect(midbottom=(500, 160))

# PLAY BUTTON MENU
play_button_surf = test_font.render('PLAY', False, 'Black')
play_button_surf = pygame.transform.scale(play_button_surf, (300, 100))
play_button_rect = play_button_surf.get_rect(topleft=(350, 245))

# SECRET BUTTON?
secret_button_surf = pygame.image.load('start_button2:png.png').convert_alpha()
secret_button_surf = pygame.transform.scale(secret_button_surf, (300, 100))
secret_button_rect = secret_button_surf.get_rect(topleft=(350, 245))

# BACKWARDS SNAKE
bckwrd_snake_surf = pygame.image.load('flatsnake.png').convert_alpha()
bckwrd_snake_surf = pygame.transform.flip(bckwrd_snake_surf, True, False)
bckwrd_snake_surf = pygame.transform.scale(bckwrd_snake_surf, (170, 50))
bckwrd_snake_x = -700
bckward_snake_rect = bckwrd_snake_surf.get_rect(bottomleft=(bckwrd_snake_x, 450))

# MENU FROG
menu_frog_x = -200
menu_frox_surf = pygame.image.load('thefroggy.png').convert_alpha()
menu_frox_surf = pygame.transform.scale(menu_frox_surf, (100, 100))
menu_frox_rect = menu_frox_surf.get_rect(bottomleft=(menu_frog_x, 450))

# HIGHSCORE COUNTER
highscore = 0
highscore_text_surf = test_font.render(f'High score: {highscore}', False, 'Black')
highscore_text_rect = highscore_text_surf.get_rect(bottomleft=(600, 600))

# LIVES COUNTER + IMAGES
lives = 3

# FULL HEARTS IMAGES
heartfull1_surf = pygame.image.load('heartfull.png').convert_alpha()
heartfull2_surf = pygame.image.load('heartfull.png').convert_alpha()
heartfull3_surf = pygame.image.load('heartfull.png').convert_alpha()
heartfull1_surf = pygame.transform.scale(heartfull1_surf, (200, 200))
heartfull2_surf = pygame.transform.scale(heartfull2_surf, (200, 200))
heartfull3_surf = pygame.transform.scale(heartfull3_surf, (200, 200))
heartfull1_rect = heartfull1_surf.get_rect(bottomleft=(250, 700))
heartfull2_rect = heartfull2_surf.get_rect(bottomleft=(300, 700))
heartfull3_rect = heartfull3_surf.get_rect(bottomleft=(350, 700))

#  EMPTY HEARTS IMAGES
heartempty1_surf = pygame.image.load('heartempty1.png')
heartempty2_surf = pygame.image.load('heartempty1.png')
heartempty3_surf = pygame.image.load('heartempty1.png')
heartempty1_surf = pygame.transform.scale(heartempty1_surf, (200, 200))
heartempty2_surf = pygame.transform.scale(heartempty2_surf, (200, 200))
heartempty3_surf = pygame.transform.scale(heartempty3_surf, (200, 200))
heartempty1_rect = heartempty1_surf.get_rect(bottomleft=(250, 700))
heartempty2_rect = heartempty2_surf.get_rect(bottomleft=(300, 700))
heartempty3_rect = heartempty3_surf.get_rect(bottomleft=(350, 700))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    if main_menu:

        # PLAY BUTTON HITBOX
        screen.blit(secret_button_surf, secret_button_rect)

        # FILL SCREEN BLUE
        screen.fill((3, 168, 244))

        # TITLE BORDER
        pygame.draw.rect(screen, 'Black', pygame.Rect(225, 45, 550, 130), 100)
        pygame.draw.rect(screen, 'Light Green', pygame.Rect(230, 50, 540, 120), 100)

        # PLAY BUTTON BORDER
        pygame.draw.rect(screen, 'Black', pygame.Rect(315, 240, 360, 110), 100)
        pygame.draw.rect(screen, 'Light Green', pygame.Rect(320, 245, 350, 100), 100)

        # DRAW MENU TEXT, PLAY BUTTON TEXT, GROUND
        screen.blit(menu_text_surf, menu_text_rect)
        screen.blit(play_button_surf, play_button_rect)
        screen.blit(ground_surf, ground_rect)

        # MENU FROG ANIMATION
        screen.blit(menu_frox_surf, menu_frox_rect)
        menu_frog_x += 9
        menu_frox_rect = menu_frox_surf.get_rect(bottomleft=(menu_frog_x, 450))
        if menu_frox_rect.left > 1000:
            menu_frog_x = -700

        # MENU SNAKE ANIMATION
        screen.blit(bckwrd_snake_surf, bckward_snake_rect)
        bckwrd_snake_x += 9
        if bckward_snake_rect.left > 1000:
            bckwrd_snake_x = -700
        bckward_snake_rect = bckwrd_snake_surf.get_rect(bottomleft=(bckwrd_snake_x, 450))

        # PLAY BUTTON
        keys = pygame.key.get_pressed()
        mouse_pos = pygame.mouse.get_pos()
        if secret_button_rect.collidepoint(mouse_pos) and pygame.mouse.get_pressed()[0]:
            froggy_alive = True
            main_menu = False
            time.sleep(0.2)
            object_picked = random_object()
    # FROG ALIVE
    if froggy_alive:

        # BACKGROUD STUFF
        if score < 50:
            blue_colour = 244 - (score * 2)
            green_colour = 168 - (score * 2)
            screen.fill((3, green_colour, blue_colour))
        elif score >= 50:
            screen.fill((6, 57, 112))

        screen.blit(ground_surf, ground_rect)
        screen.blit(cloud1_surf, cloud1_rect)
        screen.blit(cloud2_surf, cloud2_rect)
        screen.blit(cloud3_surf, cloud3_rect)

        # PLAYER AND ENEMIES
        screen.blit(player_surf, player_rect)
        screen.blit(snake_surf, snake_rect)
        screen.blit(fly_surf, fly_rect)

        # SCORE KEEPERS
        screen.blit(highscore_text_surf, highscore_text_rect)
        screen.blit(score_surf, score_rect)

        # HEALTH BAR DRAW
        screen.blit(heartfull1_surf, heartfull1_rect)
        screen.blit(heartfull2_surf, heartfull2_rect)
        screen.blit(heartfull3_surf, heartfull3_rect)

        # DRAW OVER HEARTS BASED ON LIVES
        if lives == 2:
            screen.blit(heartempty3_surf, heartempty3_rect)
        elif lives == 1:
            screen.blit(heartempty3_surf, heartempty3_rect)
            screen.blit(heartempty2_surf, heartempty2_rect)
        elif lives == 0:
            screen.blit(heartempty3_surf, heartempty3_rect)
            screen.blit(heartempty2_surf, heartempty2_rect)
            screen.blit(heartempty1_surf, heartempty1_rect)
            froggy_alive = False
            lose_screen = True

        # GRAVITY
        player_y += velocity
        if player_y >= 450:
            velocity = 0
            player_y = 450
        else:
            velocity += 1.5

        # JUMP MOVEMENT
        keys = pygame.key.get_pressed()
        if player_y == 450:
            if keys[pygame.K_SPACE]:
                velocity -= 25

        # SIDEWAYS MOVEMENT
        if player_rect.left > 0:
            if keys[pygame.K_LEFT]:
                player_x -= 10
        if player_rect.right < 1000:
            if keys[pygame.K_RIGHT]:
                player_x += 10
        player_rect = player_surf.get_rect(bottomleft=(player_x, player_y))

        # SPEED CONTROL
        background_speed = 5
        background_speed += score / 5
        snake_speed = 8
        snake_speed += score / 5

        # MOVING CLOUDS
        cloud1_x -= background_speed
        cloud2_x -= background_speed
        cloud3_x -= background_speed
        if cloud1_rect.right <= 0:
            cloud1_x = 1000
        if cloud2_rect.right <= 0:
            cloud2_x = 1000
        if cloud3_rect.right <= 0:
            cloud3_x = 1000
        cloud1_rect = cloud1_surf.get_rect(topleft=(cloud1_x, 10))
        cloud2_rect = cloud2_surf.get_rect(topleft=(cloud2_x, 40))
        cloud3_rect = cloud3_surf.get_rect(topleft=(cloud3_x, 25))

        # MOVING GROUND
        ground_x -= background_speed
        if ground_rect.right < 1000:
            ground_x = 0
        ground_rect = ground_surf.get_rect(topleft=(ground_x, 450))

        # RANDOM OBJECT PICKER
        if not snake_object:
            snake_x = 1100
        if not fly_object:
            fly_x = 1100

        if object_picked == 0:
            fly_object = True
            snake_object = False
            object_picked = None
        elif object_picked == 1 or object_picked == 2:
            snake_object = True
            fly_object = False
            object_picked = None

        # SNAKE MOVEMENT
        if snake_object:
            snake_x -= snake_speed
        if snake_rect.right <= 0:
            score += 1
            snake_x = 1100
            object_picked = random_object()
            snake_object = False

        # FLY MOVEMENT
        if fly_object:
            fly_x -= snake_speed
        if fly_rect.right <= 0:
            object_picked = random_object()
            fly_object = False
        elif player_rect.colliderect(fly_rect):
            score += 2
            fly_x = 1100
            object_picked = random_object()
            fly_object = False

        # UPDATE FLY + SNAKE
        fly_rect = fly_surf.get_rect(bottomleft=(fly_x, 250))
        snake_rect = snake_surf.get_rect(bottomleft=(snake_x, 450))

        # COLLISION
        if player_rect.colliderect(snake_rect):
            lives -= 1
            snake_x = 1200
            snake_object = False
            object_picked = 0

        # SCORE UPDATE
        if score > highscore:
            highscore = score
        score_rect = score_surf.get_rect(bottomleft=(10, 600))
        score_surf = test_font.render(f'Score: {score}', False, 'Black')
        highscore_text_rect = highscore_text_surf.get_rect(bottomleft=(600, 600))
        highscore_text_surf = test_font.render(f'High score: {highscore}', False, 'Black')

    if lose_screen:

        # DRAW LOSE SCREEN
        screen.fill('Light Blue')
        screen.blit(lost_screen_surf, lost_screen_rect)
        screen.blit(dead_frog_surf, dead_frog_rect)
        screen.blit(play_again_text_surf, play_again_text_rect)

        # DRAW PREVIOUS SCORE
        screen.blit(score_surf, score_rect)
        score_rect = score_surf.get_rect(midbottom=(475, 575))
        score_surf = test_font.render(f'Your score was {score}', False, 'Black')

        # SPACE TO PLAY AGAIN
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            froggy_alive = True
            fly_object = False
            snake_object = False
            lose_screen = False
            player_x = 100
            score = 0
            lives = 3
            object_picked = random_object()

    pygame.display.update()
    clock.tick(60)
