import requests
import shutil
import ctypes
import time
import os
import argparse

def get_input():
    parser = argparse.ArgumentParser(description="You have to use either -WAIFU or -BLOWJOB or -NEKO or -TRAP")
    parser.add_argument("-WAIFU", action="store_true", help="WAIFU ")
    parser.add_argument("-BLOWJOB", action="store_true", help="BLOWJOB")
    parser.add_argument("-NEKO", action="store_true", help="NEKO")
    parser.add_argument("-TRAP", action="store_true", help="TRAP")
    args = parser.parse_args()

    if not any(vars(args).values()):
        url = "https://api.waifu.pics/nsfw/waifu"
    else:
        url = "https://api.waifu.pics/nsfw/"
        if args.WAIFU:
            url += "waifu"
        if args.BLOWJOB:
            url += "blowjob"
        if args.NEKO:
            url += "neko"
        if args.TRAP:
            url += "trap"
    return url


def get_data(url):
    print(url)
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    pic_url = data.get('url')
    return pic_url


def download_file(url, filename):
    response = requests.get(url, stream=True)
    response.raise_for_status()
    with open(filename, 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
    return filename

def set_background(filename):
    SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, filename, 0)

url = get_input()
url_string = get_data(url)
filename = "pic.jpg"
path = os.path.join(os.path.dirname(os.path.abspath(__file__)), filename)
download_file(url_string, path)
print(path)
time.sleep(1)
set_background(path)