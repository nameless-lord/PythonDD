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


    # Вызывается перед первым on_uptate, используется для инициализации
    def on_start(self) -> None:
        pass


    # Вызывается каждый кадр перед on_draw
    def on_update(self, frame_time: float) -> None:
        pass


    # Вызывается каждый кадр во время отрисовки
    def on_draw(self, frame_time: float) -> None:
        pass


    # Вызывается каждый кадр во время отрисовки (для отладки)
    def on_debug_draw(self, frame_time: float) -> None:
        pass


    # Вызывается при уничтожении
    def on_destroy(self) -> None:
        pass