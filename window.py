import ctypes, win32gui, win32ui
from pathlib import Path
import cv2 as cv
import numpy as np
import time

from typing import Literal
from tools import threaded

from settings.settings import KeyCodes, WindowMessage


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
    
    def screenshot(self) -> cv.Mat:

        # I dont recommend touching this shit

        hwnd_dc = win32gui.GetWindowDC(self.hwnd)
        mfc_dc = win32ui.CreateDCFromHandle(hwnd_dc)
        save_dc = mfc_dc.CreateCompatibleDC()
        
        save_bit_map = win32ui.CreateBitmap()
        save_bit_map.CreateCompatibleBitmap(mfc_dc, self.resolution[0], self.resolution[1])
        save_dc.SelectObject(save_bit_map)
        
        result = ctypes.windll.user32.PrintWindow(self.hwnd, save_dc.GetSafeHdc(), 2)
        
        bmp_info = save_bit_map.GetInfo()
        bmp_data = save_bit_map.GetBitmapBits(True)
        
        win32gui.DeleteObject(save_bit_map.GetHandle())
        save_dc.DeleteDC()
        mfc_dc.DeleteDC()
        win32gui.ReleaseDC(self.hwnd, hwnd_dc)
        
        if result == 1:
            screenshot = np.frombuffer(bmp_data, dtype=np.uint8)
            screenshot = screenshot.reshape((bmp_info['bmHeight'], bmp_info['bmWidth'], 4))
            return cv.cvtColor(screenshot, cv.COLOR_BGRA2BGR)

    def locate_template(self, template: str, confidence: float) -> tuple[int, int]:
        
        template: cv.Mat = cv.imread(f"{self.template_path}/{template}", cv.IMREAD_GRAYSCALE)
        image: cv.Mat = cv.cvtColor(self.screenshot(), cv.COLOR_BGR2GRAY)

        result: cv.Mat = cv.matchTemplate(image, template, cv.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

        if max_val > confidence:
            return (
                    max_loc[0] + (template.shape[1] // 2),
                    max_loc[1] + (template.shape[0] // 2)
                )

    def await_template(self, template: str, confidence: float, timeout: int) -> bool:
        
        start = time.time()

        while True:

            if self.locate_template(template, confidence):
                return True
            
            if time.time() - start >= timeout:
                return False
            
    def match_pixel(self, xy: tuple[int, int], rgb: tuple[int, int, int], variance: int) -> bool:

        img: cv.Mat = cv.cvtColor(self.screenshot(), cv.COLOR_BGR2RGB)
        pixel_rgb: np.ndarray = img[xy[1], xy[0]]
                
        return all(abs(pixel_rgb[i] - rgb[i]) <= variance for i in range(3))

    def press(self, key: int, duration: float = 0) -> None:

        ctypes.windll.user32.PostMessageA(self.hwnd, WindowMessage.KEYDOWN, key, 0) # Button down
        time.sleep(duration)
        ctypes.windll.user32.PostMessageA(self.hwnd, WindowMessage.KEYUP, key, 0) # Button up

    @threaded
    def hold(self, key: int, duration: float) -> None:

        self.press(key, duration)

    def click(self, button: Literal["left", "right"] = "left", xy: tuple[int, int] = None, clicks: int = 1, interval: int = 0) -> None:

        for i in range(clicks):
            ctypes.windll.user32.PostMessageA( # Button down
                self.hwnd, 
                WindowMessage.LBUTTONDOWN if button == "left" else WindowMessage.RBUTTONDOWN, 
                KeyCodes.MK_LBUTTON if button == "left" else KeyCodes.MK_RBUTTON, 
                xy[1] << 16 | xy[0] if xy else 0
            )
            ctypes.windll.user32.PostMessageA( # Button up
                self.hwnd, 
                WindowMessage.LBUTTONUP if button == "left" else WindowMessage.RBUTTONUP, 
                KeyCodes.MK_LBUTTON if button == "left" else KeyCodes.MK_RBUTTON,  
                xy[1] << 16 | xy[0] if xy else 0
            )
            time.sleep(interval)
        
if __name__ == "__main__": 
    window = ProcessWindow()
    print(window.__repr__())