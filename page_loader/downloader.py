from page_loader.names import rename_filename, get_folder_name
import requests
import os
from page_loader.resources import update_links
import logging.config
import logging
from page_loader.logging import LOGGING_CONFIG
from progress.bar import FillingSquaresBar
from page_loader.storage import make_folder, make_save
from page_loader.exceptions import Error


logging.config.dictConfig(LOGGING_CONFIG)
logger = logging.getLogger('page_loader')


CHUNK_SIZE = 1024


def download(original_url, path=''):
    #logger.info('Downloading ')
    if not os.path.exists(path):
        raise Error(f'Incorrect folder: {path}') from FileNotFoundError
    path_html = os.path.join(path, rename_filename(original_url))
    local_path = os.path.join(path, get_folder_name(original_url))
    logger.info(f'Downloading  from {original_url} to {path_html}')
    urls, html = update_links(get_response(original_url).text,
                              original_url, local_path)
    make_save(path_html, html)
    download_resources(original_url, path, urls)
    logger.info('Done')
    return path_html


def download_resources(original_url, local_dir, urls):
    logger.info(f'Saving to the {local_dir}')
    root_dir = make_folder(original_url, local_dir)
    logger.info(f'Create directory: {root_dir}')
    logger.info('Download resources...')
    bar = FillingSquaresBar('Loading', max=len(urls))
    for item in urls:
        local_path = os.path.join(root_dir, str(item['filename']))
        with requests.get(item['url'], stream=True) as r:
            r.raise_for_status()
            with open(local_path, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    logger.info(f'Save to the {local_path}')
                    f.write(chunk)
                    bar.next()
    bar.finish()


def get_response(url):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        return response
    except (requests.exceptions.HTTPError,
            requests.exceptions.ConnectionError,
            requests.exceptions.MissingSchema) as error:
        raise Error(f'{error}: {url}') from error
