import pytest
import requests_mock
import os
from tempfile import TemporaryDirectory
from page_loader.downloader import download
from page_loader.exceptions import Error


URL = 'https://ru.hexlet.io/courses'
link = {'css': 'ru-hexlet-io-assets-application.css',
        'png': 'ru-hexlet-io-assets-professions-nodejs.png',
        'js': 'ru-hexlet-io-packs-js-runtime.js'}


@pytest.fixture
def get_open_file():
    with open('tests/fixtures/html_before.html') as f:
        file_before = f.read()
    with open('tests/fixtures/html_after.html') as af:
        file_after = af.read()
    with open('tests/fixtures/runtime.js') as js:
        read_js = js.read()
    with open('tests/fixtures/application.css') as css:
        read_css = css.read()
    return (file_before, read_js, read_css, file_after)


@pytest.fixture
def get_read_png():
    with open('tests/fixtures/nodejs.png', 'rb') as f:
        read_png = f.read()
        return read_png


def test_download(get_open_file, get_read_png):
    with TemporaryDirectory() as tmp_dir:
        with requests_mock.Mocker() as m:
            m.get(URL, text=get_open_file[0])
            m.get('https://ru.hexlet.io/packs/js/runtime.js',
                  text=get_open_file[1])
            m.get('https://ru.hexlet.io/assets/application.css',
                  text=get_open_file[2])
            m.get('https://ru.hexlet.io/assets/professions/nodejs.png',
                  content=get_read_png)
            file_path = download(URL, tmp_dir)
            assert os.path.isfile(file_path)
            resources_path = os.path.join(tmp_dir, 'ru-hexlet-io-courses_files')
            with open(file_path, 'r', encoding='utf-8') as f:
                actual_content = f.read().strip()
                expected_content = get_open_file[3].strip()
                assert (
                    actual_content.replace(' ', '').replace('\n', '')
                    == expected_content.replace(' ', '').replace('\n', '')
                )
            with open(os.path.join(resources_path, link['css'])) as f_css:
                assert f_css.read() == get_open_file[2]
            with open(os.path.join(resources_path, link['png']), 'rb') as f_png:
                assert f_png.read() == get_read_png
            with open(os.path.join(resources_path, link['js'])) as f_js:
                assert f_js.read() == get_open_file[1]


def test_403_error():
    with TemporaryDirectory() as tmp_dir:
        with requests_mock.Mocker() as m:
            m.get('https://example.com/forbidden', status_code=403)
            with pytest.raises(Error) as excinfo:
                download('https://example.com/forbidden', tmp_dir)
            assert '403' in str(excinfo.value)


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
