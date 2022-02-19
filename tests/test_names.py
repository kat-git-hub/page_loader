from page_loader import names
import pytest

@pytest.mark.parametrize('url, expected_filename', [
    ('https://wikipedia.org', 'wikipedia-org.html'),
    ('https://github.com', 'github-com.html'),
    ('https://slack.com', 'slack-com.html')
])


def test_rename_filename(url, expected_filename):
    assert names.rename_filename(url) == expected_filename


@pytest.mark.parametrize('url, expected_filename', [
    ('https://wikipedia.org', 'wikipedia-org_files'),
    ('https://github.com', 'github-com_files'),
    ('https://slack.com', 'slack-com_files')
])


def test_get_folder_name(url, expected_filename):
    assert names.get_folder_name(url) == expected_filename


@pytest.mark.parametrize('url, expected_name', [
    ('wikipedia.org', 'wikipedia-org'),
    ('github.com', 'github-com'),
    ('slack.com', 'slack-com')
])

def test_replace_symbols(url, expected_name):
    assert names.replace_symbols(url) == expected_name