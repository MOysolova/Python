word = input("Enter a word: ")
n = input("Enter number: ")
n = int(n)
count = 1
word_list = []
word_count = 0
while count <= n:
    a = input("Enter another word: ")
    word_list += [a]
    count += 1
for string in word_list:
    if word == string:
        word_count += 1
print("The word {} is find {} times." .format(word, word_count))