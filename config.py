from pyray import *
from dataclasses import dataclass, field

from loot import Loot, Amber

@dataclass
class GameConfig:
    virtual_resolution: Vector2 = Vector2(320, 180)

    game_width: int = int(virtual_resolution.x)
    game_height: int = int(virtual_resolution.y)

    window_width: int = int(game_width * 4)
    window_height: int = int(game_height * 4)

    scale: float = 0
    draw_width: float = 0
    draw_height: float = 0
    offset_x: float = 0
    offset_y: float = 0

    @classmethod
    def calculate(cls):
        cls.scale: float = min(
            get_screen_width() / cls.game_width,
            get_screen_height() / cls.game_height
        )
        
        cls.draw_width: float = cls.game_width * cls.scale
        cls.draw_height: float = cls.game_height * cls.scale

        cls.offset_x: float = (get_screen_width() - cls.draw_width) / 2
        cls.offset_y: float = (get_screen_height() - cls.draw_height) / 2

@dataclass
class DefaultConfig:
    fps: int = 60
    fullscreen: bool = False
    borderless: bool = False

    keybinds: dict[str, KeyboardKey | int] = field(default_factory=lambda: {
        "walk_up": KeyboardKey.KEY_W,
        "walk_right": KeyboardKey.KEY_D,
        "walk_down": KeyboardKey.KEY_S,
        "walk_left": KeyboardKey.KEY_A,
        "run": KeyboardKey.KEY_LEFT_SHIFT,
        "interact": KeyboardKey.KEY_SPACE,
    })

@dataclass
class DefaultData:
    balance: int = 0
    bag: list[Loot | Amber] = field(default_factory=list)
