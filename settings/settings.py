import json

# GameUserSettings.ini has the following that needs to be grabbed
"LookLeftRightSensitivity, LookUpDownSensitivity, FOVMultiplier, LastJoinedSessionPerCategory, bDisableMenuTransitions, bReverseTribeLogOrder, HideItemTextOverlay=True"

# Input.ini has all the keybinds appearantly default binds also has to be setup incase the file is empty.....
""


def load_keybinds() -> dict[str, int]:
    pass


    return convert_keys()

def load_tower_settings() -> dict:

    try:
        with open("settings/settings.json", "r") as f:
            return json.load(f)
        
    except json.JSONDecodeError:
        print("WARNING: Tower settings are corrupted")

    except FileNotFoundError:
        print("WARNING: Tower settings file does not exist")

def convert_keys(key_dict: dict[str, str]) -> dict[str, int]:

    for key in key_dict:
        key_dict[key] = KeyCodes.dict[str(key_dict[key])]
    
    return key_dict


default_keys: dict[str, str] = {
    "console": "tab",
    "crouch": "c",
    "drop": "o",
    "inventory": "i",
    "prone": "x",
    "target_inventory": "f",
    "toggle_hud": "backspace",
    "hud_info": "h",
    "use": "e",
    "logs": "l",
    "transfer": "t",
    "hotbar_0": "0",
    "hotbar_1": "1",
    "hotbar_2": "2",
    "hotbar_3": "3",
    "hotbar_4": "4",
    "hotbar_5": "5",
    "hotbar_6": "6",
    "hotbar_7": "7",
    "hotbar_8": "8",
    "hotbar_9": "9",
}

class WindowMessage:
    LBUTTONDOWN = 0x0201 # Left click down
    LBUTTONUP = 0x0202   # Left click up

    RBUTTONDOWN = 0x0204 # Right click down
    RBUTTONUP = 0x0205   # Right click up

    KEYDOWN = 0x0100     # Key down
    KEYUP = 0x0101       # Key up

class KeyCodes: 
    MK_LBUTTON = 0x0001     # Left click
    MK_RBUTTON = 0x0002     # Right click

    VK_MBUTTON = 0x04   # Middle mouse button
    VK_XBUTTON1 = 0x05 	# X1 mouse button
    VK_XBUTTON2 = 0x06 	# X2 mouse button
    VK_BACK = 0x08 	    # BACKSPACE key
    VK_TAB = 0x09 	    # TAB key
    VK_RETURN =	0x0D 	# ENTER key
    VK_SHIFT =	0x10 	# SHIFT key
    VK_CONTROL = 0x11 	# CTRL key
    VK_MENU =	0x12 	# ALT key
    VK_PAUSE =	0x13 	# PAUSE key
    VK_CAPITAL = 0x14 	# CAPS LOCK key
    VK_ESCAPE =	0x1B 	# ESC key
    VK_SPACE = 0x20 	# SPACEBAR
    VK_PRIOR = 0x21 	# PAGE UP key
    VK_NEXT = 0x22 	    # PAGE DOWN key
    VK_END = 0x23 	    # END key
    VK_HOME = 0x24 	    # HOME key
    VK_LEFT = 0x25 	    # LEFT ARROW key
    VK_UP =	0x26 	    # UP ARROW key
    VK_RIGHT = 0x27 	# RIGHT ARROW key
    VK_DOWN = 0x28 	    # DOWN ARROW key
    VK_SELECT =	0x29 	# SELECT key
    VK_SNAPSHOT = 0x2C 	# PRINT SCREEN key
    VK_INSERT =	0x2D 	# INS key
    VK_DELETE =	0x2E 	# DEL key
    VK_HELP = 0x2F 	    # HELP key
    VK_0 = 0x30 	    # 0 key
    VK_1 = 0x31 	    # 1 key
    VK_2 = 0x32 	    # 2 key
    VK_3 = 0x33 	    # 3 key
    VK_4 = 0x34 	    # 4 key
    VK_5 = 0x35 	    # 5 key
    VK_6 = 0x36 	    # 6 key
    VK_7 = 0x37 	    # 7 key
    VK_8 = 0x38 	    # 8 key
    VK_9 = 0x39 	    # 9 key
    VK_A = 0x41 	    # A key
    VK_B = 0x42 	    # B key
    VK_C = 0x43 	    # C key
    VK_D = 0x44 	    # D key
    VK_E = 0x45 	    # E key
    VK_F = 0x46 	    # F key
    VK_G = 0x47 	    # G key
    VK_H = 0x48 	    # H key
    VK_I = 0x49 	    # I key
    VK_J = 0x4A 	    # J key
    VK_K = 0x4B 	    # K key
    VK_L = 0x4C 	    # L key
    VK_M = 0x4D 	    # M key
    VK_N = 0x4E 	    # N key
    VK_O = 0x4F 	    # O key
    VK_P = 0x50 	    # P key
    VK_Q = 0x51 	    # Q key
    VK_R = 0x52 	    # R key
    VK_S = 0x53 	    # S key
    VK_T = 0x54 	    # T key
    VK_U = 0x55 	    # U key
    VK_V = 0x56 	    # V key
    VK_W = 0x57 	    # W key
    VK_X = 0x58 	    # X key
    VK_Y = 0x59 	    # Y key
    VK_Z = 0x5A 	    # Z key
    VK_LWIN = 0x5B 	    # Left Windows key
    VK_RWIN = 0x5C 	    # Right Windows key
    VK_APPS = 0x5D 	    # Applications key
    VK_NUMPAD0 = 0x60 	# Numeric keypad 0 key
    VK_NUMPAD1 = 0x61 	# Numeric keypad 1 key
    VK_NUMPAD2 = 0x62 	# Numeric keypad 2 key
    VK_NUMPAD3 = 0x63 	# Numeric keypad 3 key
    VK_NUMPAD4 = 0x64 	# Numeric keypad 4 key
    VK_NUMPAD5 = 0x65 	# Numeric keypad 5 key
    VK_NUMPAD6 = 0x66 	# Numeric keypad 6 key
    VK_NUMPAD7 = 0x67 	# Numeric keypad 7 key
    VK_NUMPAD8 = 0x68 	# Numeric keypad 8 key
    VK_NUMPAD9 = 0x69 	# Numeric keypad 9 key
    VK_MULTIPLY = 0x6A 	# Multiply key
    VK_SUBTRACT = 0x6D 	# Subtract key
    VK_DECIMAL = 0x6E 	# Decimal key
    VK_DIVIDE =	0x6F 	# Divide key
    VK_F1 =	0x70 	    # F1 key
    VK_F2 =	0x71 	    # F2 key
    VK_F3 =	0x72 	    # F3 key
    VK_F4 =	0x73 	    # F4 key
    VK_F5 =	0x74 	    # F5 key
    VK_F6 =	0x75 	    # F6 key
    VK_F7 =	0x76 	    # F7 key
    VK_F8 =	0x77 	    # F8 key
    VK_F9 =	0x78 	    # F9 key
    VK_F10 = 0x79 	    # F10 key
    VK_F11 = 0x7A 	    # F11 key
    VK_F12 = 0x7B 	    # F12 key
    VK_F13 = 0x7C 	    # F13 key
    VK_F14 = 0x7D 	    # F14 key
    VK_F15 = 0x7E 	    # F15 key
    VK_F16 = 0x7F 	    # F16 key
    VK_F17 = 0x80 	    # F17 key
    VK_F18 = 0x81 	    # F18 key
    VK_F19 = 0x82 	    # F19 key
    VK_F20 = 0x83 	    # F20 key
    VK_F21 = 0x84 	    # F21 key
    VK_F22 = 0x85 	    # F22 key
    VK_F23 = 0x86 	    # F23 key
    VK_F24 = 0x87 	    # F24 key
    VK_NUMLOCK = 0x90   # NUM LOCK key
    VK_SCROLL =	0x91 	# SCROLL LOCK key
    VK_LSHIFT =	0xA0 	# Left SHIFT key
    VK_RSHIFT =	0xA1 	# Right SHIFT key
    VK_LCONTROL = 0xA2 	# Left CONTROL key
    VK_RCONTROL = 0xA3 	# Right CONTROL key
    VK_LALT = 0xA4 	    # Left ALT key
    VK_RALT = 0xA5 	    # Right ALT key
    VK_SECTION = 0xA7 	# Section key
    
    dict = {
        "mmb": VK_MBUTTON,
        "xmb1": VK_XBUTTON1,
        "xmb2": VK_XBUTTON2,
        "backspace": VK_BACK,
        "tab": VK_TAB,
        "enter": VK_RETURN,
        "shift": VK_SHIFT,
        "ctrl": VK_CONTROL,
        "alt": VK_MENU,
        "pause": VK_PAUSE,
        "caps": VK_CAPITAL,
        "esc": VK_ESCAPE,
        "space": VK_SPACE,
        " ": VK_SPACE,
        "pgup": VK_PRIOR,
        "pgdown": VK_NEXT,
        "end": VK_END,
        "home": VK_HOME,
        "left": VK_LEFT,
        "up": VK_UP,
        "right": VK_RIGHT,
        "down": VK_DOWN,
        "select": VK_SELECT,
        "prntscr": VK_SNAPSHOT,
        "insert": VK_INSERT,
        "delete": VK_DELETE,
        "help": VK_HELP,
        "0": VK_0,
        "1": VK_1,
        "2": VK_2,
        "3": VK_3,
        "4": VK_4,
        "5": VK_5,
        "6": VK_6,
        "7": VK_7,
        "8": VK_8,
        "9": VK_9,
        "a": VK_A,
        "b": VK_B,
        "c": VK_C,
        "d": VK_D,
        "e": VK_E,
        "f": VK_F,
        "g": VK_G,
        "h": VK_H,
        "i": VK_I,
        "j": VK_J,
        "k": VK_K,
        "l": VK_L,
        "m": VK_M,
        "n": VK_N,
        "o": VK_O,
        "p": VK_P,
        "q": VK_Q,
        "r": VK_R,
        "s": VK_S,
        "t": VK_T,
        "u": VK_U,
        "v": VK_V,
        "w": VK_W,
        "x": VK_X,
        "y": VK_Y,
        "z": VK_Z,
        "lwin": VK_LWIN,
        "rwin": VK_RWIN,
        "application": VK_APPS,
        "numpad0": VK_NUMPAD0,
        "numpad1": VK_NUMPAD1,
        "numpad2": VK_NUMPAD2,
        "numpad3": VK_NUMPAD3,
        "numpad4": VK_NUMPAD4,
        "numpad5": VK_NUMPAD5,
        "numpad6": VK_NUMPAD6,
        "numpad7": VK_NUMPAD7,
        "numpad8": VK_NUMPAD8,
        "numpad9": VK_NUMPAD9,
        "multiply": VK_MULTIPLY,
        "subtract": VK_SUBTRACT,
        "decimal": VK_DECIMAL,
        "divide": VK_DIVIDE,
        "f1": VK_F1,
        "f2": VK_F2,
        "f3": VK_F3,
        "f4": VK_F4,
        "f5": VK_F5,
        "f6": VK_F6,
        "f7": VK_F7,
        "f8": VK_F8,
        "f9": VK_F9,
        "f10": VK_F10,
        "f11": VK_F11,
        "f12": VK_F12,
        "f13": VK_F13,
        "f14": VK_F14,
        "f15": VK_F15,
        "f16": VK_F16,
        "f17": VK_F17,
        "f18": VK_F18,
        "f19": VK_F19,
        "f20": VK_F20,
        "f21": VK_F21,
        "f22": VK_F22,
        "f23": VK_F23,
        "f24": VK_F24,
        "numlock": VK_NUMLOCK,
        "scrlock": VK_SCROLL,
        "lshift": VK_LSHIFT,
        "rshift": VK_RSHIFT,
        "lctrl": VK_LCONTROL,
        "rctrl": VK_RCONTROL,
        "lalt": VK_LALT,
        "ralt": VK_RALT,
        "section" : VK_SECTION,
    }