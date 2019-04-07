import pygame
import sys
import time
import random

pygame.init()
sizex = 1200
sizey = 800
randomUpperBound = sizey - 200
randomLowerBound = 50
random.seed()
red = 178, 34, 34
size = (sizex, sizey)
screen = pygame.display.set_mode(size)
sound = pygame.mixer.Sound("Arrow+Swoosh+1.wav")
bg_image = pygame.image.load("BTD 5 Map.jpg")

bg_image = pygame.transform.scale(bg_image, (1200, 800))
bg_image_rect = bg_image.get_rect()
kills = 0
player_image = pygame.image.load("Dart Monkey.jpg")
#did not scale the image
player_image = pygame.transform.scale(player_image, (90, 90))
player_image_rect = player_image.get_rect()

projectile_image = pygame.image.load("Ninja Star.png")
#did not scale the image
projectile_image = pygame.transform.scale(projectile_image, (30, 10))
projectile_image_rect = projectile_image.get_rect()

en_image = pygame.image.load("Balloon.png")
#did not scale the image
en_image = pygame.transform.scale(en_image, (90, 90))
en_image_rect = en_image.get_rect()

is_win = False
is_shooting = False
is_running = True
is_enemy = False

basicfont = pygame.font.SysFont(None, 100)
display_text = basicfont.render("", True,red)
text_rect = display_text.get_rect()
text_rect.centerx = sizex / 3
text_rect.centery = sizey / 2

score = basicfont.render("Score: " + str(kills), True, red)
score_rect = score.get_rect()
score_rect.centerx = sizex/2
score_rect.centery = sizey - sizey/8


start = time.process_time()
showEnemyCounter = 0
en_image_rect.centerx = sizex + 400
en_image_rect.centery = random.randrange(randomLowerBound, randomUpperBound)
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
                projectile_image_rect.centerx = player_image_rect.centerx + 100
                projectile_image_rect.centery = player_image_rect.centery
                pygame.mixer.Sound.play(sound)

    screen.blit(bg_image,bg_image_rect)
    screen.blit(player_image, player_image_rect)
    showEnemyCounter = float(time.process_time() - start)
    if is_running:
        if kills is 5:
            is_win = True
        if is_enemy == False and showEnemyCounter > 0.2:
            is_enemy = True
            start = time.process_time()
        if is_enemy == True:
            en_image_rect.centerx = en_image_rect.centerx - 10
            en_image_rect.centery = en_image_rect.centery
            screen.blit(en_image, en_image_rect)
        if is_shooting:
            projectile_image_rect = projectile_image_rect.move([10, 0])
            screen.blit(projectile_image, projectile_image_rect)
        if en_image_rect.centerx == 0:
            is_enemy = False
            en_image_rect.centerx = sizex + 400
            en_image_rect.centery = random.randrange(randomLowerBound, randomUpperBound)
        if player_image_rect.colliderect(en_image_rect):
            display_text = basicfont.render("You lost", True, red)
            screen.blit(display_text, text_rect)
            is_running = False
        if en_image_rect.colliderect(projectile_image_rect):
            projectile_image_rect.centerx = 1700
            projectile_image_rect.centery = 1700
            en_image_rect.centerx = 1900
            en_image_rect.centery = 1900
            is_enemy = False
            is_shooting = False
            kills+=1
            score = basicfont.render("score: " + str(kills), True, red)
            pygame.draw.rect(screen, red, projectile_image_rect)
            pygame.draw.rect(screen, red, en_image_rect)
        if is_win:
            display_text = basicfont.render("you win", True, red)
            screen.blit(display_text, text_rect)
            is_running = False
        screen.blit(score, score_rect)
        pygame.display.flip()