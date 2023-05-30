def get_val(collection, key, default='git'):
    for k in collection.keys():
        if k == key:
            return collection[key]
    if not collection:
        return default
    else:
        return default
