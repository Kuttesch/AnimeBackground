import requests
import shutil
import ctypes
import time
import os
import argparse

def get_input():
    parser = argparse.ArgumentParser(description="Select one of the SFW or NSFW categories.")
    
    sfw_categories = [
        "WAIFU", "NEKO", "SHINOBU", "MEGUMIN", "BULLY", "CUDDLE", "CRY", "HUG",
        "AWOO", "KISS", "LICK", "PAT", "SMUG", "BONK", "YEET", "BLUSH", "SMILE",
        "WAVE", "HIGHFIVE", "HANDHOLD", "NOM", "BITE", "GLOMP", "SLAP", "KILL",
        "KICK", "HAPPY", "WINK", "POKE", "DANCE", "CRINGE"
    ]

    nsfw_categories = [
        "WAIFU", "BLOJOB", "NEKO", "TRAP"
    ]

    for category in sfw_categories:
        parser.add_argument(f"-SFW_{category}", action="store_true", help=f"{category.lower()} (SFW)")

    for category in nsfw_categories:
        parser.add_argument(f"-NSFW_{category}", action="store_true", help=f"{category.lower()} (NSFW)")

    args = parser.parse_args()

    if not any(vars(args).values()):
        url = "https://api.waifu.pics/nsfw/waifu"
    else:
        url = "https://api.waifu.pics/"
        
        for category in sfw_categories:
            if getattr(args, f"SFW_{category}"):
                url += f"sfw/{category.lower()}"
                break

        for category in nsfw_categories:
            if getattr(args, f"NSFW_{category}"):
                url += f"nsfw/{category.lower()}"
                break

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
