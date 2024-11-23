from core import *
from components.characters.health import Health

class DamageOverTime(ActorComponent):
    def __init__(self, damage: int, period: float):
        super().__init__()
        self.__damage = damage
        self.__period = period
        self.__timer = 0.0
        self.__health: Health = None

    def on_start(self):
        self.__health = self.actor.get_component(Health)

    def on_update(self, frame_time: float):
        self.__timer += frame_time
        if self.__timer >= self.__period:
            self.__health.take_damage(self.__damage)
            self.__timer = 0.0