import dataclasses
from typing import Callable


@dataclasses.dataclass
class MacroConfig:
    name: str
    hotkey: str
    used_skill: str
    icon_path: str
    flash_fn: Callable=None
