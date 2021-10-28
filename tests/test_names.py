from page_loader import names

@pytest.mark.parametrize('url, expected_filename', [
    ('https://wikipedia.org', 'wikipedia-org.html'),
    ('https://meduza.io', 'meduza-io.html'),
    ('https://slack.com', 'slack-com.html')
])

def test_rename_filename(url, expected_filename):
    assert names.rename_filename == expected_filename


@pytest.mark.parametrize('url, expected_filename', [
    ('https://wikipedia.org', 'wikipedia-org_files'),
    ('https://meduza.io', 'meduza-io_files'),
    ('https://slack.com', 'slack-com_files')
])

def test_get_folder_name(url, expected_name):
    assert names.get_folder_name == expected_name

@pytest.mark.parametrize('url, expected_name', [
    ('https://wikipedia.org', 'wikipedia-org'),
    ('https://meduza.io', 'meduza-io'),
    ('https://slack.com', 'slack-com')
])

def test_replace_symbols(url, expected_name):
    assert names.replace_symbols == expected_name