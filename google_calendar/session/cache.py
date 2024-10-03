from pathlib import Path
import sys
import os


def cache_path():
    return Path(sys.argv[0])


def save_cache_file(name, content):
    with open(cache_path() / name, "w") as cache_file:
        cache_file.write(content)
