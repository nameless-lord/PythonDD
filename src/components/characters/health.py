from core import *
from core.eventsystem.event import Event
class Health(ActorComponent):

    @property
    def is_alive(self) -> bool:
        return self.__current_health > 0

    @property
    def current_health(self) -> int:
        return self.__current_health

    @property
    def max_health(self) -> int:
        return self.__max_health



    def __init__(self, max_health: int = 100):
        super().__init__()
        self.__max_health: int = max_health
        self.__current_health: int = max_health

        self.health_changed: Event = Event()
        self.damaged: Event[int] = Event()


    def take_damage(self, amount: int):
        self.__current_health -= amount
        if self.__current_health < 0:
            self.__current_health = 0
        self.health_changed.invoke()
        self.damaged.invoke(amount)


    def regenerate(self, amount: int):
        self.__current_health += amount
        self.__current_health = min(self.__current_health, self.__max_health)
        self.health_changed.invoke()












