from core.actor import Actor
from pyray import Vector2


class Scene:

    @property
    def actors(self) -> list[Actor]:
        return self._actors


    def __init__(self, name: str):
        self._actors: list[Actor] = list()
        self._destroyed_actors: list[Actor] = list()
        self._name: str = name


    def create_actor(self, name: str, position: Vector2, rotation: float, scale: Vector2) -> Actor:
        actor: Actor = Actor(self, name, position, rotation, scale)
        self._actors.append(actor)
        return actor


    def destroy_actor(self, actor: Actor) -> None:
        self._destroyed_actors.append(actor)
        actor.on_destroy()


    def remove_destroyed_actors(self) -> None:
        for actor in self._destroyed_actors:
            self._actors.remove(actor)

        self._destroyed_actors.clear()


    def print_actor_names(self) -> None:
        print(f"{self._name}:")
        for actor in self._actors:
            print(actor)