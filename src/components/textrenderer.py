import pyray

from core import *


class TextRenderer(ActorComponent):

    def __init__(self, text: str, centered: bool = True, font_size: int = 24, spacing: int = 4, tint: Color = Color.WHITE):
        super().__init__()
        self.text: str = text
        self.centered: bool = centered
        self.font_size: int = font_size
        self.spacing: int = spacing
        self.tint: Color = tint


    def on_draw(self, frame_time: float) -> None:
        font: pyray.Font = pyray.get_font_default()

        origin: pyray.Vector2 = pyray.vector2_zero()

        if self.centered:
            origin = pyray.measure_text_ex(font, self.text, self.font_size, self.spacing)
            origin = pyray.vector2_scale(origin, 0.5)


        pyray.draw_text_pro(font,
                            self.text,
                            self._actor.position.to_rl_vector(),
                            origin,
                            self._actor.rotation,
                            self.font_size,
                            self.spacing,
                            self.tint)