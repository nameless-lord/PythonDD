import pickle
import core.scene
from typing import Type

from .actorcomponent import ActorComponent
from .vector2 import Vector2


class Actor:

    @property
    def components(self) -> list[ActorComponent]:
        return self.__components


    @property
    def scene(self) -> 'core.scene.Scene':
        return self.__scene


    @property
    def is_destroyed(self) -> bool:
        return self.__is_destroyed


    def __init__(self, scene: 'core.scene.Scene', name: str,
                 position: Vector2, rotation: float = 0, scale: Vector2 = Vector2(1, 1)):
        self.name: str = name
        self.position: Vector2 = position
        self.rotation: float = rotation
        self.scale: Vector2 = scale
        self.__scene: 'core.scene.Scene' = scene
        self.__components: list[ActorComponent] = list()
        self.__is_destroyed: bool = False


    def __str__(self):
        return f"{self.name}_{id(self)}"


    def __getstate__(self):
        state = self.__dict__.copy()
        del state['_Actor__scene']
        del state['_Actor__is_destroyed']
        return state


    def __setstate__(self, state):
        self.__dict__.update(state)
        self.__is_destroyed = False


    def add_component[T: ActorComponent](self, component: T) -> T:
        self.__components.append(component)
        component.set_actor(self)
        return component


    def get_component[T: ActorComponent](self, component_type: Type[T]) -> T:
        for component in self.__components:
            if type(component) is component_type:
                return component


    def destroy(self):
        self.__scene.destroy_actor(self)


    def on_destroy(self) -> None:
        self.__is_destroyed = True
        for component in self.__components:
            component.on_destroy()


    def save(self, file_path: str):
        with open(file_path, 'wb') as file:
            pickle.dump(self, file, 0)


    def set_scene(self, scene):
        self.__scene = scene