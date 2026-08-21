from pyray import *
from typing import Any

from config import GameConfig
from data import ConfigManager

def main() -> None:
    game_width: int = int(GameConfig.virtual_resolution.x)
    game_height: int = int(GameConfig.virtual_resolution.y)
    window_width: int = game_width * 4
    window_height: int = game_height * 4

    config: dict[str, Any] = ConfigManager.load()

    init_window(window_width, window_height, "Amber Hunter")
    set_window_state(ConfigFlags.FLAG_WINDOW_RESIZABLE)

    if config["fullscreen"]:
        set_window_state(ConfigFlags.FLAG_FULLSCREEN_MODE)

        if config["borderless"]:
            set_window_state(ConfigFlags.FLAG_BORDERLESS_WINDOWED_MODE)

    set_target_fps(config["fps"])

    target: RenderTexture = load_render_texture(game_width, game_height)
    set_texture_filter(target.texture, TextureFilter.TEXTURE_FILTER_POINT)

    while not window_should_close():
        scale: float = min(
            get_screen_width() / game_width,
            get_screen_height() / game_height
        )

        draw_width: float = game_width * scale
        draw_height: float = game_height * scale

        offset_x: float = (get_screen_width() - draw_width) / 2
        offset_y: float = (get_screen_height() - draw_height) / 2



        begin_texture_mode(target)

        clear_background(RAYWHITE)

        end_texture_mode()



        begin_drawing()

        clear_background(BLACK)

        draw_texture_pro(
            target.texture,
            Rectangle(0, 0, game_width, -game_height),
            Rectangle(offset_x, offset_y, draw_width, draw_height),
            Vector2(0, 0),
            0,
            WHITE
        )

        end_drawing()

    close_window()

if __name__ == "__main__":
    main()
