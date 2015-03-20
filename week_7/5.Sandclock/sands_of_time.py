n = input("Write N: ")
n = int(n)

number_stars = n
star = "*"
number_dots = 0
dot = "."


while number_stars >= 1:
    print(number_dots*dot + star*number_stars + number_dots*dot)
    number_stars -= 2
    number_dots += 1
    if number_stars == 1:
        break
while number_stars < n + 1:
    print(number_dots*dot + star*number_stars + number_dots*dot)
    number_stars += 2
    number_dots -= 1
