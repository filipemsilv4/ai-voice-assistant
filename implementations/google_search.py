# implementations/google_search.py
import webbrowser
from interfaces.web_browser import WebBrowser

class GoogleSearch(WebBrowser):
    def search(self, query: str) -> str:
        url: str = f"https://www.google.com/search?q={query}"
        webbrowser.open(url)
        return f"Abrindo a pesquisa no Google para: {query}"