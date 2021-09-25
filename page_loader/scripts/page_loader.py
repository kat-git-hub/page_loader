from page_loader.main import download
from page_loader.cli import parse_args


def main():
    args = parse_args()
    print(download(args.url, args.output))


if __name__ == '__main__':
    main()
