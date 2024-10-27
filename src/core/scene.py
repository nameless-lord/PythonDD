from core.actor import Actor
from pyray import Vector2


class Scene:

    @property
    def actors(self) -> list[Actor]:
        return self._actors


    def __init__(self, name: str):
        self._actors: list[Actor] = list()
        self._name: str = name


    def create_actor(self, name: str, position: Vector2, rotation: float, scale: Vector2) -> Actor:
        actor: Actor = Actor(self, name, position, rotation, scale)
        self._actors.append(actor)
        return actor


    def print_actor_names(self) -> None:
        print(f"{self._name}:")
        for actor in self._actors:
            print(actor)