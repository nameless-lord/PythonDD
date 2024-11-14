from core import *

if __name__ == '__main__':
    Game.init_window()

    scene = Scene.load(Game.SCENES_PATH + "main_menu.svsc")

    Game.run(scene, is_debug_mode=False)