# Реализуйте функцию convert, которая принимает на вход
# список определённой структуры и возвращает словарь,
# полученный из этого списка.
#
# Список устроен таким образом, что с помощью него
# можно представлять словари. Каждый элемент списка —
# тоже список из двух элементов, где первый элемент —
# ключ, а второй — значение. Значение тоже может быть
# списком. Любой список внутри исходного списка всегда
# рассматривается как данные, которые нужно конвертировать
#
# в словарь.
#
# Примеры
# >>> from solution import convert
# >>> convert([])
# {}
# >>> convert([('key2', 'value2'), ('key', 'value')])
# {'key2': 'value2', 'key': 'value'}
# >>> convert([
# ...   ('key', [('key2', 'anotherValue')]),
# ...   ('key2', 'value2')
# ... ])
# {'key': {'key2': 'anotherValue'}, 'key2': 'value2'}
# >>>
# BEGIN (write your solution here)
def convert(items):
    result = {}
    for item in items:
        if isinstance(item[1], list):
            result[item[0]] = convert(item[1])
        else:
            result[item[0]] = item[1]
    return result
# END


if __name__ == '__main__':
    assert convert([]) == {}
    assert convert([['key', 'value']]) == {'key': 'value'}
    assert convert(
        [
            ['key2', 'value2'],
            ['key3', 'value3'],
        ]) == {'key2': 'value2', 'key3': 'value3'}
    tree = [
        ['key4', 'value4'],
        ['anotherKey', [
            ['key7', False],
            ['innerKey', []],
        ],
         ],
        ['key6', None],
        ['anotherKey2', [
            ['wow', [['one', 'two'], ['three', 'four']]],
            ['key5', True],
        ],
         ],
    ]
    expected = {
        'key4': 'value4',
        'anotherKey': {'key7': False, 'innerKey': {}},
        'key6': None,
        'anotherKey2': {'wow': {'one': 'two', 'three': 'four'}, 'key5': True},
    }
    assert convert(tree) == expected