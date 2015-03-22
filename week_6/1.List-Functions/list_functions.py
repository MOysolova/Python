list1 = [1, 2, 3, 4, 5, 66]
list2 = [1, 2, 3, 4, 5, 66]

# взима списък и връща първият елемент на този списък.
def head(list1):
    return list1[0]
print(head(list1))

# взима списък и връща последния елемент на този списък
def last(list1):
    return list1[-1]
print(last(list1))

# взима списък и връща нов списък, 
# който се състои от всички елементи без първия от първоначалния списъка.
def tail(list1):
    return list1[1:]
print(tail(list1))

# взима два списъка и връща True, ако двата списъка за еднакви.
def equal_lists(list1, list2):
    if list1 == list2:
        return True
    else:
        return False
print(equal_lists(list1, list2))

# взима два аргумента - елемент и списък. 
# Функцията връща броят на срещанията на дадения елемент в дадения списък.
def count_item(list1):
    return count_item(5, [list1])
print(count_item(list1))

# взима два аргумента - цяло число и списък.
# Функцията връща нов списък, който се състои от първите n елемента, 
# където n е цялото число от първия аргумент.
def take(n, items):
    result = []
    for index in range(0, min(n, len(items))):
        result += [items[index]]
    return result

# взима два аргумента - цяло число n и списък.
# Функцията връща нов списък, който представлява стария списък, без първите n елемента.
def drop(n, items):
    result = []
    for index in range(n, len(items)):
        result += [items[index]]
    return result

# взима един списък и го връща обърнат. 
# Последния елемент става първи, предпоследния втори и т.н.
def reverse(items):
    result = []
    last_index = len(items) - 1
    while last_index >= 0:
        result += [items[last_index]]
        last_index -= 1
    return result