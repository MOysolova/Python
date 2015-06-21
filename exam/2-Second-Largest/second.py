def sorted_list(numbers):
    result = sorted(numbers)
    return result

def remove_unwanted(numbers):
    result = []
    for number in numbers:
        if number not in result:
            result += [number]
    return result


def second_largest(numbers):
    sorted_l = sorted_list(numbers)
    actual_list = remove_unwanted(sorted_l)
    if len(actual_list) <= 1:
        return False
    if len(actual_list) > 1:
        answer = actual_list[-2]
        return answer

