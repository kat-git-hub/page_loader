import pytest
import os
import requests_mock
from tempfile import TemporaryDirectory
#import requests
from bs4 import BeautifulSoup
from page_loader.main import download
#from pathlib import Path

URL = 'https://ru.hexlet.io/courses'
MOCKED_SITE = open('tests/fixtures/html_before.html').read()

MOCKED_LINKS = ["https://ru.hexlet.io/courses/assets/application.css",
                "https://ru.hexlet.io/courses/assets/professions/nodejs.png",
                "https://ru.hexlet.io/packs/js/runtime.js"]
EXPECTED_SITE = open('tests/fixtures/html_after.html').read()

path = 'tests/fixtures/'

def test_download():
    with TemporaryDirectory() as temp_folder:
        with requests_mock.Mocker() as m:
            m.get(URL, text=MOCKED_SITE)
            filename = download(URL, temp_folder)
            result_path = os.path.join(temp_folder, filename)
            with open(result_path) as f:
                result = f.read()
    exp = BeautifulSoup(EXPECTED_SITE, "html.parser")
            #with open
        #with open(file) as fil:
    assert result == exp.prettify()

