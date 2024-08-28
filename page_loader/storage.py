import logging
import os
from page_loader.logging import LOGGING_CONFIG
from page_loader.exceptions import Error


logging.config.dictConfig(LOGGING_CONFIG)
logger = logging.getLogger('page_loader')


def make_folder(folder):
    if not os.path.exists(folder):
        os.mkdir(folder)
        logger.info(f'Create folder: {folder}')
        return folder
    if not os.access(folder, os.W_OK):
        raise OSError('Access denied.')


def make_save(path_to_file, data):
    try:
        with open(path_to_file, 'wb') as f:
            logger.info(f'Save to the {path_to_file}')
            return f.write(data)
    except OSError as error:
        logger.warning(f'Incorrect folder. Error: {error}')
        raise Error(f'{error}') from error
