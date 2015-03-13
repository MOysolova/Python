from random import randint
n = input("Enter sides: ")
n = int(n)

def random_dice(n):
    result = randint(1, n)
    return result
print (random_dice(n))
