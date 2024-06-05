import requests
import shutil
import ctypes
import time
import os

def get_data():
    response = requests.get("https://api.waifu.pics/nsfw/waifu")
    response.raise_for_status()
    data = response.json()
    url = data.get('url')
    return url

def download_file(url, filename):
    response = requests.get(url, stream=True)
    response.raise_for_status()
    with open(filename, 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
    return filename

def set_background(filename):
    SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, filename, 0)

url_string = get_data()
filename = "waifu.jpg"
path = os.path.join(os.getcwd(), filename)
download_file(url_string, filename)
time.sleep(1)
set_background(path)
