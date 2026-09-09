from pyray import *
from pathlib import Path

class TextureManager:
    tile_size: int = 16
    path: Path = Path("assets/sprites/")

    # Terrain
    sea: Texture
    wave: Texture
    sand: Texture

    # UI
    title: Texture
    start_button: Texture
    settings_button: Texture
    credits_button: Texture
    exit_button: Texture

    @classmethod
    def load(cls) -> None:
        # Terrain
        cls.sea: Texture = load_texture(str(cls.path.joinpath("terrain/sea.png")))
        cls.wave: Texture = load_texture(str(cls.path.joinpath("terrain/wave.png")))
        cls.sand: Texture = load_texture(str(cls.path.joinpath("terrain/sand.png")))

        # UI
        cls.title: Texture = load_texture(str(cls.path.joinpath("ui/title.png")))
        cls.start_button: Texture = load_texture(str(cls.path.joinpath("ui/start_button.png")))
        cls.settings_button: Texture = load_texture(str(cls.path.joinpath("ui/settings_button.png")))
        cls.credits_button: Texture = load_texture(str(cls.path.joinpath("ui/credits_button.png")))
        cls.exit_button: Texture = load_texture(str(cls.path.joinpath("ui/exit_button.png")))

    @classmethod
    def unload(cls) -> None:
        # Terrain
        unload_texture(cls.sea)
        unload_texture(cls.wave)
        unload_texture(cls.sand)
        unload_texture(cls.title)
        unload_texture(cls.start_button)
        unload_texture(cls.settings_button)
        unload_texture(cls.credits_button)
        unload_texture(cls.exit_button)
