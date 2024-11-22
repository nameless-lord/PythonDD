import pickle
from typing import Type

from core.actor import Actor
from core.actorcomponent import  ActorComponent
from .vector2 import Vector2


class Scene:

    @property
    def actors(self) -> list[Actor]:
        return self.__actors


    def __init__(self, name: str):
        self.__actors: list[Actor] = list()
        self.__destroyed_actors: list[Actor] = list()
        self.__name: str = name


    def save(self, file_path: str):
        with open(file_path, 'wb') as file:
            pickle.dump(self, file, 0)


    def create_actor(self, name: str, position: Vector2, rotation: float = 0, scale: Vector2 = Vector2(1, 1)) -> Actor:
        actor: Actor = Actor(self, name, position, rotation, scale)
        self.actors.append(actor)
        return actor


    def create_actor_from_file(self, file_path: str) -> Actor:
        with open(file_path, 'rb') as file:
            actor: Actor = pickle.load(file)

        actor.set_scene(self)

        self.actors.append(actor)
        return actor


    def destroy_actor(self, actor: Actor) -> None:
        self.__destroyed_actors.append(actor)
        actor.on_destroy()


    def remove_destroyed_actors(self) -> None:
        for actor in self.__destroyed_actors:
            self.actors.remove(actor)

        self.__destroyed_actors.clear()


    def find_component[T: ActorComponent](self, component_type: Type[T]) -> T:
        for actor in self.actors:
            component = actor.get_component(component_type)
            if component is not None:
                return component


    def print_actor_names(self) -> None:
        print(f"{self.__name}:")
        for actor in self.actors:
            print(actor)


    def close(self):
        for actor in self.actors:
            self.destroy_actor(actor)


    @staticmethod
    def load(file_path: str) -> 'Scene':
        with open(file_path, 'rb') as file:
            return pickle.load(file)