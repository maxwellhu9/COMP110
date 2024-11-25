"""EX03 - Various list functions"""

__author__ = "730759980"


def all(a_list: list[int], num1: int) -> bool:
    """
    Check if all elements in the list match the given number.
    If the list is empty, return False.
    """
    # If the list is empty, return False because no values to check.
    if len(a_list) == 0:
        return False

    i = 0
    # Loop through each element in the list
    while i < len(a_list):
        # If an element doesn't match num1, return False right away
        if a_list[i] != num1:
            return False
        i += 1

    # If we get through the whole loop and didn't find a mismatch, return True
    return True


def max(a_list: list[int]) -> int:
    """
    Return the largest number in the list.
    If the list is empty, raise an error.
    """
    # Raise an error if the list is empty
    if len(a_list) == 0:
        raise ValueError("max() arg is an empty List")

    # Assume the first element is the largest
    largest = a_list[0]
    i = 1  # Start loop at 1 since we already took the first element

    # Loop through the rest of the list
    while i < len(a_list):
        # If we find a bigger number, update largest
        if a_list[i] > largest:
            largest = a_list[i]
        i += 1

    # After checking all, return the largest value
    return largest


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """
    Check if two lists are equal in both length and content.
    """
    # If lengths are different, lists can't be equal
    if len(list1) != len(list2):
        return False

    i = 0
    # Compare elements one by one
    while i < len(list1):
        # If any pair of elements is different, return False
        if list1[i] != list2[i]:
            return False
        i += 1

    # If we finish the loop without finding differences, lists are equal
    return True


def extend(list1: list[int], list2: list[int]) -> None:
    """
    Add all elements of list2 to the end of list1.
    """
    # Loop through each element in list2
    i = 0
    while i < len(list2):
        # Append each element from list2 to list1
        list1.append(list2[i])
        i += 1
