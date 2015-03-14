n = input("Enter a number: ")
n = int(n)
names = []
count = 1
while count <= n:
    new_name = input("Write a name: ")
    names += [new_name]
    count += 1

names = sorted(names)

for name in names:
    print(name)