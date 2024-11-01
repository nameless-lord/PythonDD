from core import *
from core.eventsystem.event import Event
from components.collisionbox import CollisionBox


class Button(ActorComponent):

    def __init__(self):
        super().__init__()
        self.pressed: Event = Event()
        self._collision_box: CollisionBox = None


    def on_start(self) -> None:
        self._collision_box = self._actor.get_component(CollisionBox)


    def on_update(self, frame_time: float) -> None:
        if pyray.is_mouse_button_pressed(pyray.MouseButton.MOUSE_BUTTON_LEFT):
            if self._collision_box.check_collision_point(pyray.get_mouse_position()):
                self.pressed.invoke()
