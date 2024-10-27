from pyray import *

from core.scene import Scene


class Game:

    def __init__(self):
        self._current_scene: Scene = None


    def run(self, start_scene: Scene) -> None:

        set_trace_log_level(TraceLogLevel.LOG_WARNING)
        set_target_fps(60)

        init_window(1600, 900, "Game")

        self._current_scene = start_scene

        while not window_should_close():
            frame_time: float = get_frame_time()

            self.on_update(frame_time)

            begin_drawing()
            clear_background(BLACK)
            self.on_draw(frame_time)

            draw_text(f"FPS: {get_fps()}", 5, 5, 20, DARKGREEN)
            draw_text(f"Frame time: {1000 * frame_time:.2f} ms", 5, 25, 20, DARKGREEN)

            end_drawing()

        self.on_close()

        close_window()


    def on_update(self, frame_time: float) -> None:
        for actor in self._current_scene.actors:
            for component in actor.components:
                if not component.is_started:
                    component.start()
                component.on_update(frame_time)


    def on_draw(self, frame_time) -> None:
        for actor in self._current_scene.actors:
            for component in actor.components:
                component.on_draw(frame_time)


    def on_close(self) -> None:
        for actor in self._current_scene.actors:
            for component in actor.components:
                component.on_destroy()