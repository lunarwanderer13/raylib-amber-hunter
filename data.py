import json
from pathlib import Path
from platformdirs import user_config_dir, user_data_dir
from dataclasses import asdict
from typing import Any

from config import DefaultConfig, DefaultData

class ConfigManager:
    path: Path = Path(user_config_dir("AmberHunter"))
    path.mkdir(parents=True, exist_ok=True)
    path = path / "config.json"

    @classmethod
    def load(cls) -> dict[str, Any]:
        if not cls.path.exists():
            cls.save()

        with open(Path(cls.path), "r") as file:
            return json.load(file)

    @classmethod
    def save(cls, data: dict[str, Any] | None = None) -> None:
        if not data:
            data = asdict(DefaultConfig())

        with open(cls.path, "w") as file:
            json.dump(data, file, indent=4)

class DataManager:
    path: Path = Path(user_data_dir("AmberHunter"))
    path.mkdir(parents=True, exist_ok=True)
    path = path / "data.json"

    @classmethod
    def load(cls) -> dict[str, Any]:
        if not cls.path.exists():
            cls.save()

        with open(Path(cls.path), "r") as file:
            return json.load(file)

    @classmethod
    def save(cls, data: dict[str, Any] | None = None) -> None:
        if not data:
            data = asdict(DefaultData())

        with open(cls.path, "w") as file:
            json.dump(data, file, indent=4)
