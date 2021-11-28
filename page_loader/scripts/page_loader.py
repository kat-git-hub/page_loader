from page_loader.downloader import download
from page_loader.cli import parse_args
from page_loader.logging import LOGGING_CONFIG
import logging.config
#import sys

logging.config.dictConfig(LOGGING_CONFIG)


def main():
    logger = logging.getLogger('page_loader')
    args = parse_args()
    url, output = args.url, args.output
    download(url, output)
    logger.info('Done.')

if __name__ == '__main__':
    main()
