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
