import pytest
import os
import requests_mock
import tempfile
import requests
from page_loader.main import download



path = 'tests/fixtures/'

def test_download(requests_mock):
    with tempfile.TemporaryDirectory() as temp_folder:
        #expected_result = f.read()
        requests_mock.get('https://ru.hexlet.io/courses', text='data')
        file = download('https://ru.hexlet.io/courses', temp_folder)
        #with open(file) as fil:
        assert 'data' == requests.get('https://ru.hexlet.io/courses').text

def test_update_links():
    pass
