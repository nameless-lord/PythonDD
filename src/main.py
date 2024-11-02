from core import *

from components.spriterenderer import SpriteRenderer
from components.collisionbox import CollisionBox
from components.ui.button import Button


if __name__ == '__main__':

    scene = Scene("TestScene")

    button_actor = scene.create_actor("Button Actor", Vector2(800, 450))
    button_actor.add_component(CollisionBox(256, 256))
    button_actor.add_component(SpriteRenderer("../resources/images/placeholder.png", 256, 256))
    button_actor.add_component(Button())
    button_component = button_actor.get_component(Button)
    button_component.pressed.add_callback(lambda : print("Pressed"))

    Game.run(scene, is_debug_mode=True)
