def fit(data, targets):
    n = len(data)

    result = []
    i = 0
    last_observation = None
    for t in targets:
        while i < n and data[i][0] <= t:
            last_observation = data[i][1]
            i += 1

        result.append(last_observation)

    return result


assert fit([(1, 10.1), (4, 9.9), (5, 9.8)], [0, 2, 4, 5, 6]) == [None, 10.1, 9.9, 9.8, 9.8]