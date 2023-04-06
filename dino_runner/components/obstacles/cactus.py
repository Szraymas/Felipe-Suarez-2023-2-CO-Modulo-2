import random

from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS
class Cactus(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 5)
        if self.type < 3:
            super().__init__(SMALL_CACTUS, self.type)
            self.rect.y = 325
        else:
            super().__init__(LARGE_CACTUS, self.type - 3)
            self.rect.y = 300
        #super().__init__(image, self.type)
        #self.rect.y = 325