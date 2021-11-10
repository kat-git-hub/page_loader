from page_loader.names import rename_filename, get_folder_name
import requests
import os
from page_loader.resources import update_links
#from pathlib import Path
#from urllib.parse import urlparse


def download(original_url, path):
    filename = rename_filename(original_url)
    print(filename)
    name_dir = get_folder_name(original_url)
    local_path = os.path.abspath(path)
    path_html = os.path.join(local_path, filename)
    path_resources = os.path.join(local_path, name_dir)
    
    if not os.path.exists(path_resources):
        os.makedirs(path_resources)
    response = requests.get(original_url, stream=True)
    urls, pretty_html = update_links(response.content, original_url, name_dir)
    if response.status_code == 200:
        with open(path_html, 'wb') as f:
            f.write(pretty_html)
        return filename
    download_resources(original_url, path_resources, name_dir)



def download_resources(original_url, local_dir):
    #local_dir = get_folder_name(original_url)
    #if not os.path.exists(local_dir):
    response = requests.get(original_url, stream=True)
    urls, pretty_html = update_links(response.content, original_url, local_dir)
    print('######')
    print(urls)
    print('#######')
    #print(pretty_html)
    #rename_urls = rename_filename(urls)
    for item in urls:
        path_to_file = str(item['filename'])
        with open(path_to_file, 'wb') as f:
            f.write(pretty_html)


