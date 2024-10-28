from core.engine import *

from components.followcursor import FollowCursor
from components.spriterenderer import SpriteRenderer
from components.destroyonstart import DestroyOnStart


if __name__ == '__main__':
    game = Game()

    scene = Scene("TestScene")

    actor = scene.create_actor("Actor", Vector2(128, 128), 0, Vector2(1, 1))
    actor.add_component(SpriteRenderer("../resources/images/placeholder.png", 256, 256))
    actor.add_component(DestroyOnStart())

    cursor = scene.create_actor("Cursor", Vector2(0, 0), 0, Vector2(1, 1))
    cursor.add_component(FollowCursor())
    cursor.add_component(SpriteRenderer("../resources/images/placeholder.png", 64, 64, Color(0, 0, 255, 255)))

    scene.print_actor_names()

    game.run(scene)
