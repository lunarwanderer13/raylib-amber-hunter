from pyray import *
from math import ceil

from assets import TextureManager
from config import GameConfig
from timer import Timer

class Scene:
    name: str = ""
    size: Vector2 = Vector2(0, 0)

    def getArea(self, axis: str, rect: Rectangle) -> range:
        match(axis):
            case "x":
                return range(int(rect.x), int(rect.x + rect.width) + TextureManager.tile_size - 1, TextureManager.tile_size)
            case "y":
                return range(int(rect.y), int(rect.y + rect.height) + TextureManager.tile_size - 1, TextureManager.tile_size)
            case _:
                raise ValueError("Argument axis of Scene.getArea only accepts x or y as values.")

    def draw(self) -> None:
        ...

class Beach(Scene):
    name: str = "Beach"
    size: Vector2 = Vector2(GameConfig.virtual_resolution.x * 5, GameConfig.virtual_resolution.y)

    sea_area: Rectangle = Rectangle(0, 0, GameConfig.virtual_resolution.x * 5, GameConfig.virtual_resolution.y / 2)
    beach_area: Rectangle = Rectangle(0, GameConfig.virtual_resolution.y / 2, GameConfig.virtual_resolution.x * 5, GameConfig.virtual_resolution.y / 2)

    timer: Timer = Timer(4)

    def draw(self) -> None:
        if self.timer.time > 0:
            self.timer.update()

        for y in self.getArea("y", self.sea_area):
            for x in self.getArea("x", self.sea_area):
                draw_texture_rec(
                    TextureManager.sea,
                    Rectangle((ceil(self.timer.time * 2) % 2) * TextureManager.tile_size, 0, TextureManager.tile_size, TextureManager.tile_size),
                    Vector2(x, y),
                    WHITE
                )

        for y in self.getArea("y", self.beach_area):
            for x in self.getArea("x", self.beach_area):
                draw_texture(TextureManager.sand, x, y, WHITE)

        for x in self.getArea("x", self.beach_area):
            draw_texture_rec(
                TextureManager.wave,
                Rectangle((ceil(self.timer.time) % 4) * TextureManager.tile_size, 0, TextureManager.tile_size, TextureManager.tile_size),
                Vector2(x, self.beach_area.y),
                WHITE
            )

        if self.timer.time <= 0:
            self.timer.time = 4

scenes: dict[str, Scene] = {
    "beach": Beach()
}
