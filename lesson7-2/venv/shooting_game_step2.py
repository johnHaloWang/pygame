import pygame
import sys



pygame.init()


size = (1200, 800)
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

is_shooting = False

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

   if is_shooting:
       ml_image_rect = ml_image_rect.move([10, 0])
       screen.blit(ml_image, ml_image_rect)

   pygame.display.flip()
