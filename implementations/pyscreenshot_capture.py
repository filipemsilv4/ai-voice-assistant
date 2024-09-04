# implementations/pyscreenshot_capture.py
import pyscreenshot as ps
from interfaces.screen_capture import ScreenCapture

class PyscreenshotCapture(ScreenCapture):
    def capture(self) -> str:
        screenshot: ps.Image = ps.grab()
        screenshot_path: str = "screenshot.png"
        screenshot.save(screenshot_path)
        return screenshot_path