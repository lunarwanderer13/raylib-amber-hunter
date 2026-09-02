from pyray import *
from dataclasses import dataclass, field

from loot import Loot, Amber

@dataclass
class GameConfig:
    virtual_resolution: Vector2 = Vector2(320, 180)

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
