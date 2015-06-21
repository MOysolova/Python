def find_least(cinema):
    least = cinema[0]
    for n in cinema:
        if 0 in n:
            if least.count(0) == 0 or least.count(0) > n.count(0):
                least = n
    return least

def find_start_index(cinema):
    least = find_least(cinema)
    least_row = cinema.index(least)
    next_index = least.index(0)
    return least_row, next_index

def order_of_seats(cinema):
    expected = []
    for n in cinema:
        while 0 in n:
            index_list = find_start_index(cinema)
            expected.append(tuple([index_list[0] + 1, index_list[1] + 1]))
            cinema[index_list[0]][index_list[1]] = 1

    return expected



cinema = [ [1, 1, 1],
           [1, 0, 0],
           [1, 0, 0],
           [1, 1, 0] ]


print(order_of_seats(cinema))
