import pyray

from core import *
from core.eventsystem.event import Event
from components.collisionbox import CollisionBox


class Button(ActorComponent):

    def __init__(self):
        super().__init__()
        self.pressed: Event = Event()
        self.__collision_box: CollisionBox = None


    def on_start(self) -> None:
        self.__collision_box = self.actor.get_component(CollisionBox)


    def __getstate__(self):
        state = self.__dict__.copy()
        del state['_Button__collision_box']
        return state


    def on_update(self, frame_time: float) -> None:
        if pyray.is_mouse_button_pressed(pyray.MouseButton.MOUSE_BUTTON_LEFT):
            world_point = pyray.get_screen_to_world_2d(pyray.get_mouse_position(), Game.camera)
            if self.__collision_box.check_collision_point(world_point):
                self.pressed.invoke()