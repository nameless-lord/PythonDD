import core

class ActorComponent:

    @property
    def is_started(self) -> bool:
        return self._is_started


    @property
    def actor(self) -> 'core.actor.Actor':
        return self._actor


    def __init__(self):
        self._actor: 'core.actor.Actor' = None
        self._is_started: bool = False


    def set_actor(self, actor: 'core.actor.Actor'):
        self._actor = actor


    def start(self) -> None:
        self._is_started = True
        self.on_start()


    def on_start(self) -> None:
        pass


    def on_update(self, frame_time: float) -> None:
        pass


    def on_draw(self, frame_time: float) -> None:
        pass


    def on_debug_draw(self, frame_time: float) -> None:
        pass


    def on_destroy(self) -> None:
        pass