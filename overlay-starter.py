from pathlib import Path

from d2rmacro.config import parse_config
from d2rmacro.ui.overlay import D2ROverlay
from d2rmacro.util import picture_fetcher

if __name__ == '__main__':
    custom_macro=None
    if not Path("img").exists():
        picture_fetcher.fetch_wiki_images()
    print("Starting overlay...")
    conf = parse_config(Path('macro.yaml'))
    if custom_macro:
        conf = parse_config(Path('macros/macro-trapsin.yaml'))
    overlay = D2ROverlay(conf)
