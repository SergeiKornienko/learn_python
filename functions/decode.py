def decode(string):
    if not string:
        return ''
    result = ''
    list_len = list(map(len, string.split('|')))
    if string[0] != '|':
        result = '{}'.format('0' * list_len[0])
    return '{a}{b}'.format(
        a=result, b=''.join(
            list(
                map(
                    lambda x: ('1{a}'.format(a=(x - 1) * '0')), list_len[1:],
                )
            )
        )
    )
