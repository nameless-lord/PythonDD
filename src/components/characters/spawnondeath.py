from components.characters.damageresponse import DamageResponse
from components.characters.health import Health
from components.characters.healthview import HealthView
from components.collisionbox import CollisionBox
from components.spriterenderer import SpriteRenderer
from components.textrenderer import TextRenderer
from components.ui.button import Button
from core import *


class SpawnOnDeath(ActorComponent):
    def on_destroy(self) -> None:
        enemy = Game.get_current_scene().create_actor("NewEnemy", Vector2())
        enemy.add_component(SpriteRenderer(Game.IMAGES_PATH + "character2.png", 400, 400))
        enemy.add_component(CollisionBox(140, 286))
        enemy_health = enemy.add_component(Health(3000))
        enemy_text = enemy.add_component(TextRenderer("", offset=Vector2(0, -180)))
        enemy.add_component(HealthView(enemy_health, enemy_text))
        enemy_button = enemy.add_component(Button())
        enemy_button.pressed.add_callback(lambda: enemy_health.take_damage(7))
        enemy.add_component(DamageResponse())