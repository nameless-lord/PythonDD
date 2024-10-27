from typing import Callable


class Event:
    def __init__(self):
        self._callbacks: list[Callable] = list()


    def add_listener(self, callback: Callable):
        self._callbacks.append(callback)


    def remove_listener(self, callback: Callable):
        self._callbacks.remove(callback)


    def invoke(self):
        for callback in self._callbacks:
            callback()