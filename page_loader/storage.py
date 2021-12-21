from page_loader.logging import LOGGING_CONFIG
import logging
import os
from pathlib import Path
from page_loader.names import get_folder_name
import sys


logging.config.dictConfig(LOGGING_CONFIG)
logger = logging.getLogger('page_loader')


def make_folder(url, path):
    folder = Path(path) / Path(get_folder_name(url))
    if not os.path.exists(folder):
        os.makedirs(folder)
    return folder


def make_save(path_to_file, data):
    try:
        with open(path_to_file, 'wb') as f:
            logger.info(f'Save to the {path_to_file}')
            return f.write(data)
    except OSError as error:
        logger.warning(f'Incorrect folder. Error:{error}')
        sys.exit()
