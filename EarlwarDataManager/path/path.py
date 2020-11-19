def get_path(path: str, name: str):
    return f'{path}/{name}'


def get_edit_path(path: str):
    return f'/edit/{path}/form'


def get_root(path: str):
    split = path.split('/')
    return split[1] if split[0] == '' else split[0]
