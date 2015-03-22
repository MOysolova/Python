beers = [10, 11]
fries = [1, 5]

def max_score(beers, fries):
    beers = sorted(beers)
    fries = sorted(fries)
    result = 0
    for index in range(0, len(beers)):
        result += beers[index] * fries[index]
    return result
print(max_score(beers, fries))