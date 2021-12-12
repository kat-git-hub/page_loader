import pytest
import requests_mock
import os
from page_loader.names import rename_filename
from tempfile import TemporaryDirectory
from requests.exceptions import HTTPError
from page_loader.downloader import download, download_resources


URL = 'https://ru.hexlet.io/courses'
MOCKED_SITE = open('tests/fixtures/html_before.html').read
EXPECTED_LINKS = ["ru-hexlet-io-courses_files/ru-hexlet-io-courses.html",
                "ru-hexlet-io-courses_files/ru-hexlet-io-assets-professions-nodejs.png",
                "ru-hexlet-io-courses_files/ru-hexlet-io-packs-js-runtime.js"]


def test_download():
    with TemporaryDirectory() as tmp_dir:
        with requests_mock.Mocker() as m:
            m.get(URL, text ='123')
            file_path = download(URL, tmp_dir)
            with open(file_path) as f:
                assert '123\n' == f.read()


def test_403_error():
    with TemporaryDirectory() as tmp_dir:
        with pytest.raises(HTTPError) as excinfo:
            url = 'https://en.wikipediaa.com/'
            download(url, tmp_dir)
        assert '403 Client Error: Forbidden for url' in str(excinfo.value)


def test_404_error():
    with TemporaryDirectory() as tmp_dir:
        with pytest.raises(HTTPError) as excinfo:
            url = 'https://www.google.com/error'
            download(url, tmp_dir)
        assert '404 Client Error: Not Found for url' in str(excinfo.value)


def test_access_error(requests_mock):
    requests_mock.get('URL')
    wrong_path = '/non-existent_path'
    with pytest.raises(OSError):
        assert download('URL', wrong_path)

def test_load_files():
    with TemporaryDirectory() as temp:
        link_for_test = '/assets/professions/nodejs.png'
        path = os.path.join(temp, rename_filename(link_for_test))
        download([(link_for_test, path)])
        assert os.path.isfile(path)