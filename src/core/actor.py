import core.scene
from typing import Type
from .actorcomponent import ActorComponent
from pyray import Vector2


class Actor:

    @property
    def components(self) -> list[ActorComponent]:
        return self._components


    @property
    def is_destroyed(self) -> bool:
        return self._is_destroyed


    def __init__(self, scene: 'core.scene.Scene', name: str,
                 position: Vector2, rotation: float = 0, scale: Vector2 = Vector2(1, 1)):
        self.name: str = name
        self.position: Vector2 = position
        self.rotation: float = rotation
        self.scale: Vector2 = scale
        self._scene: 'core.scene.Scene' = scene
        self._components: list[ActorComponent] = list()
        self._is_destroyed: bool = False


    def __str__(self):
        return f"{self.name}_{id(self)}"


    def add_component(self, component: ActorComponent) -> None:
        self._components.append(component)
        component.set_actor(self)


    def get_component[T: ActorComponent](self, component_type: Type[T]) -> T:
        for component in self._components:
            if type(component) is component_type:
                return component


    def destroy(self):
        self._scene.destroy_actor(self)


    def on_destroy(self) -> None:
        self._is_destroyed = True
        for component in self._components:
            component.on_destroy()