import pyray

from core import *


class TextRenderer(ActorComponent):

    def __init__(self, text: str, offset: Vector2 = Vector2(), centered: bool = True,
                 font_size: int = 24, spacing: int = 4, tint: Color = Color.WHITE):
        super().__init__()
        self.text: str = text
        self.offset: Vector2 = offset
        self.centered: bool = centered
        self.font_size: int = font_size
        self.spacing: int = spacing
        self.tint: Color = tint


    def on_draw(self, frame_time: float) -> None:
        font: pyray.Font = pyray.get_font_default()

        position: pyray.Vector2 = (self.actor.position + self.offset).to_rl_vector()

        origin: pyray.Vector2 = pyray.vector2_zero()

        if self.centered:
            origin = pyray.measure_text_ex(font, self.text, self.font_size, self.spacing)
            origin = pyray.vector2_scale(origin, 0.5)


        pyray.draw_text_pro(font,
                            self.text,
                            position,
                            origin,
                            self.actor.rotation,
                            self.font_size,
                            self.spacing,
                            self.tint)