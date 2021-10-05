from pathlib import Path

import yaml
from yaml import Loader

from d2rmacro.config.macroconfig import MacroConfig


def load_config(file_path: Path) -> {}:
    return yaml.load(file_path.open(), Loader=Loader)


def parse_config(file_path: Path):
    conf = load_config(file_path)
    hotkeys = conf.get('hotkeys', None)
    if hotkeys:
        return [MacroConfig(**c) for c in hotkeys]
    else:
        raise Exception("Unable to load config file, no 'hotkeys' entry found.")