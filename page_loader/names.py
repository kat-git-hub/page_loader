import os
from urllib.parse import urlparse
from pathlib import Path
import re

def rename_filename(source):
    parse = urlparse(source)
    root, ext = os.path.splitext(parse.path)
    rename_netloc = replace_symbols(parse.netloc)
    if parse.path == '':
        return rename_netloc + str('.html')
    if parse.path != '':
        filename_path = replace_symbols(root)
        local_path =  Path(filename_path)
        result =  str(local_path) + ext
        return result

def replace_symbols(path):
    valid_filename_parts = re.findall(r'[^\W]+', path)
    final_filename = '-'.join(valid_filename_parts)
    return final_filename


def get_folder_name(url):
    root, _ = os.path.splitext(rename_filename(url))
    name = root + '_files'
    return name
