list1 = [1, 2, 3]
list2 = [0, 0, 1, 2, 3, 5, 6]


def sublist(list1, list2):
    if len(list1) == 0 or len(list2) == 0:
        return True
    if list1 in list2:
        return True
    elif list2 in list1:
        return True
    else:
        return False

print(sublist(list1, list2))
