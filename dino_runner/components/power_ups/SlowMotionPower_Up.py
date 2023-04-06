from dino_runner.components.power_ups.power_up import PowerUp
from dino_runner.utils.constants import HEART, HEART_TYPE

class SlowMotionPowerUp(PowerUp):
    def __init__(self):
        super().__init__(HEART,HEART_TYPE)
    