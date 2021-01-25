def filter_map(func, items):
    result = []
    for item in items:
        predicate, mean = func(item)
        if predicate:
            result.append(mean)
    return result
