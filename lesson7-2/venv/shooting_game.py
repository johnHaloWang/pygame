import pygame
import sys
import time
import random

pygame.init()

random.seed()
is_shooting = False
is_enemy = False
is_win = False
is_running = True
red = 178,34,34
crash_sound = pygame.mixer.Sound("bomb.wav")
size_x = 1200
size_y = 800
randomUpperBound = size_y - 200
randomLowerBound = 50
kills = 0


size = (size_x, size_y)
screen = pygame.display.set_mode(size)

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



start = time.process_time()
showEnemyCounter = 0
# from right
en_image_rect.centerx = size_x + 400
# top is zero
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
              ml_image_rect.centerx = player_image_rect.centerx + 100
              ml_image_rect.centery = player_image_rect.centery
              pygame.mixer.Sound.play(crash_sound)

   screen.blit(bg_image, bg_image_rect)
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
           ml_image_rect = ml_image_rect.move([10, 0])
           screen.blit(ml_image, ml_image_rect)

       if en_image_rect.centerx == 0:
           is_enemy = False
           en_image_rect.centerx = 1600
           en_image_rect.centery = random.randrange(randomLowerBound, randomUpperBound);

       if player_image_rect.colliderect(en_image_rect):
           display_text = basicfont.render("YOU LOST", True, red)
           screen.blit(display_text, text_rect)
           is_running = False

       if en_image_rect.colliderect(ml_image_rect):
           ml_image_rect.centerx = 1700
           ml_image_rect.centery = 1700
           en_image_rect.centerx = 1800
           en_image_rect.centery = 1800
           is_enemy = False
           is_shooting = False
           kills+=1
           score = basicfont.render("Score: " + str(kills), True, red)
           pygame.draw.rect(screen, red, ml_image_rect)
           pygame.draw.rect(screen, red, en_image_rect)

       if is_win:
           display_text = basicfont.render("YOU WIN", True, red)
           screen.blit(display_text, text_rect)
           is_running = False

       screen.blit(score, score_rect)
       pygame.display.flip()
