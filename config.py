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

@dataclass
class DefaultData:
    balance: int = 0
    bag: list[Loot | Amber] = field(default_factory=list)
