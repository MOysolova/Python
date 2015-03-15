n = input("Write a number: ")
n = int(n)
list_digits = []
reversed_list = []
while n != 0:
    digit = n % 10
    list_digits += [digit]
    n = n // 10
for index in reversed(list_digits):
    reversed_list += [index]
print(reversed_list)

n_again = 0
for digit in reversed_list:
    n_again = n_again * 10 + digit

print(n_again)