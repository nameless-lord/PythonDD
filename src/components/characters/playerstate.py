from typing import List
from core import *
from core.eventsystem.event import Event
from components.items.itemdata import ItemData


class PlayerState(ActorComponent):

    @property
    def gold(self) -> int:
        return self.__gold

    @property
    def inventory(self) -> List[ItemData]:
        return self.__inventory



    def __init__(self):
        super().__init__()
        self.__gold: int = 0  # Поле для хранения количества золота
        self.__inventory: List[ItemData] = []  # Поле для хранения инвентаря (список предметов)

        # События для изменения состояния
        self.gold_changed: Event = Event()
        self.inventory_changed: Event = Event()



    def add_gold(self, amount: int) -> None:

        self.__gold += amount
        self.gold_changed.invoke()  # Вызываем событие об изменении золота

    def remove_gold(self, amount: int) -> None:
        if self.__gold - amount < 0:
            self.__gold = 0
        else:
            self.__gold -= amount
        self.gold_changed.invoke()  # Вызываем событие об изменении золота

    def add_item(self, item: ItemData) -> None:
        self.__inventory.append(item)
        self.inventory_changed.invoke()  # Вызываем событие об изменении инвентаря

    def remove_item(self, item: ItemData) -> None:
        if item in self.__inventory:
            self.__inventory.remove(item)
            self.inventory_changed.invoke()  # Вызываем событие об изменении инвентаря

    def clear_inventory(self) -> None:
        self.__inventory.clear()
        self.inventory_changed.invoke()  # Вызываем событие об изменении инвентаря





























