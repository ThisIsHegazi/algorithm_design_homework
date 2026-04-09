start = [9, 10, 11, 12, 13, 15]
end = [11, 11, 12, 14, 15, 16]


def selector(start: list, end: list):
    results = [0]
    i = 1
    j = 0
    for i, v in enumerate(start, 0):
        if v >= end[j]:
            results.append(i)
            j = i
    return results


print(selector(start, end))
