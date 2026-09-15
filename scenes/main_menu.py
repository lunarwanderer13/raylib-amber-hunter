from pyray import *

import scenes.scene as scene

from assets import TextureManager
from config import GameConfig
from utils import Timer, getGameMousePosition

class MainMenu(scene.Scene):
    name: str = "MainMenu"
    size: Vector2 = GameConfig.virtual_resolution

    title_rect: Rectangle = Rectangle(64, 16, 48, 26)
    start_button_rect: Rectangle = Rectangle(-16, 51, 80, 24)
    settings_button_rect: Rectangle = Rectangle(-16, 86, 64, 18)
    credits_button_rect: Rectangle = Rectangle(-16, 118, 64, 18)
    exit_button_rect: Rectangle = Rectangle(-16, 150, 48, 26)
    rects: list[Rectangle] = [start_button_rect, settings_button_rect, credits_button_rect, exit_button_rect]

    start_button_timer: Timer = Timer(4)
    settings_button_timer: Timer = Timer(4)
    credits_button_timer: Timer = Timer(4)
    exit_button_timer: Timer = Timer(4)
    timers: list[Timer] = [start_button_timer, settings_button_timer, credits_button_timer, exit_button_timer]

    def onLoad(self) -> None:
        self.player.togglePlayer(False)

    def draw(self) -> None:
        for index, (rect, timer) in enumerate(zip(self.rects, self.timers)):
            if check_collision_point_rec(getGameMousePosition(), rect):
                timer.time = max(timer.time - get_frame_time(), 0)

                if is_mouse_button_pressed(MouseButton.MOUSE_BUTTON_LEFT):
                    match (index + 1):
                        case 1:
                            scene.scenes["beach"].setCurrentScene()
                        case _:
                            ...
            else:
                timer.time = min(1 / timer.start_time, timer.time + get_frame_time())

            rect.x = -16 * timer.time * timer.start_time

        # Title
        draw_texture_v(
            TextureManager.title,
            Vector2(self.title_rect.x, self.title_rect.y),
            WHITE
        )

        # Start button
        draw_texture_v(
            TextureManager.start_button,
            Vector2(self.start_button_rect.x, self.start_button_rect.y),
            WHITE
        )

        # Settings button
        draw_texture_v(
            TextureManager.settings_button,
            Vector2(self.settings_button_rect.x, self.settings_button_rect.y),
            WHITE
        )

        # Credits button
        draw_texture_v(
            TextureManager.credits_button,
            Vector2(self.credits_button_rect.x, self.credits_button_rect.y),
            WHITE
        )

        # Exit button
        draw_texture_v(
            TextureManager.exit_button,
            Vector2(self.exit_button_rect.x, self.exit_button_rect.y),
            WHITE
        )
