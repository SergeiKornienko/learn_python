# BEGIN (write your solution here)
from operator import add


def triangle(count_line):
    row = [1]
    lines = range(0, count_line)
    for _ in lines:
        row = list(map(
            add,
            row + [0],
            [0] + row,
        ))
    return row
# END
