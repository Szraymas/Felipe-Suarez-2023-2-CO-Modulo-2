import random

from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import BIRD

class Bird(Obstacle):
    BIRD_HEIGHTS = [310, 230, 100]

    def __init__(self):
        self.type = 0
        super().__init__(BIRD, self.type)
        self.rect.y = self.BIRD_HEIGHTS[random.randint(0, 2)] 
        self.index = 0
        self.vel_y = random.randint(-5, 5)

    def draw(self, screen):
        if self.index >= 9:
            self.index = 0
    
        screen.blit(BIRD[self.index // 5], self.rect)   
        self.index += 1

        self.rect.y += self.vel_y

        if self.rect.top <= 0:
            self.vel_y = random.randint(1, 5)
        elif self.rect.bottom >= 380:
            self.vel_y = random.randint(-5, -1)