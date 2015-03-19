n = input("Write N: ")
n = int(n)

# 1 + 1 = 2
# Вече имаме 1, 1, 2
# Следващото число е последните 2 >> 1 + 2 = 3
# Имаме 1, 1, 2, 3 след това ще е 5
# 1. Трябва да вземем последното число>> дължината на списъка - 1
def last(items):
    return items[len(items) - 1]

# 2. Трябва ни и предпоследното число >> дължината на списъка - 2
def before_last(items):
    return items[len(items) - 2]

# 3. първите елементи ги знаем
def fib(n):
    if n == 1:
        return [1] # Ако въведеното число е 1 се спасяваме така
    if n == 2:
        return [1, 1] # Ако въведеното число е 2 се спасяваме така
    result = [1, 1]
    while len(result) < n:
        next_fib = last(result) + before_last(result) #Тук използваме първите 2 функции
        result = result + [next_fib] # Тук добавяме следващите елементи в горния резултат
    return result


# Функцията взима едно цяло число и връща броя на неговите цифри
def count_digits(n):
    result = 0
    while n != 0:
        result += 1
        n = n // 10
    return result

# Функцията взима списък от цели числа, които може и да са с повече от 1 цифра
# Например [1, 12, 18, 5]
# И връща число, което представлява всички цифри събрани заедно: 112185
def to_number(numbers):
    result = 0
    for number in numbers:
        # Умножаваме по 10^на степен = броя на цифрите на числото, с което ще съберем
        # Така си освобождаваме толова на брой места (0ли)
        multiplier = 10 ** count_digits(number)
        result = result * multiplier + number 
    return result


def fib_number(n):
    return to_number(fib(n))
print(fib_number(n))