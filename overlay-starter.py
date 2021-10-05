import logging
import sys
from pathlib import Path

from d2rmacro.config import parse_config
from d2rmacro.ui.overlay import D2ROverlay
from d2rmacro.util import picture_fetcher
from d2rmacro.util.logging import log


if __name__ == '__main__':
    log.debug(sys.argv)
    custom_macro=None
    if len(sys.argv) > 1:
        custom_macro = sys.argv[1]
    if not Path("img").exists():
        picture_fetcher.fetch_wiki_images()
    log.info("Starting overlay...")
    conf = parse_config(Path('macro.yaml'))
    if custom_macro:
        logging.info(f"loading custom macro from dragging... {custom_macro}")
        conf = parse_config(Path(custom_macro))
    overlay = D2ROverlay(conf)
