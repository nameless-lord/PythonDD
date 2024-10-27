from core.actorcomponent import ActorComponent
from pyray import *

class SpriteRenderer(ActorComponent):

    def __init__(self, texture_path: str, width: float, height: float, tint: Color = WHITE):
        super().__init__()
        self._texture_path: str = texture_path
        self._texture: Texture2D = None
        self._width: float = width
        self._height: float = height
        self._tint: Color = tint


    def on_start(self) -> None:
        self._texture = load_texture(self._texture_path)


    def on_draw(self, frame_time: float) -> None:
        if self._texture is None:
            return

        source_rect = Rectangle(
            0,
            0,
            self._texture.width,
            self._texture.height)

        dest_rect = Rectangle(
            self._actor.position.x,
            self._actor.position.y,
            self._width * self._actor.scale.x,
            self._height * self._actor.scale.y)

        origin = Vector2(self._width * 0.5, self._height * 0.5)

        draw_texture_pro(self._texture, source_rect, dest_rect, origin, self._actor.rotation, self._tint)


    def on_destroy(self) -> None:
        if self._texture is None:
            return

        unload_texture(self._texture)