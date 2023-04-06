import pygame
import random

from dino_runner.components.power_ups.shield import Shield
#from dino_runner.components.power_ups.SlowMotionPower_Up import SlowMotionPowerUp

class PowerUpManager:
    def __init__(self):
        self.power_ups = []
        self.when_appears = random.randint(150, 250)
        self.duration = random.randint(3, 5)
        #Slow Motion
        #self.active = False
        #self.durationS = 5000
        #self.start_time = None

#
    #def apply(self, game):
        #self.active = True
        #self.start_time = game.current.time

        #for obstacle in game.obstacle_manager.obstacles:
        #    obstacle.speed *= 0.5

        #game.draw_background.speed *= 0.5

#
    def generate_power_up(self):
        power_up = Shield() 
        #power_up_slow_motion = SlowMotionPowerUp() 
        self.when_appears += random.randint(150, 250)
        self.power_ups.append(power_up)  
        #self.power_ups.append(power_up_slow_motion) 


    def update(self, game):
        if len(self.power_ups) == 0 and self.when_appears == game.score.count:
            self.generate_power_up()

        for power_up in self.power_ups:
            power_up.update(game.game_speed, self.power_ups)
            if game.player.dino_rect.colliderect(power_up.rect):
                power_up.start_time = pygame.time.get_ticks()
                game.player.type = power_up.type
                game.player.has_power_up = True
                game.player.power_time_up = power_up.start_time + (self.duration * 1000)
                self.power_ups.remove(power_up)
        #
      #  if self.active:
      #      current_time = game.current.time
       #     elapsed_time = current_time - self.start_time

#            if elapsed_time >= self.duration:
 #               for power_up in self.power_ups:
  #                  if power_up.type == "slow_motion":
   #                     self.power_up.remove(game)
        #


    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)


    def reset(self):
        self.power_ups = []
        self.when_appears = random.randint(150, 250)
