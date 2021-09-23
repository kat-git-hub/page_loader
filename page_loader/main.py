import requests
import os


def formatting_url(source):
    _, url_name= source.split('://')
    local_filename = url_name.replace('.', '-').replace('/', '-') + str('.html')
    return local_filename


def download(url, dest_dir = ' '):
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir) # create folder if it does not exist
    
    filename = formatting_url(url)
    file_path = os.path.join(os.getcwd() + dest_dir, filename)
    

    r = requests.get(url, stream=True)
    if r.ok:
        print("saving to", os.path.abspath(file_path))
        with open(file_path, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024 * 8):
                if chunk:
                    f.write(chunk)
                    f.flush()
                    os.fsync(f.fileno())
    else:  # HTTP status code 4XX/5XX
        print("Download failed: status code {}\n{}".format(r.status_code, r.text))
