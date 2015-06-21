n = input("Enter a number: ")
n = int(n)
# Взимаме цифрите на числото
def digits(n):
    result = []
    while n != 0:
        digit = n % 10
        n = n // 10
        result += [digit] #result.append(digit)
    return result
print(digits(n))
# Намираме факториела произжедения на числата от 1 до n
def factoriel(n):
    start = 1
    total = 1
    while start <= n:
        total *= start
        start += 1
    return total
print(factoriel(n))

# За всеки дигит трябва да намерим факториел и после да го съберем
def sum_factoriel(n):
    result = 0
    n = digits(n)
    for number in n:
        number = factoriel(number) # в скобките трябва да е това, от което искаме да намерим функцията
        result += number
    return result
print(sum_factoriel(n))