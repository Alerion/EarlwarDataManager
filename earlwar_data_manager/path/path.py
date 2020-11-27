import re


def get_path(path: str, name: str):
    return f'{path}/{name}'


def get_root(path: str):
    split = path.split('/')
    return split[1] if split[0] == '' else split[0]


def get_folder(file: str):
    m = re.match('^(.+)/([^/]+)$', file)
    return f'/{m.group(1)}'
