from operator import mul


def transposed(matrix):
    return list(map(list, zip(*matrix)))


def multiply(matrix1, matrix2):
    result = []
    for line in matrix1:
        elem = []
        for row in transposed(matrix2):
            elem.append(sum(map(mul, line, row)))
        result.append(elem)
    return result
