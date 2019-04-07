import pygame
import sys
import time
import random

pygame.init()
size_x = 1200
size_y = 800
randomUpperBound = size_y -200
randomLowerBound = 50
random.seed()
red = 178, 34, 34



size = (size_x, size_y)
screen = pygame.display.set_mode(size)
crash_sound = pygame.mixer.Sound("bomb.wav")

bg_image = pygame.image.load("background.png")
bg_image = pygame.transform.scale(bg_image, (size_x, size_y))
bg_image_rect = bg_image.get_rect()

player_image = pygame.image.load("plane.png")
player_image = pygame.transform.scale(player_image, (90, 90))
player_image_rect = player_image.get_rect()


ml_image = pygame.image.load("missile.png")
ml_image = pygame.transform.scale(ml_image, (30, 10))
ml_image_rect = ml_image.get_rect()

en_image = pygame.image.load("enemy.png")
en_image = pygame.transform.scale(en_image, (90, 90))
en_image_rect = en_image.get_rect()

is_shooting = False
is_running = True
is_enemy = False
kills = 0

# Fonts
basicfont = pygame.font.SysFont(None, 100)
display_text = basicfont.render("", True, red)
text_rect = display_text.get_rect()
text_rect.centerx = size_x / 3
text_rect.centery = size_y / 2


score = basicfont.render("Score: " + str(kills), True, red)
score_rect = score.get_rect()
score_rect.centerx = size_x / 2
score_rect.centery = size_y - size_y / 8

en_image_rect.centerx = size_x + 400
en_image_rect.centery = random.randrange(randomLowerBound, randomUpperBound)
start = time.process_time()
showEnemyCounter = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_image_rect = player_image_rect.move([0, 10])
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player_image_rect = player_image_rect.move([0, -10])
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_image_rect = player_image_rect.move([-10, 0])
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player_image_rect = player_image_rect.move([10, 0])
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
               is_shooting = True
               ml_image_rect.centerx = player_image_rect.centerx + 100
               ml_image_rect.centery = player_image_rect.centery
               #crash_sound = pygame.mixer.Sound("bomb.wav")
               pygame.mixer.Sound.play(crash_sound)

    screen.blit(bg_image, bg_image_rect)
    screen.blit(player_image, player_image_rect)
    showEnemyCounter = float(time.process_time() - start)
    if is_running:
        if showEnemyCounter > 0.2:
            is_enemy = True
            start = time.process_time()
        if is_enemy == True:
            en_image_rect.centerx = en_image_rect.centerx -10
            en_image_rect.centery = en_image_rect.centery
            screen.blit(en_image, en_image_rect)
        if is_shooting:
            ml_image_rect = ml_image_rect.move([10, 0])
            screen.blit(ml_image, ml_image_rect)
        if en_image_rect.centerx == 0:
            is_enemy = False
            en_image_rect.centerx = size_x + 400
            en_image_rect.centery = random.randrange(randomLowerBound, randomUpperBound)

        if player_image_rect.colliderect(en_image_rect):
            is_running = False
        if en_image_rect.colliderect(ml_image_rect):
            #red = 178, 34, 34
            ml_image_rect.centerx = 1700
            ml_image_rect.centery = 1700
            en_image_rect.centerx = 1800
            en_image_rect.centery = 1800
            is_enemy = False
            is_shooting = False
            kills += 1
            score = basicfont.render("Score: " + str(kills), True, red)
            pygame.draw.rect(screen, red, ml_image_rect)
            pygame.draw.rect(screen, red, en_image_rect)
        pygame.display.flip()
