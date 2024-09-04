# interfaces/web_browser.py
from abc import ABC, abstractmethod

class WebBrowser(ABC):
    @abstractmethod
    def search(self, query: str) -> str:
        pass