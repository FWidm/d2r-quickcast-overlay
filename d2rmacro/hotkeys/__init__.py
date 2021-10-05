from pynput import keyboard

f_keys = [
    keyboard.Key.f1,
    keyboard.Key.f2,
    keyboard.Key.f3,
    keyboard.Key.f4,
    keyboard.Key.f5,
    keyboard.Key.f6,
    keyboard.Key.f7,
    keyboard.Key.f8,
    keyboard.Key.f9,
    keyboard.Key.f10,
    keyboard.Key.f11,
    keyboard.Key.f12
]


def translate_f_key(key):
    return {
        'f1': f_keys[0],
        'f2': f_keys[1],
        'f3': f_keys[2],
        'f4': f_keys[3],
        'f5': f_keys[4],
        'f6': f_keys[5],
        'f7': f_keys[6],
        'f8': f_keys[7],
        'f9': f_keys[8],
        'f10': f_keys[9],
        'f11': f_keys[10],
        'f12': f_keys[11],
    }.get(key, None)
