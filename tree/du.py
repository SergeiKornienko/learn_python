# Реализуйте функцию du, которая принимает на вход директорию,
# а возвращает список узлов, вложенных (директорий и файлов)
# в указанную директорию на один уровень, и место, которое
# они занимают. Размер файла задается в метаданных. Размер
# директории складывается из сумм всех размеров файлов,
# находящихся внутри во всех подпапках. Сами папки размера не имеют.
#
# Пример
# >>> from hexlet.fs import mkdir, mkfile
# >>> from solution import du
# >>> tree = mkdir('/', [
# ...     mkdir('etc', [
# ...         mkdir('apache'),
# ...         mkdir('nginx', [
# ...             mkfile('nginx.conf', {'size': 800}),
# ...         ]),
# ...         mkdir('consul', [
# ...             mkfile('.config.json', {'size': 1200}),
# ...             mkfile('data', {'size': 8200}),
# ...             mkfile('raft', {'size': 80}),
# ...         ]),
# ...     ]),
# ...     mkfile('hosts', {'size': 3500}),
# ...     mkfile('resolve', {'size': 1000}),
# ... ])
# >>> du(tree)
# [('etc', 10280), ('hosts', 3500), ('resolve', 1000)]
# >>>
# Примечания
# Обратите внимание на структуру результирующего cписка.Каждый
# элемент — кортеж с двумя значениями: именем директории
# и размером файлов внутри.
# Результат отсортирован по размеру в обратном порядке.
# То есть сверху самые тяжёлые, внизу самые лёгкие.
from hexlet.fs import get_children, get_meta, get_name, is_file, mkdir, mkfile


# BEGIN (write your solution here)
def get_size_node(node):
    if is_file(node):
        return get_meta(node)['size']
    children = get_children(node)
    size_children = list(map(get_size_node, children))
    return sum(size_children)


def du(tree):
    children = get_children(tree)
    result = list(map(
        lambda child: (get_name(child), get_size_node(child)),
        children,
    ))
    result.sort(key=lambda size: size[1], reverse=True)
    return result
# END


if __name__ == '__main__':
    tree = mkdir('/', [
        mkdir('etc', [
            mkdir('apache'),
            mkdir('nginx', [
                mkfile('nginx.conf', {'size': 800}),
            ]),
            mkdir('consul', [
                mkfile('.config.json', {'size': 1200}),
                mkfile('data', {'size': 8200}),
                mkfile('raft', {'size': 80}),
            ]),
        ]),
        mkfile('hosts', {'size': 3500}),
        mkfile('resolve', {'size': 1000}),
    ])
    assert du(tree) == [('etc', 10280), ('hosts', 3500), ('resolve', 1000)]
    expected = [('consul', 9480), ('nginx', 800), ('apache', 0)]
    assert du(get_children(tree)[0]) == expected
