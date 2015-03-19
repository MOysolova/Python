n = input("Enter number of buildings: ")
n = int(n)

buildings = []
while n > 0:
    blok = input("Write high: ")
    blok = int(blok)
    buildings += [blok]
    n -= 1
high_max = 0
seen = 0
for index in buildings:
    if index >= high_max:
        seen += 1
        high_max = index

print("Ivancho can see max " + str(seen) + " buildings.")
