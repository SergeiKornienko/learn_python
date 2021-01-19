# Реализуйте функцию find_files_by_name, которая принимает
# на вход файловое дерево и подстроку, а возвращает список
# файлов, имена которых содержат эту подстроку. Функция
# должна вернуть полные пути файлам.
#
# Пример
# >>> from hexlet.fs import mkdir, mkfile
# >>> from solution import find_files_by_name
# >>> tree = mkdir('/', [
# ...     mkdir('etc', [
# ...         mkdir('apache'),
# ...         mkdir('nginx', [
# ...             mkfile('nginx.conf', {'size': 800}),
# ...         ]),
# ...         mkdir('consul', [
# ...             mkfile('config.json'),
# ...             mkfile('data'),
# ...             mkfile('raft'),
# ...         ]),
# ...     ]),
# ...     mkfile('hosts', {'size': 3500}),
# ...     mkfile('resolve', {'size': 1000}),
# ... ])
# >>> find_files_by_name(tree, 'co')
# ['/etc/nginx/nginx.conf', '/etc/consul/config.json']
# >>>
import os

from hexlet.fs import flatten, get_children, get_name, is_file, mkdir, mkfile


# BEGIN (write your solution here)
def find_files_by_name(tree, string):

    def inner(node, path):
        name_node = get_name(node)
        children = get_children(node)
        if is_file(node) and string in name_node:
            return path
        if is_file(node) or len(children) == 0:
            return []
        output = list(map(
            lambda child: inner(child, os.path.join(path, get_name(child))),
            children,
        ))
        return flatten(output)
    return inner(tree, get_name(tree))
# END


if __name__ == '__main__':
    tree = mkdir('/', [
        mkdir('etc', [
            mkdir('apache'),
            mkdir('nginx', [
                mkfile('nginx.conf', {'size': 800}),
            ]),
            mkdir('consul', [
                mkfile('config.json'),
                mkfile('data'),
                mkfile('raft'),
            ]),
        ]),
        mkfile('hosts', {'size': 3500}),
        mkfile('resolve', {'size': 1000}),
    ])

    assert find_files_by_name(tree, 'toohard') == []
    assert find_files_by_name(tree, 'co') == [
        '/etc/nginx/nginx.conf',
        '/etc/consul/config.json',
    ]
    assert find_files_by_name(tree, 'data') == ['/etc/consul/data']
