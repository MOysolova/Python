numbers = [0, 2, -2, 5, 10]
def count_zero_pairs(numbers):
    result = 0
    n = len(numbers)
    for index in range(0, n):
        for number in range(index, n):
            x = numbers[index]
            y = numbers[number]
            if x + y == 0:
                result += 1

    return result

print(count_zero_pairs(numbers))