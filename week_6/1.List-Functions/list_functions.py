list1 = [1, 2, 3, 4, 5, 66]
list2 = [1, 2, 3, 4, 5, 66]

def head(list1):
    return list1[0]
print(head(list1))

def last(list1):
    return list1[-1]
print(last(list1))

def tail(list1):
    return list1[1:]
print(tail(list1))

def equal_lists(list1, list2):
    if list1 == list2:
        return True
    else:
        return False
print(equal_lists(list1, list2))

def count_item(list1):
    return count_item(5, [list1])
print(count_item(list1))