from bs4 import BeautifulSoup as bs
from page_loader.names import rename_filename, get_folder_name
import requests
from urllib.parse import urlparse, urljoin
import requests
from pathlib import Path


TAGS = {
    'img': 'src',
    'script': 'src',
    'link': 'href'
}


def update_links(html, url, path):
    souped = bs(html, "html.parser")
    urls = []
    #for tag, attr in TAGS.items():
    for tag in souped.find_all(TAGS.keys()):
        attr_val = tag.get(TAGS[tag.name])
        if not attr_val:
            continue
        # make the URL absolute by joining domain with the URL that is just extracted
        link = urljoin(url, attr_val)
        if urlparse(link).netloc != urlparse(url).netloc:
            continue

        new_filename = rename_filename(link)
        urls.append({
             
            'url': link,
            'filename': new_filename,
            
        })
        tag[TAGS[tag.name]] = Path(path) / new_filename
    return urls, souped.prettify("utf-8")

