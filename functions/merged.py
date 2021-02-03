# BEGIN (write your solution here)
def merged(*dicts):
    result = {}
    for item in dicts:
        for key in item.keys():
            if key not in result.keys():
                result[key] = {item[key]}
            else:
                result[key] = result[key] | {item[key]}
    return result
# END
