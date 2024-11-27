from components.characters.damageovertime import DamageOverTime
from components.characters.damageresponse import DamageResponse
from components.characters.health import Health
from components.characters.healthview import HealthView
from components.characters.playerstate import PlayerState
from components.characters.spawnondeath import SpawnOnDeath
from components.collisionbox import CollisionBox
from components.spriterenderer import SpriteRenderer
from components.textrenderer import TextRenderer
from components.ui.button import Button
from components.ui.exitbutton import ExitButton
from core import *

def create_main_menu() -> Scene:
    scene = Scene("MainMenu")

    sb = scene.create_actor("StartButton", Vector2(0, -50))
    sb.add_component(TextRenderer("Start", font_size=64, spacing=4))
    size = pyray.measure_text_ex(pyray.get_font_default(), "Start", 64, 4)
    sb.add_component(CollisionBox(size.x, size.y))
    sb.add_component(Button())
    sb.get_component(Button).pressed.add_callback(lambda : Game.change_scene(create_sample_scene()))

    eb = scene.create_actor("ExitButton", Vector2(0, 50))
    eb.add_component(TextRenderer("Exit", font_size=64, spacing=4))
    size = pyray.measure_text_ex(pyray.get_font_default(), "Exit", 64, 4)
    eb.add_component(CollisionBox(size.x, size.y))
    eb.add_component(ExitButton())

    return scene


def create_sample_scene() -> Scene:
    scene = Scene("Sample")
    background = scene.create_actor("Background", Vector2())
    background.add_component(SpriteRenderer(Game.IMAGES_PATH + "background.png", 1600, 900))

    player_state_actor = scene.create_actor("PlayerState", Vector2(-700, -400))
    player_state = player_state_actor.add_component(PlayerState())
    player_state.gold_changed.add_callback(lambda : update_gold_text(player_state))
    player_state_actor.add_component(TextRenderer("Gold", tint=Color.YELLOW))

    enemy = scene.create_actor("NewEnemy", Vector2())
    enemy.add_component(SpriteRenderer(Game.IMAGES_PATH + "character1.png", 256, 256))
    enemy.add_component(CollisionBox(128, 256))
    enemy_health = enemy.add_component(Health(300))
    enemy_text = enemy.add_component(TextRenderer("", offset=Vector2(0, -150)))
    enemy.add_component(HealthView(enemy_health, enemy_text))
    enemy_button = enemy.add_component(Button())
    enemy_button.pressed.add_callback(lambda: enemy_health.take_damage(7))
    enemy.add_component(DamageResponse())
    enemy.add_component(SpawnOnDeath())

    dot_damage_button = scene.create_actor("Dot", Vector2(-600, 400))
    text = "Add dot damage (cost 100)"
    dot_damage_button.add_component(TextRenderer(text, tint=Color.RED))
    size = pyray.measure_text_ex(pyray.get_font_default(), text, 24, 4)
    dot_damage_button.add_component(CollisionBox(size.x, size.y))
    dot_damage_button.add_component(Button())
    dot_damage_button.get_component(Button).pressed.add_callback(dot_button_response)

    return scene


def update_gold_text(player_state: PlayerState) -> None:
    tr = player_state.actor.get_component(TextRenderer)
    tr.text = f"Gold: {player_state.gold}"


def dot_button_response() -> None:
    health = Game.get_current_scene().find_component(Health)
    if health is None:
        return

    enemy = health.actor
    if enemy.scene.find_component(PlayerState).gold > 100:
        enemy.add_component(DamageOverTime(1, 1.5))
        enemy.scene.find_component(PlayerState).remove_gold(100)


if __name__ == '__main__':
    Game.init_window()

    scene = create_main_menu()

    Game.run(scene, is_debug_mode=False)