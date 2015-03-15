string = input("Write something: ")

def vowels(string):
    vowels = "aeiouyAEIOUY"
    counter = 0
    for ch in string:
        if ch in vowels:
            counter += 1
    return ("The number of vowels is: " + str(counter))
print(vowels(string))