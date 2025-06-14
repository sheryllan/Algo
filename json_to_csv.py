
def json_to_csv(json_data):
    def get_key_value(obj, prefix):
        if not isinstance(obj, dict):
            yield prefix, obj
        else:
            for k, v in obj.items():
                new_prefix = f'{prefix}_{k}' if prefix else k
                yield from get_key_value(v, new_prefix)

    keys = set()
    results = []
    for i, js in enumerate(json_data):
        line = {}
        for k, v in get_key_value(js, ''):
            keys.add(k)
            line[k] = str(v)
        results.append(line)

    print(','.join(keys))
    for line in results:
        print(','.join(line.get(k, '') for k in keys))




# json_to_csv([
# {"key1": 1, "key2": 2, "key3": 3, "key4": 4},
# {"key1": 5, "key2": 6, "key3": 7, "key5": 8}
# ])



# json_to_csv({"key1": 1, "key2": 2, "key3": 3, "key4": 4})
json_to_csv([
    {"key1": 1, "key2": {"key3": 3, "key4": {"key5": 5, "key_6": 6}}},
{"key1": 1, "key2": {"key7": 3, "key4": {"key5": 5, "key_6": 6}}},
])
