import pyray

from core import *


class TextRenderer(ActorComponent):

    def __init__(self, text: str, offset: Vector2, font_size: int = 24, color: Color = pyray.WHITE):
        super().__init__()
        self.text = text
        self.offset = offset
        self.font_size = font_size
        self.color = color


    def on_draw(self, frame_time: float) -> None:
        font: pyray.Font = pyray.get_font_default()
        pyray.draw_text_pro(font,
                            self.text,
                            self._actor.position,
                            pyray.vector2_negate(self.offset),
                            self._actor.rotation,
                            self.font_size,
                            4,
                            self.color)