from random import randint
start = input("Start number: ")
start = int(start)
end = input("End number: ")
end = int(end)
n = input("Enter number of numbers: ")
n = int(n)
def generate_random_list(n, start, end):
    result_list = []
    count = 1
    while count <= n:
        if start < end:
            result_list += [randint(start, end)]
            count += 1
        elif start > end:
            result_list += [randint(end, start)]
            count += 1
    return result_list
print(generate_random_list(n, start, end))