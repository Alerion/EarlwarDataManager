import os


def get_root(path: str):
    split = path.split(os.sep)
    return split[1] if split[0] == '' else split[0]


def get_relative_path(path: str):
    return '/' + path.replace(os.sep, '/')
