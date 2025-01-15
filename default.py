import xbmc
import xbmcgui
import xbmcaddon
from resources.lib.web_browser import WebBrowser

class OnlineBrowser(xbmcaddon.Addon):
    def __init__(self):
        self.addon_id = xbmcaddon.Addon().getAddonInfo('id')
        self.addon_name = xbmcaddon.Addon().getAddonInfo('name')
        self.addon_version = xbmcaddon.Addon().getAddonInfo('version')

    def run(self):
        dialog = xbmcgui.Dialog()
        url = dialog.input('Enter URL', type=xbmcgui.INPUT_ALPHANUM)
        if url:
            web_browser = WebBrowser()
            web_browser.browse(url)

if __name__ == '__main__':
    addon = OnlineBrowser()
    addon.run()
