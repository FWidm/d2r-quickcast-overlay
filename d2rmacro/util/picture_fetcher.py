from pathlib import Path

import requests as requests
from bs4 import BeautifulSoup


def fetch_wiki_images():
    print(f"No img folder exists, fetching from wiki...")
    chars = ['Amazon', 'Assassin', 'Barbarian', 'Druid', 'Necromancer', 'Paladin', 'Sorceress']

    for char in chars:
        print(f"Saving icons for character {char}")
        url = f"https://diablo-archive.fandom.com/wiki/Category:Diablo_II_{char}_Skill_Icon_Images"

        result = requests.get(url)
        html = result.text
        dom_document = BeautifulSoup(html, 'html.parser')
        imgs = dom_document.find_all("img", {"width": "120"})
        for img in imgs:
            src_url = img['src']
            data_src = img.attrs.get('data-src')
            if data_src:
                src_url = data_src
            file_name = img['alt']
            file_name = '_'.join(file_name.lower().split()).replace('_icon', '')
            img_result = requests.get(src_url)
            file = Path(f"img/{char.lower()}/{file_name}")
            print(f"... saving image {file}")
            file.parent.mkdir(parents=True, exist_ok=True)
            file.open('wb').write(img_result.content)
