def stringify(data, replacer=' ', spaces_count=1):

    def inner(items, replacer_in=replacer, count=spaces_count):
        if not isinstance(items, dict):
            return str(items)
        list_values = []
        for key in items.keys():
            list_values.append(''.join([
                replacer_in * count,
                str(key),
                ': ',
                str(inner(
                    items[key],
                    replacer_in=replacer,
                    count=count + spaces_count,
                )),
            ]))
        return '\n'.join([
            '{',
            *list_values,
            '{a}{b}'.format(a=(replacer_in * (count - spaces_count)), b='}'),
        ])
    return inner(data, replacer_in=replacer, count=spaces_count)
