import pytest
import os
import requests_mock
from tempfile import TemporaryDirectory
#import requests
from requests.exceptions import HTTPError
from bs4 import BeautifulSoup
from page_loader.downloader import download
from pathlib import Path

URL = 'https://ru.hexlet.io/courses'
MOCKED_SITE = open('tests/fixtures/html_before.html').read()

MOCKED_LINKS = ["https://ru.hexlet.io/courses/assets/application.css",
                "https://ru.hexlet.io/courses/assets/professions/nodejs.png",
                "https://ru.hexlet.io/packs/js/runtime.js"]
EXPECTED_SITE = open('tests/fixtures/html_after.html').read()

path = 'tests/fixtures/'

# удалить мусор /var/folders/8g/

#def test_download():
#    with TemporaryDirectory() as tmp_dir:
#        with requests_mock.Mocker() as m:
#            m.get(URL, text=MOCKED_SITE)
#            for link in MOCKED_LINKS:
#                m.get(link, text='ссылки для скачивания ')
#            filename = download(URL, tmp_dir)
#            #result_path = os.path.join(tmp_dir, filename)
#        with open(filename) as f:         
#            exp = BeautifulSoup(EXPECTED_SITE, "html.parser")
#            assert f.read() == exp.prettify('utf-8')

def test_download():
    with TemporaryDirectory() as tmp_dir:
        with requests_mock.Mocker() as m:
            m.get(URL, text ='123')
            file_path = download(URL, tmp_dir)
            with open(file_path) as f:
                assert '123\n' == f.read()


def test_valid_url():
    pass

def test_network_error():
    with TemporaryDirectory() as tmp_dir:
        with pytest.raises(HTTPError) as excinfo:
            url = 'https://www.google.com/error'
            download(url, tmp_dir)
        assert '404 Client Error' in str(excinfo.value)