from typing import Callable


class Event[**P]:
    def __init__(self):
        self._callbacks: list[Callable[P, None]] = list()


    def add_callback(self, callback: Callable[P, None]):
        self._callbacks.append(callback)


    def remove_callback(self, callback: Callable[P, None]):
        self._callbacks.remove(callback)


    def invoke(self, *args: P.args, **kwargs: P.kwargs):
        for callback in self._callbacks:
            callback(*args, **kwargs)