square1 = [ [23, 28, 21], [22, 24, 26], [27, 20, 25] ]
square = [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ]

def sum_second_diag(square):
    result = 0
    row_index = 0
    col_index = len(square[0]) - 1

    for row in square:
        result += square[row_index][col_index]
        row_index += 1
        col_index -= 1
    return result


def sum_main_diag(square):
    result = 0
    index = 0

    for row in square:
        result += square[index][index]
        index += 1
    return result


def sum_row(square, index):
    result = 0
    index = 0
    for index in range(0, len(square)):
        result += index
    return sum(square[index])


def sum_col(square, index):
    result = 0
    for row in square:
        result += row[index]
    return result

def magic_square(square):
    target_sum = sum_main_diag(square)

    if sum_second_diag(square) != target_sum:
        return False
# Тук се появява index, който използваме в горните функции
    for index in range(0, len(square)):
        if sum_row(square, index) != target_sum:
            return False

    for index in range(0, len(square[0])):
        if sum_col(square, index) != target_sum:
            return False

    return True
print(magic_square(square))