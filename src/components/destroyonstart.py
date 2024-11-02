from core import *


class DestroyOnStart(ActorComponent):

    def on_start(self) -> None:
        self._actor.destroy()