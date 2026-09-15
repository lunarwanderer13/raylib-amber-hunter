from pyray import *
from math import ceil

import scenes.scene as scene

from assets import TextureManager
from config import GameConfig
from utils import Timer

class Beach(scene.Scene):
    name: str = "Beach"
    size: Vector2 = Vector2(GameConfig.virtual_resolution.x * 5, GameConfig.virtual_resolution.y)

    sea_area: Rectangle = Rectangle(0, 0, GameConfig.virtual_resolution.x * 5, GameConfig.virtual_resolution.y / 2)
    beach_area: Rectangle = Rectangle(0, GameConfig.virtual_resolution.y / 2, GameConfig.virtual_resolution.x * 5, GameConfig.virtual_resolution.y / 2)

    timer: Timer = Timer(4)

    def onLoad(self) -> None:
        self.player.togglePlayer(True)

    def draw(self) -> None:
        if self.timer.time > 0:
            self.timer.update()

        # Sea
        for y in self.getArea("y", self.sea_area):
            for x in self.getArea("x", self.sea_area):
                draw_texture_rec(
                    TextureManager.sea,
                    Rectangle((ceil(self.timer.time * 2) % 2) * TextureManager.tile_size, 0, TextureManager.tile_size, TextureManager.tile_size),
                    Vector2(x, y),
                    WHITE
                )

        # Beach
        for y in self.getArea("y", self.beach_area):
            for x in self.getArea("x", self.beach_area):
                draw_texture(TextureManager.sand, x, y, WHITE)

        # Waves
        for x in self.getArea("x", self.beach_area):
            draw_texture_rec(
                TextureManager.wave,
                Rectangle((ceil(self.timer.time) % 4) * TextureManager.tile_size, 0, TextureManager.tile_size, TextureManager.tile_size),
                Vector2(x, self.beach_area.y),
                WHITE
            )

        if self.timer.time <= 0:
            self.timer.reset()
