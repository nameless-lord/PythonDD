from core import *

if __name__ == '__main__':
    Game.init_window()

    scene = Scene("Scene")

    Game.run(scene, is_debug_mode=False)