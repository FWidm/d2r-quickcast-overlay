import functools
from ctypes import windll, create_unicode_buffer
from random import random
from time import sleep
from typing import Optional

from pynput import keyboard, mouse

from d2rmacro.config import MacroConfig
from d2rmacro.hotkeys import translate_f_key, f_keys


class CoreHotkeyListener:
    kb_controller = keyboard.Controller()
    mouse_controller = mouse.Controller()

    def __init__(self, hotkeys: [MacroConfig]):
        self.listener = keyboard.Listener(
            # on_press=self.on_press,
            on_release=self.on_release)
        self.listener.start()
        self.macros = self.__translate_macros(hotkeys)

    def use_skill(self, key, fn):
        if len(key) > 1:
            key = translate_f_key(key)
        if key:
            self.__write_key(key)
            self.__click(mouse.Button.right)
        if fn:
            fn(0)

    def getForegroundWindowTitle(self) -> Optional[str]:
        hWnd = windll.user32.GetForegroundWindow()
        length = windll.user32.GetWindowTextLengthW(hWnd)
        buf = create_unicode_buffer(length + 1)
        windll.user32.GetWindowTextW(hWnd, buf, length + 1)

        if buf.value:
            return buf.value
        else:
            return None

    def __write_key(self, key: str):
        self.kb_controller.press(key)
        sleep(random() / 50)
        self.kb_controller.release(key)

    def __click(self, button: mouse.Button):
        self.mouse_controller.press(button)
        sleep(random() / 50)
        self.mouse_controller.release(button)

    def check_macros(self, key: keyboard.Key):
        func = self.macros.get(key.char, None)
        if func:
            func()

    def on_release(self, key):
        if key not in f_keys and isinstance(key, keyboard.KeyCode):

            window_title = self.getForegroundWindowTitle()
            d2r = "Diablo II: Resurrected"
            if window_title == d2r:
                self.check_macros(key)

    def __translate_macros(self, hotkeys):
        macros = {}
        for hotkey in hotkeys:
            macros[hotkey.hotkey] = functools.partial(self.use_skill, hotkey.used_skill, hotkey.flash_fn)
        return macros
