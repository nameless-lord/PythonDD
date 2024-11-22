from core import *
from pyray import *


class SpriteRenderer(ActorComponent):

    def __init__(self, texture_path: str, width: float, height: float):
        super().__init__()
        self.__texture_path: str = texture_path
        self.__texture: Texture = None
        self.__width: float = width
        self.__height: float = height


    def __getstate__(self):
        state = self.__dict__.copy()
        del state['_SpriteRenderer__texture']
        return state


    def __setstate__(self, state):
        self.__dict__.update(state)
        self.__texture = None


    def on_start(self) -> None:
        self.__texture = load_texture(self.__texture_path)


    def on_draw(self, frame_time: float) -> None:
        if self.__texture is None:
            return

        source_rect = Rectangle(
            0,
            0,
            self.__texture.width,
            self.__texture.height)

        dest_rect = Rectangle(
            self.actor.position.x,
            self.actor.position.y,
            self.__width * self.actor.scale.x,
            self.__height * self.actor.scale.y)

        origin = Vector2(self.__width * 0.5, self.__height * 0.5)

        draw_texture_pro(self.__texture, source_rect, dest_rect, origin, self.actor.rotation, WHITE)


    def on_destroy(self) -> None:
        if self.__texture is None:
            return

        unload_texture(self.__texture)