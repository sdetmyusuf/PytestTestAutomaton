from pathlib import Path
from logging import config
import os
import yaml
from dotenv import load_dotenv

class ConfigManager:
    _config = None

    @classmethod
    def load_config(cls, env: str = None):
        if cls._config is None:
            load_dotenv()
            env = env or os.getenv("ENV", "local")

             # Always resolve relative to project root
            project_root = Path(__file__).parent.parent
            config_path = project_root / "config" / "config.yaml"
            try:
                with open(config_path, "r") as f:
                    all_cfg = yaml.safe_load(f) or {}
            except FileNotFoundError:
                raise RuntimeError("Missing config/config.yaml file")

            if env not in all_cfg:
                raise RuntimeError(f"Environment '{env}' not found in config.yaml")

            cls._config = all_cfg.get(env, {})
        return cls._config

    @classmethod
    def get(cls, key: str, default=None):
        if cls._config is None:
            cls.load_config()
        return cls._config.get(key, default)
