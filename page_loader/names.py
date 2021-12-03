import os
from urllib.parse import urlparse
import re


def rename_filename(input_url):
    parse = urlparse(input_url)
    rename_netloc = replace_symbols(parse.netloc)
    rename_path = replace_symbols(parse.path)
    without_schema = parse.netloc + parse.path
    root, ext = os.path.splitext(without_schema)
    filename = replace_symbols(root)
    if parse.path == '':
        return rename_netloc + rename_path + str('.html')
    if ext == '':
        ext = '.html'
    return filename + ext


def replace_symbols(path):
    valid_filename_parts = re.findall(r'[^\W]+', path)
    final_filename = '-'.join(valid_filename_parts)
    return final_filename


def get_folder_name(url):
    root, _ = os.path.splitext(rename_filename(url))
    name = root + '_files'
    return name
