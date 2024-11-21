import pickle
from typing import Type

from core.actor import Actor
from core.actorcomponent import  ActorComponent
from .vector2 import Vector2


class Scene:

    @property
    def actors(self) -> list[Actor]:
        return self._actors


    def __init__(self, name: str):
        self._actors: list[Actor] = list()
        self._destroyed_actors: list[Actor] = list()
        self._name: str = name


    def save(self, file_path: str):
        with open(file_path, 'wb') as file:
            pickle.dump(self, file, 0)


    def create_actor(self, name: str, position: Vector2, rotation: float = 0, scale: Vector2 = Vector2(1, 1)) -> Actor:
        actor: Actor = Actor(self, name, position, rotation, scale)
        self._actors.append(actor)
        return actor


    def create_actor_from_file(self, file_path: str) -> Actor:
        with open(file_path, 'rb') as file:
            actor: Actor = pickle.load(file)

        actor._scene = self

        self._actors.append(actor)
        return actor


    def destroy_actor(self, actor: Actor) -> None:
        self._destroyed_actors.append(actor)
        actor.on_destroy()


    def remove_destroyed_actors(self) -> None:
        for actor in self._destroyed_actors:
            self._actors.remove(actor)

        self._destroyed_actors.clear()


    def find_component[T: ActorComponent](self, component_type: Type[T]) -> T:
        for actor in self._actors:
            component = actor.get_component(component_type)
            if component is not None:
                return component


    def print_actor_names(self) -> None:
        print(f"{self._name}:")
        for actor in self._actors:
            print(actor)


    def close(self):
        for actor in self._actors:
            self.destroy_actor(actor)


    @staticmethod
    def load(file_path: str) -> 'Scene':
        with open(file_path, 'rb') as file:
            return pickle.load(file)