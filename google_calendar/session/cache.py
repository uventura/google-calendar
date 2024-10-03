from pathlib import Path
import sys
import os


def cache_path():
    return Path(sys.argv[0]).parent / "cache"


def save_cache_file(name, content):
    if not cache_path().exists():
        os.makedirs(cache_path(), exist_ok=True)

    with open(cache_path() / name, "w") as cache_file:
        cache_file.write(content)
