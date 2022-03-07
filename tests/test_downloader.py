import pytest
import requests_mock
import os
from tempfile import TemporaryDirectory
from page_loader.downloader import download
from page_loader.exceptions import Error


URL = 'https://ru.hexlet.io/courses'
file_before = open('tests/fixtures/html_before.html').read()
file_after = open('tests/fixtures/html_after.html').read()
read_css = open('tests/fixtures/application.css').read()
read_png = open('tests/fixtures/nodejs.png', 'rb').read()
read_js = open('tests/fixtures/runtime.js').read()


def test_download():
    with TemporaryDirectory() as tmp_dir:
        with requests_mock.Mocker() as m:
            m.get(URL, text=file_before)
            m.get('https://ru.hexlet.io/packs/js/runtime.js', text=read_js)
            m.get('https://ru.hexlet.io/assets/application.css', text=read_css)
            m.get('https://ru.hexlet.io/assets/professions/nodejs.png', content=read_png)
            file_path = download(URL, tmp_dir)
            assert os.path.isfile(file_path)
            resources_path = os.path.join(tmp_dir, 'ru-hexlet-io-courses_files')
            with open(file_path) as f:
                assert f.read() == file_after
            with open(os.path.join(resources_path, 'ru-hexlet-io-assets-application.css')) as f_css:
                assert f_css.read() == read_css
            d = os.path.join(resources_path, 'ru-hexlet-io-assets-professions-nodejs.png')
            with open(d, 'rb') as f_png:
                assert f_png.read() == read_png
            with open(os.path.join(resources_path, 'ru-hexlet-io-packs-js-runtime.js')) as f_js:
                assert f_js.read() == read_js


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
    requests_mock.get(URL)
    wrong_path = '/usr/local/lib'
    with pytest.raises(Error):
        assert download(URL, wrong_path)


def test_is_exist_file():
    url = 'https://wikipedia.com'
    with TemporaryDirectory() as tmp_dir:
        folder_with_files = download(url, tmp_dir)
        assert os.path.exists(folder_with_files)
        assert os.path.isfile(folder_with_files)
