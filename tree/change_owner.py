# example
import copy
from pprint import pprint
from hexlet import fs

tree = fs.mkdir('/', [
    fs.mkdir('etc', [
        fs.mkfile('bashrc'),
        fs.mkfile('consul.cfg'),
    ]),
    fs.mkfile('hexletrc'),
    fs.mkdir('bin', [
        fs.mkfile('ls'),
        fs.mkfile('cat'),
    ]),
])


def change_owner(node, owner):
    name = fs.get_name(node)
    new_meta = copy.deepcopy(fs.get_meta(node))
    new_meta['owner'] = owner
    if fs.is_file(node):
        # Возвращаем обновлённый файл
        return fs.mkfile(name, new_meta)
    children = fs.get_children(node)
    # Ключевая строчка
    # Вызываем рекурсивное обновление каждого ребёнка
    new_children = list(
        map(lambda child: change_owner(child, owner), children))
    new_tree = fs.mkdir(name, new_children, new_meta)
    # Возвращаем обновлённую директорию
    return new_tree


tree2 = change_owner(tree, 'nobody')
pprint(tree2)
