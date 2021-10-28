from page_loader.main import download, download_images
from page_loader.cli import parse_args


def main():
    args = parse_args()
    url, output = args.url, args.output
    print(download(url, output))
    print(download_images(url))
    #imgs = update_links(args.url)
    #for img in imgs:
    #    return download(img, args.path)

if __name__ == '__main__':
    main()
