from random import randint
n = input("Write a number: ")
n = int(n)

count = 0
score = 0
while count < 3:
    roll = randint(1, n)
    score = score + roll
    count += 1
    print(roll)
print("Sum is: {}" .format(score))
