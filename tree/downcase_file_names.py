# Реализуйте функцию downcase_file_names, которая принимает
# на вход директорию (объект-дерево), приводит имена всех
# файлов в этой и во всех вложенных директориях к нижнему
# регистру. Результат в виде обработанной директории
# возвращается наружу.
#
# Пример
# >>> from hexlet.fs import mkdir, mkfile, get_children, get_name
# >>> from solution import downcase_file_names
# >>> tree = mkdir('/', [
# ...     mkdir('eTc', [
# ...         mkdir('NgiNx', [], {'size': 4000}),
# ...         mkdir(
# ...             'CONSUL',
# ...             [mkfile('config.JSON', {'uid': 0})],
# ...         ),
# ...     ]),
# ...     mkfile('HOSTS'),
# ... ])
# >>> new_tree = downcase_file_names(tree)
# >>> new_file = get_children(new_tree)[1]
# >>> get_name(new_file)
# hosts
# >>>
import copy

from hexlet.fs import get_children, get_meta, get_name, is_file, mkdir, mkfile


# BEGIN (write your solution here)
def downcase_file_names(tree):
    name = get_name(tree)
    meta = copy.deepcopy(get_meta(tree))
    if is_file(tree):
        return mkfile(name.lower(), meta)
    children = get_children(tree)
    new_children = list(map(downcase_file_names, children))
    return mkdir(name, new_children, meta)
# END


if __name__ == "__main__":
    tree = mkdir('/', [
        mkdir('eTc', [
            mkdir('NgiNx', [], {'size': 4000}),
            mkdir(
                'CONSUL',
                [mkfile('config.JSON', {'uid': 0})],
            ),
        ]),
        mkfile('hOsts'),
    ])
    original = copy.deepcopy(tree)
    downcase_file_names(tree)
    assert tree == original
    tree = mkdir('/', [
        mkdir('eTc', [
            mkdir('NgiNx', [], {'size': 4000}),
            mkdir(
                'CONSUL',
                [mkfile('config.JSON', {'uid': 0})],
            ),
        ]),
        mkfile('hOsts'),
    ])

    expected = {
        'name': '/',
        'meta': {},
        'type': 'directory',
        'children': [
            {
                'name': 'eTc',
                'meta': {},
                'type': 'directory',
                'children': [
                    {
                        'name': 'NgiNx',
                        'meta': {'size': 4000},
                        'type': 'directory',
                        'children': [],
                    },
                    {
                        'name': 'CONSUL',
                        'meta': {},
                        'type': 'directory',
                        'children': [
                            {
                                'name': 'config.json',
                                'type': 'file',
                                'meta': {'uid': 0},
                            },
                        ],
                    },
                ],
            },
            {'name': 'hosts', 'type': 'file', 'meta': {}},
        ],
    }
    assert downcase_file_names(tree) == expected
