n = input("Enter N: ")
n = int(n)
def square(n):
    return n ** 2
print("Square " + str(square(n)))

def factorial(n):
    result = 1
    start = 1
    while start <= n:
        result *= start
        start += 1
    return result
print("Factorial " + str(factorial(n)))

items = [1, 2, 3, 4, 5, 6]
def count_elements(items):
    result = 0
    for item in items:
        result += 1
    return result
print("Elements " + str(count_elements(items)))

def member(n, items):
    found = False
    for part in items:
        if n == part:
            found = True
            break
    return found
print("Is N in list? " + str(member(n, items)))

students = ["Rado", "Ivo", "Maria", "Nina"]
grades = [3, 4.5, 5.5, 6]
limit = 4.5
def grades_that_pass(students, grades, limit):
    result = []
    index = 0
    for grade in grades:
        student = students[index]
        if grade >= limit:
            result += [student]
        index += 1
    return result
print(grades_that_pass(students, grades, limit))