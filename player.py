from pyray import *
from typing import Any

from loot import Loot, Amber

class Player:
    def __init__(self, data: dict[str, Any], keybinds: dict[str, KeyboardKey | int]) -> None:
        self.data: dict[str, Any] = data
        self.balance: int = data["balance"]
        self.bag: list[Loot | Amber] = data["bag"]
        self.keybinds: dict[str, KeyboardKey | int] = keybinds

        self.is_active: bool = False
        self.is_hidden: bool = True
        self.position: Vector2 = Vector2(0, 0)
        self.movement: Vector2 = Vector2(0, 0)
        self.movement_speed: int = 50
        self.run_speed: float = 2.0
        self.is_running: bool = False
        self.is_colliding: bool = False
        self.can_interact: bool = False
        
        self.size: Vector2 = Vector2(16, 16)
        self.rect: Rectangle = Rectangle(
            self.position.x, self.position.y - self.size.y,
            self.size.x, self.size.y
        )
        self.collision_rect: Rectangle = Rectangle(
            self.position.x, self.position.y,
            self.size.x, 1
        )

    def togglePlayer(self, is_enabled: bool) -> None:
        self.is_active = is_enabled
        self.is_hidden = not is_enabled

    def canMove(self) -> bool:
        return (
            self.is_active
            and self.movement_speed > 0
            and not self.is_colliding
        )

    def move(self) -> None:
        if is_key_down(self.keybinds["walk_up"]):
            self.movement.y = -1
        if is_key_down(self.keybinds["walk_right"]):
            self.movement.x = 1
        if is_key_down(self.keybinds["walk_down"]):
            self.movement.y = 1
        if is_key_down(self.keybinds["walk_left"]):
            self.movement.x = -1

        if is_key_down(self.keybinds["walk_up"]) and is_key_down(self.keybinds["walk_down"]):
            self.movement.y = 0
        if is_key_down(self.keybinds["walk_left"]) and is_key_down(self.keybinds["walk_right"]):
            self.movement.x = 0

        if is_key_up(self.keybinds["walk_up"]) and is_key_up(self.keybinds["walk_down"]):
            self.movement.y = 0
        if is_key_up(self.keybinds["walk_left"]) and is_key_up(self.keybinds["walk_right"]):
            self.movement.x = 0

        length: float = vector2_length_sqr(self.movement)

        if length > 0:
            self.movement.x /= length
            self.movement.y /= length

        if self.is_running:
            self.movement.x *= self.run_speed
            self.movement.y *= self.run_speed

        self.position.x += round(self.movement.x * self.movement_speed * get_frame_time(), 2)
        self.position.y += round(self.movement.y * self.movement_speed * get_frame_time(), 2)

    def clamp(self, scene_size: Vector2) -> None:
        self.position.x = clamp(
            self.position.x,
            0,
            scene_size.x - self.collision_rect.width
        )
        self.position.y = clamp(
            self.position.y,
            self.collision_rect.height - 1,
            scene_size.y - 1
        )

        self.rect.x = self.position.x
        self.rect.y = self.position.y - self.size.y

        self.collision_rect.x = self.position.x
        self.collision_rect.y = self.position.y

    def draw(self) -> None:
        if self.is_hidden:
            return

        draw_rectangle_rec(self.rect, BLUE)
        draw_rectangle_rec(self.collision_rect, YELLOW)
        draw_pixel_v(self.position, BLACK)

    def update(self) -> None:
        self.is_running = is_key_down(self.keybinds["run"])

        if self.canMove():
            self.move()
