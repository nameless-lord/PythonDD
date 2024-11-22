from core import *
from core.eventsystem.event import Event
class Spoliage(ActorComponent):
    def __init__(self, max_spoliage: int):
        super().__init__()
        self.__current_spoliage: int = 0  # Текущее значение порчи
        self.__max_spoliage: int = 100  # Максимальное значение порчи

        # События для изменения порчи и смерти персонажа
        self.spoliage_changed: Event = Event()
        self.character_died: Event = Event()

    @property
    def current_spoliage(self) -> int:
        return self.__current_spoliage

    @property
    def max_spoliage(self) -> int:
        return self.__max_spoliage

    def add_spoliage(self, amount: int) -> None:
        self.__current_spoliage += amount
        if self.__current_spoliage >= self.__max_spoliage:
            self.__current_spoliage = self.__max_spoliage
            self.character_died.invoke()  # Вызываем событие смерти персонажа
        self.spoliage_changed.invoke()  # Вызываем событие об изменении порчи

    def reset_spoliage(self) -> None:
        self.__current_spoliage = 0
        self.spoliage_changed.invoke()  # Вызываем событие об изменении порчи
