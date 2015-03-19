n = input("Enter a number: ")
n = int(n)
start = 0
words = []
while start <= n:
    word = input("Write a word: ")
    words += [word]
    start += 1
for word in words:
    if word 
def take(n, items):
    result = []
    for index in range(0, min(n, len(items))):
        result += [items[index]]
    return result
def string_matrix(matrix_width, strings):