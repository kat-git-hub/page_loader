from page_loader.main import download, download_resources
from page_loader.cli import parse_args
from page_loader.resources import update_links
import requests


def main():
    args = parse_args()
    url, output = args.url, args.output
    print(download(url, output))


if __name__ == '__main__':
    main()
