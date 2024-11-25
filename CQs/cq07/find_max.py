__author__ = "730759980"


def find_and_remove_max(list1: list[int]) -> int:
    if len(list1) == 0:
        return -1

    largest = list1[0]

    for num in list1:
        if num > largest:
            largest = num

    i = 0

    while i < len(list1):
        if list1[i] == largest:
            list1.pop(i)
        else:
            i += 1

    return largest
