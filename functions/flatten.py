def flatten(items):
    new_list = []
    for item in items:
        if isinstance(item, list):
            new_list.extend(flatten(item))
        else:
            new_list.append(item)
    return new_list

