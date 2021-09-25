import requests
import os


def formatting_url(source):
    _, url_name= source.split('://')
    local_filename = url_name.replace('.', '-').replace('/', '-') + str('.html')
    return local_filename


def download(url, path):
    filename = formatting_url(url)
    file_path = os.path.join(path, filename)
    #print(path, file_path)
    if not os.path.exists(path):
        os.makedirs(path)
    r = requests.get(url, stream=True)
    if r.ok:
        #print("saving to", os.path.abspath(file_path))
        #k = os.path.abspath(file_path)
        #return os.path.abspath(file_path)
        with open(file_path, 'wb') as f:
            #f.write(r.content)
            for chunk in r.iter_content(chunk_size=1024 * 8):
                if chunk:
                    f.write(chunk)
                    f.flush()
                    os.fsync(f.fileno())
            return os.path.abspath(file_path)
    else:  # HTTP status code 4XX/5XX
        print("Download failed: status code {}\n{}".format(r.status_code, r.text))
