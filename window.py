import ctypes, win32gui
from pathlib import Path


class ProcessWindow:

    def __init__(self) -> None:
        ctypes.windll.user32.SetProcessDPIAware()

        self.hwnd = self.find_window("UnrealWindow", "ArkAscended")
        self.resolution = self.get_resolution()
        self.template_path = f"{Path(__file__).parent}/templates"
        self.ocr_path = r"C:/Program Files/Tesseract-OCR/tesseract.exe"

    def __repr__(self) -> str:
        return (
            f"HWND: {self.hwnd}",
            f"Resolution: {self.resolution[0]}x{self.resolution[1]}",
            f"Template Path: {self.template_path}",
            f"OCR Path: {self.ocr_path}"
        )
    
    def find_window(self, PyResourceId: str | None, window_title: str) -> int:

        hwnd = win32gui.FindWindow(PyResourceId, window_title)

        if hwnd == 0:
            raise ValueError(f"Window: '{window_title}' was not found.")
        
        else: 
            return hwnd

    def get_resolution(self) -> tuple[int, int]:

        left, top, right, bot = win32gui.GetWindowRect(self.hwnd)

        return (right - left, bot - top)
    
    def set_window_foreground(self) -> None:

        win32gui.SetForegroundWindow(self.hwnd)

    def has_crashed(self) -> bool:

        crash_str: list[str] = ["The UE-ShooterGame Game has crashed and will close", "Crash!"]

        for crash in crash_str:
            try:
                if self.find_window(None, crash): # Crash has been detected
                    return True 

            except:
                pass # Crash window not found

        return False # No crash window was found 


if __name__ == "__main__": 
    screen = ProcessWindow()
    print(screen.__repr__())