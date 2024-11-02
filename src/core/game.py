from pyray import *
from core.scene import Scene


class Game:

    SCREEN_WIDTH = 1600
    SCREEN_HEIGHT = 900

    camera: Camera2D

    request_exit: bool = False

    _current_scene: Scene = None
    _is_debug_mode: bool = False


    @staticmethod
    def run(start_scene: Scene, is_debug_mode: bool) -> None:
        set_trace_log_level(TraceLogLevel.LOG_WARNING)
        set_target_fps(60)

        init_window(Game.SCREEN_WIDTH, Game.SCREEN_HEIGHT, "Game")

        Game._current_scene = start_scene
        Game._is_debug_mode = is_debug_mode

        # noinspection PyArgumentList
        Game.camera = Camera2D()
        Game.camera.offset = Vector2(Game.SCREEN_WIDTH * 0.5, Game.SCREEN_HEIGHT * 0.5)
        Game.camera.zoom = 1


        while not window_should_close() and not Game.request_exit:
            frame_time: float = get_frame_time()

            Game._on_update(frame_time)

            begin_drawing()
            clear_background(BLACK)

            begin_mode_2d(Game.camera)

            Game._on_draw(frame_time)
            if Game._is_debug_mode:
                Game._on_debug_draw(frame_time)

            end_mode_2d()

            if Game._is_debug_mode:
                draw_text(f"FPS: {get_fps()}", 5, 5, 20, DARKGREEN)
                draw_text(f"Frame time: {1000 * frame_time:.2f} ms", 5, 25, 20, DARKGREEN)

            end_drawing()

        Game._on_close()

        close_window()


    @staticmethod
    def _on_update(frame_time: float) -> None:
        for actor in Game._current_scene.actors:
            if actor.is_destroyed:
                continue

            for component in actor.components:
                if not component.is_started:
                    component.start()
                component.on_update(frame_time)

        Game._current_scene.remove_destroyed_actors()


    @staticmethod
    def _on_draw(frame_time: float) -> None:
        for actor in Game._current_scene.actors:
            for component in actor.components:
                component.on_draw(frame_time)


    @staticmethod
    def _on_debug_draw(frame_time: float) -> None:
        for actor in Game._current_scene.actors:
            for component in actor.components:
                component.on_debug_draw(frame_time)


    @staticmethod
    def _on_close() -> None:
        for actor in Game._current_scene.actors:
            Game._current_scene.destroy_actor(actor)