"""Utility Functions"""

__author__ = "730759980"


def only_evens(list1: list[int]) -> list[int]:
    # Return a list of only even numbers from the input list
    list2 = []
    for i in list1:
        if i % 2 == 0:
            list2.append(i)
    return list2


def sub(list1: list[int], num1: int, num2: int) -> list[int]:
    # Return a subset of list1 from index num1 to num2 (exclusive)
    if len(list1) == 0 or num1 >= len(list1) or num2 <= 0:
        return []

    list2 = []

    if num1 < 0:
        num1 = 0

    if num2 > len(list1):
        num2 = len(list1)

    for i in range(num1, num2):
        list2.append(list1[i])

    return list2


def add_at_index(list1: list[int], value: int, index: int) -> None:
    # Insert value at the given index, raises IndexError if out of bounds
    if index < 0 or index > len(list1):
        raise IndexError("Index is out of bounds for the input list")
    list1.append(0)

    for i in range(len(list1) - 1, index, -1):
        list1[i] = list1[i - 1]
    list1[index] = value
