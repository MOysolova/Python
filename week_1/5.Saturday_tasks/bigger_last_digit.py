n = input("Enter N: ")
n = int(n)
m = input("Enter M: ")
m = int(m)
def last_digit(n, m):
    last_digit1 = n % 10
    last_digit2 = m % 10
    if last_digit1 > last_digit2:
        return n
    elif last_digit1 < last_digit2:
        return m
    elif n == m:
        return "Tie"
    else:
        if n > m:
            return n
        else:
            return m
print(last_digit(n, m))