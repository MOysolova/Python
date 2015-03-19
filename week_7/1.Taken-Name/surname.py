surname_wife = input("Wife name: ")
surname_husband = input("Husband name: ")

def taken_name(surname_husband, surname_wife):
    if surname_wife.find(surname_husband) != -1:
        return True
    else:
        return False

print(taken_name(surname_husband, surname_wife))
