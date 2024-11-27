from pyray import *
from core.scene import Scene


class Game:

    SCREEN_WIDTH = 1600
    SCREEN_HEIGHT = 900

    RESOURCES_PATH = "../resources/"
    SCENES_PATH = "../resources/scenes/"
    ACTORS_PATH = "../resources/actors/"
    IMAGES_PATH = "../resources/images/"

    camera: Camera2D

    request_exit: bool = False

    __current_scene: Scene = None
    __new_scene: Scene = None
    __is_debug_mode: bool = False


    @staticmethod
    def get_current_scene() -> Scene:
        return Game.__current_scene


    @staticmethod
    def init_window():
        # Установка параметров
        set_trace_log_level(TraceLogLevel.LOG_WARNING)
        set_target_fps(60)

        # Создание окна
        init_window(Game.SCREEN_WIDTH, Game.SCREEN_HEIGHT, "Game")


    @staticmethod
    def run(start_scene: Scene, is_debug_mode: bool) -> None:
        Game.__current_scene = start_scene
        Game.__is_debug_mode = is_debug_mode

        # Инициализация камеры
        # noinspection PyArgumentList
        Game.camera = Camera2D()
        Game.camera.offset = Vector2(Game.SCREEN_WIDTH * 0.5, Game.SCREEN_HEIGHT * 0.5)
        Game.camera.zoom = 1

        # Основной игровой цикл
        while not window_should_close() and not Game.request_exit:
            frame_time: float = get_frame_time()

            if Game.__new_scene is not None:
                Game.__switch_scenes()

            # Обновление состояния объектов
            Game.__on_update(frame_time)

            # Отрисовка

            begin_drawing()
            clear_background(BLACK)

            begin_mode_2d(Game.camera)

            Game.__on_draw(frame_time)

            if Game.__is_debug_mode:
                Game.__on_debug_draw(frame_time)

            end_mode_2d()

            if Game.__is_debug_mode:
                draw_text(f"FPS: {get_fps()}", 5, 5, 20, DARKGREEN)
                draw_text(f"Frame time: {1000 * frame_time:.2f} ms", 5, 25, 20, DARKGREEN)

            end_drawing()

        # Очистка при закрытии
        Game.__on_close()

        close_window()


    @staticmethod
    def change_scene(scene: Scene):
        Game.__new_scene = scene


    @staticmethod
    def exit():
        Game.request_exit = True


    @staticmethod
    def __on_update(frame_time: float) -> None:
        for actor in Game.__current_scene.actors:
            if actor.is_destroyed:
                continue

            for component in actor.components:
                if not component.is_started:
                    component.start()
                component.on_update(frame_time)

        Game.__current_scene.remove_destroyed_actors()


    @staticmethod
    def __on_draw(frame_time: float) -> None:
        for actor in Game.__current_scene.actors:
            for component in actor.components:
                component.on_draw(frame_time)


    @staticmethod
    def __on_debug_draw(frame_time: float) -> None:
        for actor in Game.__current_scene.actors:
            for component in actor.components:
                component.on_debug_draw(frame_time)


    @staticmethod
    def __on_close() -> None:
        Game.__current_scene.close()


    @staticmethod
    def __switch_scenes():
        Game.__current_scene.close()
        Game.__current_scene = Game.__new_scene
        Game.__new_scene = None