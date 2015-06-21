def setify(a):
    result = []
    for number in a:
        if number not in result:
            result += [number]
    return result

def diff(a, b):
    result = []
    for number in a:
        if number not in b:
            result += [number]
    return setify(result)


def union(a, b):
    # result = []
    # for number in a:
    #     if number not in result:
    #         result += [number]
    # for number in b:
    #     if number not in result:
    #         result += [number]
    return setify(a + b)


def intersection(a, b):
    result = []
    for number in a:
        if number in b:
            result += [number]
    return setify(result)


def cartesian_product(a, b):
    # Tuple is (a, b) as a syntax
    result = []
    for number_a in setify(a):
        for number_b in setify(b):
            result += [(number_a, number_b)]
    return result

def main():
    print(setify([0, 1, 1, 5, 5, 6]) == [0, 1, 5, 6])
    print(union([0, 0, 0, 0, 0], [1, 2]) == [0, 1, 2])
    print(intersection([0, 0, 1, 2, 5], [5, 5, 6]) == [5])
    print(diff([0, 1, 2, 3, 4, 5], [0, 0, 1, 1, 2, 2, 3, 3]) == [4, 5])
    print(cartesian_product([0, 1], [1]) == [(0, 1), (1, 1)])


if __name__ == '__main__':
    main()