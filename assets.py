from pyray import *
from pathlib import Path

class TextureManager:
    tile_size: int = 16
    path: Path = Path("assets/sprites/")

    sea: Texture
    wave: Texture
    sand: Texture

    @classmethod
    def load(cls) -> None:
        cls.sea: Texture = load_texture(str(cls.path.joinpath("terrain/sea.png")))
        cls.wave: Texture = load_texture(str(cls.path.joinpath("terrain/wave.png")))
        cls.sand: Texture = load_texture(str(cls.path.joinpath("terrain/sand.png")))

    @classmethod
    def unload(cls) -> None:
        unload_texture(cls.sea)
        unload_texture(cls.wave)
        unload_texture(cls.sand)
