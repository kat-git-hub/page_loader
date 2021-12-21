import pytest
import requests_mock
import os
from tempfile import TemporaryDirectory
from requests.exceptions import HTTPError
from page_loader.downloader import download, AppInternalError as Error


URL = 'https://en.wikipedia.org/wiki/Python_(programming_language)'


def test_download():
    with TemporaryDirectory() as tmp_dir:
        with requests_mock.Mocker() as m:
            m.get(URL, text ='123')
            file_path = download(URL, tmp_dir)
            with open(file_path) as f:
                assert '123\n' == f.read()


def test_403_error():
    with TemporaryDirectory() as tmp_dir:
        with pytest.raises(Error) as excinfo:
            url = 'https://en.wikipediaa.com/'
            download(url, tmp_dir)
        assert '403 Client Error: Forbidden for url' in str(excinfo.value)


def test_404_error():
    with TemporaryDirectory() as tmp_dir:
        with pytest.raises(Error) as excinfo:
            url = 'https://www.google.com/error'
            download(url, tmp_dir)
        assert '404 Client Error: Not Found for url' in str(excinfo.value)


def test_access_error(requests_mock):
    requests_mock.get('URL')
    wrong_path = '/non-existent_path'
    with pytest.raises(Error):
        assert download('URL', wrong_path)


def test_is_exist_file():
    url = 'https://wikipedia.com'
    with TemporaryDirectory() as tmp_dir:
        folder_with_files = download(url, tmp_dir)
        assert os.path.exists(folder_with_files)
        assert os.path.isfile(folder_with_files)
