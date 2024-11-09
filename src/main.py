import pyray

from core import *


from components.spriterenderer import SpriteRenderer
from components.collisionbox import CollisionBox
from components.testmotion import TestMotion
from components.ui.button import Button


def create_test_scene() -> Scene:
    scene = Scene("TestScene")

    button_actor = scene.create_actor("Button Actor", Vector2(0, 0))
    button_actor.add_component(TestMotion())
    button_actor.add_component(CollisionBox(256, 256))
    button_actor.add_component(SpriteRenderer("../resources/images/placeholder.png", 256, 256))
    button_actor.add_component(Button())
    button_component = button_actor.get_component(Button)
    #button_component.pressed.add_callback(lambda : print("Pressed"))

    return scene


if __name__ == '__main__':
    loaded_scene = Scene.load("../resources/scenes/test_scene.svcs")

    Game.run(loaded_scene, is_debug_mode=True)
