def is_increasing(seq):

    index = 0
    result = True
    for number in seq:
        if index < len(seq) - 1:
            next_number = seq[index + 1]
            if number > next_number:
                result = False
                break
        index += 1
    return result
print(is_increasing([5,6,-10]))