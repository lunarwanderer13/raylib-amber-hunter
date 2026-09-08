from pyray import *
from typing import Any

from assets import TextureManager
from config import GameConfig
from data import ConfigManager, DataManager
from player import Player
from scenes import Scene, scenes

def main() -> None:
    game_width: int = int(GameConfig.virtual_resolution.x)
    game_height: int = int(GameConfig.virtual_resolution.y)
    window_width: int = game_width * 4
    window_height: int = game_height * 4

    config: dict[str, Any] = ConfigManager.load()

    init_window(window_width, window_height, "Amber Hunter")
    set_window_position(
        round(get_monitor_width(get_current_monitor()) / 2 - get_screen_width() / 2),
        round(get_monitor_height(get_current_monitor()) / 2 - get_screen_height() / 2)
    )
    set_window_state(ConfigFlags.FLAG_WINDOW_RESIZABLE)

    if config["fullscreen"]:
        set_window_state(ConfigFlags.FLAG_FULLSCREEN_MODE)

        if config["borderless"]:
            set_window_state(ConfigFlags.FLAG_BORDERLESS_WINDOWED_MODE)

    set_target_fps(config["fps"])

    TextureManager.load()
    data: dict[str, Any] = DataManager.load()
    player: Player = Player(data, config["keybinds"])
    camera: Camera2D = Camera2D(
        Vector2(game_width / 2, game_height / 2),
        Vector2(player.position.x + player.size.x / 2, game_height / 2),
        0.0,
        1.0
    )

    current_scene: Scene = scenes["beach"]

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

        player.update()
        player.clamp(current_scene.size)

        camera.target = Vector2(
            clamp(
                player.position.x + player.size.x / 2,
                game_width / 2,
                current_scene.size.x - game_width / 2
            ),
            current_scene.size.y / 2
        )

        begin_mode_2d(camera)

        current_scene.draw()

        player.draw()

        end_mode_2d()

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
