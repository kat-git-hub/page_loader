from requests.models import Response
from page_loader.names import rename_filename, get_folder_name
import requests
import os
from page_loader.resources import update_links
from pathlib import Path



 #>>> get_get_folder_name('https://en.wikipedia.org')
    #ParseResult(scheme='https', netloc='en.wikipedia.org', path='', params='', query='', #fragment='')
    #['https://en.wikipedia.org/static/images/footer/wikimedia-button.png
    # path = static/images/footer/wikimedia-button.png


def download_page():
    pass


def download(original_url, path):
    filename = rename_filename(original_url)
    name_dir = get_folder_name(original_url)
    local_path = os.path.abspath(path)
    print(local_path)
    path_html = os.path.join(local_path, filename)
    path_resources = os.path.join(local_path, name_dir)
    if not os.path.exists(path_resources):
        os.makedirs(path_resources)
    r = requests.get(original_url, stream=True)
    if r.status_code == 200:
        with open(path_html, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024 * 8):
                if chunk:
                    f.write(chunk)
                    f.flush()
                    os.fsync(f.fileno())
        #return os.path.abspath(file_path), r
    #else:
    #    print("Download failed: status code {}\n{}"
    #          .format(r.status_code, r.text))
    #if not os.path.exists(path_resources):
    #    Path(path_resources).mkdir
    download_resources(original_url, path_resources, name_dir)



def download_resources(original_url, path, local_dir):
    #local_dir = get_folder_name(original_url)
    #if not os.path.exists(local_dir):
    #    os.makedirs(local_dir)
    response = requests.get(original_url, stream=True)
    urls, pretty_html = update_links(response.content, original_url, local_dir)
    #print(urls)
    for item in urls:
        path_to_file = str(Path(path) / item['filename'])
        with open(path_to_file, 'wb') as f:
            f.write(pretty_html)

