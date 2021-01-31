def transposed(matrix):
    return list(map(list, zip(*matrix)))


def snail_path(matrix):
    result = []
    while len(matrix) > 0:  # noqa: WPS507
        result.extend(matrix.pop(0))
        matrix = transposed(list(map(reversed, matrix)))
        print(matrix)
    return result
