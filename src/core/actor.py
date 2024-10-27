import core
from pyray import Vector2
from core.actorcomponent import ActorComponent


class Actor:

    @property
    def components(self) -> list[ActorComponent]:
        return self._components


    def __init__(self, scene: 'core.scene.Scene', name: str,
                 position: Vector2, rotation: float = 0, scale: Vector2 = Vector2(1, 1)):
        self.name: str = name
        self.position: Vector2 = position
        self.rotation: float = rotation
        self.scale: Vector2 = scale
        self._scene: 'core.scene.Scene' = scene
        self._components: list[ActorComponent] = list()


    def add_component(self, component: ActorComponent) -> None:
        self._components.append(component)
        component.set_actor(self)


    def __str__(self):
        return f"{self.name}_{id(self)}"