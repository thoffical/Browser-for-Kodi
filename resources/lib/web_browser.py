import requests
from bs4 import BeautifulSoup
import xbmcgui

class WebBrowser:
    def __init__(self):
        self.dialog = xbmcgui.Dialog()

    def browse(self, url):
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            title = soup.title.text if soup.title else 'No title'
            self.dialog.ok(title, soup.prettify())
        except Exception as e:
            self.dialog.ok('Error', str(e))
