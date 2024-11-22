from components.ui.button import Button
from core import *

class ExitButton(Button):
    def on_start(self) -> None:
        super().on_start()
        self.pressed.add_callback(Game.exit)