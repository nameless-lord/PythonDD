from components.characters.health import Health
from components.characters.playerstate import PlayerState
from core import *

class DamageResponse(ActorComponent):
    def __init__(self):
        super().__init__()
        self.__player_state = None


    def on_start(self) -> None:
        self.__player_state = self.actor.scene.find_component(PlayerState)
        self.actor.get_component(Health).damaged.add_callback(self.on_damage_dealed)


    def on_damage_dealed(self, amount):
        self.__player_state.add_gold(amount)

        if not self.actor.get_component(Health).is_alive:
            self.actor.destroy()