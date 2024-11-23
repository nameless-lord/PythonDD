
from core import *
from components.characters.spoliage import Spoliage
from components.textrenderer import TextRenderer
from core.eventsystem import ActorComponent
class SpoliageView(ActorComponent):
    def __init__(self, spoliage: Spoliage, textrenderer: TextRenderer):
        super().__init__()
        self.__spoliage: Spoliage = spoliage  # Приватное поле для хранения ссылки на Spoliage
        self.__text_renderer: TextRenderer = textrenderer  # Приватное поле для хранения ссылки на TextRenderer

    def on_start(self):
        # Подписываемся на изменения порчи
        self.__spoliage.spoliage_changed.add_callback(self.on_spoliage_changed)

        # Вызываем начальное обновление порчи
        self.on_spoliage_changed()

    def on_spoliage_changed(self):
        # Обновляем текст в TextRenderer со значением текущей порчи
        if self.__text_renderer:
            self.__text_renderer.text = f"{self.__spoliage.current_spoliage}"


