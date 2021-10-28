from page_loader.names import rename_filename, get_folder_name
import requests
import os
from bs4 import BeautifulSoup as bs
from pathlib import Path
from urllib.parse import urlparse, urljoin



 #>>> get_get_folder_name('https://en.wikipedia.org')
    #ParseResult(scheme='https', netloc='en.wikipedia.org', path='', params='', query='', #fragment='')
    #['https://en.wikipedia.org/static/images/footer/wikimedia-button.png
    # path = static/images/footer/wikimedia-button.png
TAGS = {
    'img': 'src',
    'script': 'src',
    'link': 'href'
}

def download_page():
    pass


def download(url, path):
    filename = rename_filename(url)  #  en-wiki-org.html
    file_path = os.path.join(path, filename) # g/en-wiki-org.html
    if not os.path.exists(path): # create g/
        os.makedirs(path)
    r = requests.get(url, stream=True)
    if r.status_code == 200:
        with open(file_path, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024 * 8):
                if chunk:
                    f.write(chunk)
                    f.flush()
                    os.fsync(f.fileno())
        return os.path.abspath(file_path), r
    else:
        print("Download failed: status code {}\n{}"
              .format(r.status_code, r.text))


def update_links(url, path):
    souped = bs(requests.get(url).content, "html.parser")
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


def download_images(url):
    images = update_links(url)
    
    image_dir = get_folder_name(url)
    for image in images:
        download(image, image_dir)

