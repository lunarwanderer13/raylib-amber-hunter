from pyray import *
from importlib import import_module

from assets import TextureManager
from player import Player

class Scene:
    name: str = ""
    size: Vector2 = Vector2(0, 0)
    player: Player

    def getArea(self, axis: str, rect: Rectangle) -> range:
        match(axis):
            case "x":
                return range(int(rect.x), int(rect.x + rect.width) + TextureManager.tile_size - 1, TextureManager.tile_size)
            case "y":
                return range(int(rect.y), int(rect.y + rect.height) + TextureManager.tile_size - 1, TextureManager.tile_size)
            case _:
                raise ValueError("Argument axis of Scene.getArea only accepts x or y as values.")

    def setCurrentScene(self) -> Scene:
        global current_scene
        current_scene = self
        return current_scene

    def onLoad(self) -> None:
        ...

    def draw(self) -> None:
        ...

scenes: dict[str, Scene] = {
    "main_menu": import_module("scenes.main_menu").MainMenu(),
    "beach": import_module("scenes.beach").Beach()
}

current_scene: Scene = scenes["main_menu"]
