import math

from core import *


class TestMotion(ActorComponent):
    def on_update(self, frame_time: float) -> None:
        time: float = pyray.get_time()
        position: Vector2 = Vector2(100 * math.sin(time), 150 * math.cos(time))

        self._actor.position = position