from pyray import *

from config import GameConfig

class Timer:
    def __init__(self, time: float = 0) -> None:
        self.start_time: float = time
        self.time: float = time

    def update(self) -> None:
        self.time -= get_frame_time()

    def reset(self) -> None:
        self.time = self.start_time

def getGameMousePosition() -> Vector2:
    mouse: Vector2 = get_mouse_position()

    return Vector2(
        (mouse.x - GameConfig.offset_x) / GameConfig.scale,
        (mouse.y - GameConfig.offset_y) / GameConfig.scale
    )