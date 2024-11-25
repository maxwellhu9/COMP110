"""Mutating functions"""

__author__ = "730759980"


def manual_append(a_list: list[int], num1: int) -> None:
    a_list.append(num1)


def double(a_list: list[int]) -> None:
    i: int = 0

    while i < len(a_list):
        a_list[i] *= 2
        i += 1


list_1 = [1, 2, 3]
list_2 = list_1
double(list_2)

print(list_1)
print(list_2)
