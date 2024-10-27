import pyray

from components.followcursor import FollowCursor
from components.spriterenderer import SpriteRenderer
from core.game import Game
from core.scene import Scene

from pyray import Vector2

if __name__ == '__main__':
    game = Game()

    scene = Scene("TestScene")

    actor = scene.create_actor("A2", Vector2(128, 128), 0, Vector2(1, 1))
    actor.add_component(SpriteRenderer("resources/images/placeholder.png", 256, 256))

    actor = scene.create_actor("A", Vector2(0, 0), 0, Vector2(1, 1))
    actor.add_component(FollowCursor())
    actor.add_component(SpriteRenderer("resources/images/placeholder.png", 64, 64, pyray.BLUE))

    scene.print_actor_names()

    game.run(scene)
