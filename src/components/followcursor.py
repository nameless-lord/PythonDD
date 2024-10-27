from core.actorcomponent import ActorComponent
import pyray

class FollowCursor(ActorComponent):


    def on_update(self, frame_time: float) -> None:
        position = pyray.get_mouse_position()
        self._actor.position = position