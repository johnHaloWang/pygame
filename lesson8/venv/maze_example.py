import pygame, sys, runner, crate

pygame.init()
SCREENSIZE = (1600, 1800)
class Control():

    def __init__(self):
        self.obstacles = [crate.Crate((800, 800))]
        self.bg_mask, self.bg_image = self.make_bg_mask()

        # self.bg_mask, self.bg_image = self.make_bg_mask()
        # self.obstacles = [crate.Crate((250, 100))]

    def update(self):
        SCREEN.fill(WHITE)
        SCREEN.blit(self.bg_image, (0, 0))
        runner.update(self.bg_image, self.bg_image)
        
    def main(self):
        self.update()
        self.event_loop()
        runner.update(self.bg_mask, self.bg_image)

    def make_bg_mask(self):
        temp = pygame.Surface(SCREENSIZE).convert_alpha()
        temp.fill((0, 0, 0, 0))
        for obs in self.obstacles:
            obs.update(temp)
        return pygame.mask.from_surface(temp), temp
        # temp = pygame.Surface(SCREEN.get_size())
        # temp.fill((255, 255, 255, 0))
        # for obs in self.obstacles:
        #     obs.update(temp)
        # return pygame.mask.from_surface(temp), temp

    def event_loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    runner.ddown = True
                    if runner.x_vel < 0:
                        runner.x_vel = -runner.x_vel
                if event.key == pygame.K_a:
                    runner.adown = True
                    if runner.x_vel > 0:
                        runner.x_vel = -runner.x_vel
                    if event.key == pygame.K_SPACE:
                        runner.spacedown = True

                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_d:
                            runner.ddown = False
                        if event.key == pygame.K_a:
                            runner.adown = False
                        if event.key == pygame.K_SPACE:
                            runner.spacedown = False
# sets up colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# sets up screen
SCREEN = pygame.display.set_mode((1600, 1800))
SCREEN.fill(WHITE)
# defines general veriables and objects
clock = pygame.time.Clock()
running = True
runit = Control()
runner = runner.Runner([10, 10])
# main loop
while running:
    runit.main()
    clock.tick(60)
    pygame.display.flip()
