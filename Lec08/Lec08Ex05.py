def flatten(L):
    result = []
    for x in L:
        if type(x) == list:
            result.extend(flatten(x))
        else:
            result.append(x)
    return result


def flatten2(L):
    result = []
    for elem in L:
        result.append(elem)
    return result


def flatten3(L):
    result = []
    stack = L[::-1]
    while stack:
        item = stack.pop()
        if isinstance(item, list):
            stack.extend(item[::-1])
        else:
            result.append(item)
    return result


if __name__ == "__main__":
    v = [[1, 5], 6, [[2]], [3, [7, 8, [9, 10], [11, 12]]]]
    print(v)
    print(flatten3(v))
