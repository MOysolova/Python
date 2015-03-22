numbers = [1, 2, -2, 0, 0, 5, -5]
def count_zero_neighbours(numbers):

    result = 0
    index = 0

    for number in numbers:
        if index < len(numbers) - 1:
            next_number = numbers[index + 1]
            if number + next_number == 0:
                result += 1
        index += 1
    return result
print(count_zero_neighbours(numbers))
