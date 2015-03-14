def marks(points):
    min = 0
    max = 100
    if points >= 0 and points <= 50:
        return "Слаб 2"
    elif points >= 51 and points <= 60:
        return "Среден 3"
    elif points >= 61 and points <= 70:
        return "Добър 4"
    elif points >= 71 and points <= 80:
        return "Много Добър 5"
    elif points >= 81 and points <= 99:
        return "Отличен 6"
    elif points == 100:
        return "Много Отличен 7"
points = input("Enter points: ")
points = int(points)
print(marks(points))
