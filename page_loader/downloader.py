from page_loader.names import rename_filename, get_folder_name
import requests
import os
from page_loader.resources import update_links
import sys
import logging.config
import logging
from page_loader.logging import LOGGING_CONFIG
from pathlib import Path

#A good convention to use when naming loggers is to use a module-level logger,
#  in each module which uses logging, named as follows:
#
logging.config.dictConfig(LOGGING_CONFIG)
logger = logging.getLogger('page_loader')

def download(original_url, path):
    logger = logging.getLogger('page_loader')
    logger.info(f'Download {original_url}...')

    filename = rename_filename(original_url)
    #name_dir = get_folder_name(original_url)
    #local_path = os.path.join(path, name_dir)
    path_html = os.path.join(path, filename)
    _, html = update_links(get_response(original_url).content, original_url, path_html)
    #print(path_html)

    #path_resources = os.path.join(local_path, name_dir)
    #if not os.path.exists(path_resources):
    #    os.makedirs(path_resources)
    #######################
    #   переписать в хтмл линки на локальные
    #################
   # make_save()
        #response = requests.get(original_url, stream=True)

    #    raise ConnectionError('Connection error') from e
    #    sys.exit(1)  ## 1?

    
    make_save(path_html, html)  
    download_resources(original_url, path)   
    return path_html   #logger.info('fff')




def download_resources(original_url, local_dir):
    logger.info(f'Saving to the {local_dir}')
    #try:
    folder = make_folder(original_url,local_dir)
    #print(folder)
    
    ######################## косяк с путями куда сохраняются 
    urls, _ = update_links(get_response(original_url).content, original_url, local_dir)
    logger.info(f'download resources')
    for item in urls:
        url = get_response(item['url']).content
        local_path =  os.path.join(folder, str(item['filename']))
        make_save(local_path, url)

    ##########################python3

    #print(pretty_html)
    #for item in urls:
        #path_to_file = str(item['filename'])
        #with open(path_to_file, 'wb') as f:
         #   for chunk in response.iter_content(chunk_size=1280):
         #       f.write(local_html)
                #logger.debug('Saving to the {local_dir}')

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