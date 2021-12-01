import pytest
import os
import requests_mock
from tempfile import TemporaryDirectory
import requests
from requests.exceptions import HTTPError
from bs4 import BeautifulSoup
from page_loader.downloader import download
from pathlib import Path

URL = 'https://ru.hexlet.io/courses'
MOCKED_SITE = open('tests/fixtures/html_before.html').read()


path = 'tests/fixtures/'

# удалить мусор /var/folders/8g/
# правильно ли формируются локальные ссылки
def test_download():
    with TemporaryDirectory() as tmp_dir:
        with requests_mock.Mocker() as m:
            m.get(URL, text ='123')
            file_path = download(URL, tmp_dir)
            with open(file_path) as f:
                assert '123\n' == f.read()


def test_valid_url():
    pass

#def test_404_error():
#    with TemporaryDirectory() as tmp_dir:
#        with pytest.raises(HTTPError) as excinfo:
#            url = 'https://www.google.com/error'
#            download(url, tmp_dir)
#        assert '404 Client Error: Not Found for url' in str(excinfo.value)
        #assert str(excinfo.value) == 'It was an error, my Lord'

#@pytest.mark.xfail(raises=HTTPError)
def test_404_error():
    with TemporaryDirectory() as tmp_dir:
        with pytest.raises(HTTPError) as excinfo:
            url = 'https://www.google.com/error'
            download(url, tmp_dir)
        assert '404 Client Error: Not Found for url' in str(excinfo.value)