__author__ = "730759980"

from find_max import find_and_remove_max


def test_expected_value() -> None:
    list1: list[int] = [1, 2, 3, 4, 5]
    assert find_and_remove_max(list1) == 5


def test_mutate() -> None:
    list1: list[int] = [1, 2, 3, 4, 5]
    find_and_remove_max(list1)
    assert list1 == [1, 2, 3, 4]


def test_empty_list() -> None:
    list1: list[int] = []
    assert find_and_remove_max(list1) == -1
