from components.ui.button import Button
from core import *


class StartButton(Button):
    def on_start(self) -> None:
        super().on_start()
        level_selection_scene = Scene.load(Game.SCENES_PATH + "level_selection.svsc")
        self.pressed.add_callback(lambda : Game.change_scene(level_selection_scene))