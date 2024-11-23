from core import *
from core.eventsystem.event import Event
class ItemData:
    def __init__(self, name: str, cost: int, spoliage: int, texture_path: str):
        self.__name = name                  # Название предмета
        self.__cost = cost                  # Стоимость предмета в золоте
        self.__spoliage = spoliage          # Порча, которую даёт предмет
        self.__texture_path = texture_path   # Путь до иконки предмета

    @property
    def name(self) -> str:
        return self.__name

    @property
    def cost(self) -> int:
        return self.__cost

    @property
    def spoliage(self) -> int:
        return self.__spoliage

    @property
    def texture_path(self) -> str:
        return self.__texture_path


