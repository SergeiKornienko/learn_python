# Реализуйте функцию get_hidden_files_count, которая
# считает количество скрытых файлов в директории и всех
# поддиректориях. Скрытым файлом в Linux системах
# считается файл, название которого начинается с точки.
#
# Пример
# >>> from hexlet.fs import mkdir, mkfile
# >>> from solution import get_hidden_files_count
#
# >>> tree = mkdir('/', [
# ...     mkdir('etc', [
# ...         mkdir('apache'),
# ...         mkdir('nginx', [
# ...             mkfile('.nginx.conf', {'size': 800}),
# ...         ]),
# ...         mkdir('.consul', [
# ...             mkfile('.config.json', {'size': 1200}),
# ...             mkfile('data', {'size': 8200}),
# ...             mkfile('raft', {'size': 80}),
# ...         ]),
# ...      ]),
# ...      mkfile('.hosts', {'size': 3500}),
# ...      mkfile('resolve', {'size': 1000}),
# ... ])
# >>> get_hidden_files_count(tree)
# 3
# >>>
from hexlet.fs import get_name, is_file, get_children, mkdir, mkfile


# BEGIN (write your solution here)
def get_hidden_files_count(node):
    if is_file(node) and get_name(node).startswith('.'):
        return 1
    if is_file(node):
        return 0
    children = get_children(node)
    count_hidden_children = list(map(get_hidden_files_count, children))
    return sum(count_hidden_children)
# END


if __name__ == '__main__':
    tree = mkdir('/', [
        mkdir('etc', [
            mkdir('apache'),
            mkdir('nginx', [
                mkfile('.nginx.conf'),
            ]),
            mkdir('consul', [
                mkfile('.config.json'),
                mkfile('data'),
                mkfile('raft'),
            ]),
        ]),
        mkfile('.hosts', {'size': 3500}),
        mkfile('resolve'),
    ])
    assert get_hidden_files_count(tree) == 3
    tree = mkdir('/', [
        mkdir('.etc', [
            mkdir('.apache'),
            mkdir('nginx', [
                mkfile('nginx.conf'),
            ]),
            mkdir('.consul', [
                mkfile('config.json', {'size': 3500}),
                mkfile('.raft'),
            ]),
        ]),
        mkfile('hosts'),
        mkfile('resolve'),
    ])
    assert get_hidden_files_count(tree) == 1
