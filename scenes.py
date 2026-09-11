from pyray import *
from math import ceil

from assets import TextureManager
from config import GameConfig
from player import Player
from utils import Timer, getGameMousePosition

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

class MainMenu(Scene):
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
                            scenes["beach"].setCurrentScene()
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

class Beach(Scene):
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

scenes: dict[str, Scene] = {
    "main_menu": MainMenu(),
    "beach": Beach()
}

current_scene: Scene = scenes["main_menu"]
