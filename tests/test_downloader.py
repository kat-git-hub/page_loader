import pytest
import requests_mock
from tempfile import TemporaryDirectory
from requests.exceptions import HTTPError
from page_loader.downloader import download


URL = 'https://ru.hexlet.io/courses'
MOCKED_SITE = open('tests/fixtures/html_before.html').read()


path = 'tests/fixtures/'

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
