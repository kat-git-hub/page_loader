
from page_loader.names import rename_filename, get_folder_name
import requests
import os
from page_loader.resources import update_links
import logging.config
import logging
from page_loader.logging import LOGGING_CONFIG
from pathlib import Path
#from urllib.parse import urlparse

#A good convention to use when naming loggers is to use a module-level logger,
#  in each module which uses logging, named as follows:
#
logging.config.dictConfig(LOGGING_CONFIG)
logger = logging.getLogger('page_loader')

def download(original_url, path=''):
    logger = logging.getLogger('page_loader')
    logger.info(f'Download {original_url}...')
    if not os.path.exists(path):
        os.makedirs(path)
    path_html = os.path.join(path, rename_filename(original_url))
    local_path = os.path.join(path, get_folder_name(original_url))
    _, html = update_links(get_response(original_url).content, original_url, local_path)
    make_save(path_html, html)  
    download_resources(original_url, path)  
    logger.info('Done') 
    return path_html   


def download_resources(original_url, local_dir):
    logger.info(f'Saving to the {local_dir}')
    #try:
    folder = make_folder(original_url,local_dir)
    print(folder)
    
    ######################## косяк с путями куда сохраняются 
    urls, _ = update_links(get_response(original_url).content, original_url, local_dir)
    logger.info(f'download resources')
    for item in urls:
        url = get_response(item['url']).content
        local_path =  os.path.join(folder, str(item['filename']))
        make_save(local_path, url)


def make_save(path_to_file, data):
    with open(path_to_file, 'wb') as f:
        logger.info(f'Save to the {path_to_file}')
        f.write(data)


def get_response(url):
    response = requests.get(url, stream=True)
    response.raise_for_status()
    return response



def make_folder(url, path):
    folder = Path(path) / Path(get_folder_name(url))
    if not os.path.exists(folder):
        os.makedirs(folder)
    return folder