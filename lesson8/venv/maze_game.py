import pygame
import sys
import time
import random


# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (50, 50, 255)

class Wall(pygame.sprite.Sprite):
    """ Wall the player can run into. """

    def __init__(self, x, y, width, height):
        """ Constructor for the wall that the player can run into. """
        # Call the parent's constructor
        super().__init__()

        # Make a blue wall, of the size specified in the parameters
        self.image = pygame.image.load("crate.png")
        self.image = pygame.transform.scale(self.image, (50, 50))

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x


class Player(pygame.sprite.Sprite):
    """ This class represents the bar at the bottom that the player
    controls. """

    # Constructor function
    def __init__(self, x, y):
        # Call the parent's constructor
        super().__init__()

        # Set height, width
        self.image = pygame.image.load("plane.png")
        self.image = pygame.transform.scale(self.image, (40, 40))
        #self.image = pygame.Surface([15, 15])
        #self.image.fill(WHITE)

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

        # Set speed vector
        self.change_x = 0
        self.change_y = 0
        self.walls = None

    def changespeed(self, x, y):
        """ Change the speed of the player. """
        self.change_x += x
        self.change_y += y

    def update(self):
        """ Update the player position. """
        # Move left/right
        self.rect.x += self.change_x

        # Did this update cause us to hit a wall?
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:
            # If we are moving right, set our right side to the left side of
            # the item we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            else:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right

        # Move up/down
        self.rect.y += self.change_y

        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:

            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom



pygame.init()



size_x = 600
size_y = 600

size = (size_x, size_y)

screen = pygame.display.set_mode(size)
bg_image = pygame.image.load("background.png")
bg_image = pygame.transform.scale(bg_image, (size_x, size_y))
bg_image_rect = bg_image.get_rect()
#
#
# player_image = pygame.image.load("plane.png")
# player_image = pygame.transform.scale(player_image, (90, 90))
# player_image_rect = player_image.get_rect()

# List to hold all the sprites
all_sprite_list = pygame.sprite.Group()

# Make the walls. (x_pos, y_pos, width, height)
wall_list = pygame.sprite.Group()

#x, y
y = 0
while  y < 600:
    wall = Wall(0, y, 50, 50)
    wall_list.add(wall)
    all_sprite_list.add(wall)
    y+=50

x = 50;
while x <150:
    wall = Wall(x, 200, 50, 50)
    wall_list.add(wall)
    all_sprite_list.add(wall)
    x+=50

y = 200;
while y <400:
    wall = Wall(150, y, 50,50)
    wall_list.add(wall)
    all_sprite_list.add(wall)
    y+=50

y = 0
while y<300:
    wall = Wall(250, y, 50,50)
    wall_list.add(wall)
    all_sprite_list.add(wall)
    y+=50

x = 200
y = 450
while(x<400):
    wall = Wall(x, y, 50, 50)
    wall_list.add(wall)
    all_sprite_list.add(wall)
    x += 50
x = 200
y = 500
while(x<400):
    wall = Wall(x, y, 50, 50)
    wall_list.add(wall)
    all_sprite_list.add(wall)
    x += 50

x = 350
y = 100
while(y<450):
    wall = Wall(x, y, 50, 50)
    wall_list.add(wall)
    all_sprite_list.add(wall)
    y += 50

x = 400
y = 100

while(x<500):
    wall = Wall(x, y, 50, 50)
    wall_list.add(wall)
    all_sprite_list.add(wall)
    x += 50

x = 450
y = 150
while(y<400):
    wall = Wall(x, y, 50, 50)
    wall_list.add(wall)
    all_sprite_list.add(wall)
    y += 50

x = 450
y = 0
while(x<600):
    wall = Wall(x, y, 50, 50)
    wall_list.add(wall)
    all_sprite_list.add(wall)
    x += 50


x = 550
y = 50
while(y<450):
    wall = Wall(x, y, 50, 50)
    wall_list.add(wall)
    all_sprite_list.add(wall)
    y += 50


# Create the player paddle object
player = Player(50, 0)
player.walls = wall_list

all_sprite_list.add(player)

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.changespeed(-50, 0)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(50, 0)
            elif event.key == pygame.K_UP:
                player.changespeed(0, -50)
            elif event.key == pygame.K_DOWN:
                player.changespeed(0, 50)

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.changespeed(50, 0)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(-50, 0)
            elif event.key == pygame.K_UP:
                player.changespeed(0, 50)
            elif event.key == pygame.K_DOWN:
                player.changespeed(0, -50)

        all_sprite_list.update()
        screen.blit(bg_image, bg_image_rect)
        #screen.blit(player_image, player_image_rect)
        all_sprite_list.draw(screen)
        pygame.display.flip()

