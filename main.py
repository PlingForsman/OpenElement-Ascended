from pynput.keyboard import Key, Listener
import os


def on_key_press(key: Key) -> None:

    if key == Key.f1:
        pass

    elif key == Key.f3:
        pass

    elif key == key.f5:
        pass


if __name__ == "__main__":
    listener = Listener(on_press=on_key_press)
    listener.start()

    os.system("cls")
    print() # Keybind options
