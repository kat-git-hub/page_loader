import argparse
import os


def parse_args():
    parser = argparse.ArgumentParser(prog='page-loader',
                                     description='Page Loader')
    parser.add_argument('-o', '--output',
                        default=os.getcwd(),
                        help='set path to download folder. '
                        'Downloading to current directory by default')
    parser.add_argument('<url>', help='specify URL')
    args = parser.parse_args()
    return args
