__winc_id__ = 'ae539110d03e49ea8738fd413ac44ba8'
__human_name__ = 'files'

import glob
import os
import zipfile


def clean_cache():
    directory = "cache"
    if os.path.exists(directory):
        files = glob.glob(f'{directory}/*')
        for file in files:
            os.remove(file)
    else:
        os.mkdir('cache')


def cache_zip(zip_file_path, cache_dir_path):
    clean_cache()
    zipfile.ZipFile(zip_file_path).extractall(cache_dir_path)


def cached_files():
    return glob.glob('cache/*')


def find_password(file_paths):
    for file_path in file_paths:
        text = open(file_path).read()
        for line in text.split("\n"):
            if "password" in line:
                return line.split(" ")[-1]


if __name__ == '__main__':
    zip_file_path = "data.zip"
    cache_dir_path = "cache"
    cache_zip(zip_file_path, cache_dir_path)
    print(find_password(cached_files()))
