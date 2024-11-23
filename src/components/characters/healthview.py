from core import *
from components.characters.health import Health
from components.textrenderer import TextRenderer
class HealthView(ActorComponent):
    def __init__(self):
        super().__init__()
        self.__health: Health = None  # Приватное поле для хранения ссылки на Health
        self.__text_renderer: TextRenderer = None  # Приватное поле для хранения ссылки на TextRenderer

    def on_start(self):
        # Получаем компонент Health
        self.__health = self.actor.get_component(Health)

        # Получаем компонент TextRenderer
        self.__text_renderer = self.actor.get_component(TextRenderer)

        # Подписываемся на изменения здоровья
        self.__health.health_changed.add_callback(self.on_health_changed)

        # Вызываем начальное обновление здоровья
        self.on_health_changed()

    def on_health_changed(self):
        # Обновляем текст в TextRenderer со значением текущего и максимального здоровья
        if self.__text_renderer:
            self.__text_renderer.text = f"{self.__health.current_health}/{self.__health.max_health}"
