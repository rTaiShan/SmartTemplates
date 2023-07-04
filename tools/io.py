from time import sleep
import os
import tempfile
import webbrowser

CHROME_PATH = r'C:\Program Files\Google\Chrome\Application\chrome.exe'

def read_from_file(path):
    '''
    Reads the file in the path, using utf-8 encoding and returns the content.
    '''
    with open(path, "r", encoding="utf-8") as f:
        return f.read()
    

def preview_html(html : str, browser_path=CHROME_PATH):
    '''
    Previews html from string using browser.
    If no custom browser_path is specified, uses default chrome path
    '''
    html_dirpath = os.path.dirname("")
    try:
        with tempfile.NamedTemporaryFile(dir=html_dirpath, suffix=".html", mode='w', delete=False, encoding="utf-8") as temp_file:
            temp_file.write(html)
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(browser_path))
            webbrowser.get("chrome").open(temp_file_name := temp_file.name)
    finally:
        sleep(0.5) # Wait until chrome finishes reading
        os.remove(temp_file_name)
