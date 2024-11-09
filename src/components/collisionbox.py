import pyray

from core import *
from pyray import Rectangle

class CollisionBox(ActorComponent):

    def __init__(self, width: float, height: float):
        super().__init__()
        self.width = width
        self.height = height
        self._rectangle: Rectangle = Rectangle(0, 0, 0, 0)


    def on_start(self) -> None:
        self._rectangle: Rectangle = Rectangle(0, 0, 0, 0)


    def __getstate__(self):
        state = self.__dict__.copy()
        del state['_rectangle']
        return state


    def on_debug_draw(self, frame_time: float) -> None:
        self.update_position()
        pyray.draw_rectangle_lines_ex(self._rectangle, 4, pyray.GREEN)


    def update_position(self) -> None:
        self._rectangle.x = self.actor.position.x - self.width * 0.5
        self._rectangle.y = self.actor.position.y - self.height * 0.5
        self._rectangle.width = self.width * self.actor.scale.x
        self._rectangle.height = self.height * self.actor.scale.y


    def check_collision_point(self, point: Vector2) -> bool:
        self.update_position()
        return pyray.check_collision_point_rec(point, self._rectangle)
