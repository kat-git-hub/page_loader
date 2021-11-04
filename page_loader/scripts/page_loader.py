from page_loader.main import download, download_resources
from page_loader.cli import parse_args
from page_loader.resources import update_links
import requests


def main():
    args = parse_args()
    url, output = args.url, args.output
    print(download(url, output))
    #print(output)
    #print(download_resources(url, output))
    #resources = update_links(requests.get(url, stream=True).content, url, output)
    #for img in resources:
    #    return download_resources(img, output)

if __name__ == '__main__':
    main()
