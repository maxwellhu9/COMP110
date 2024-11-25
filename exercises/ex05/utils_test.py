"""Utility Unit Tests"""

__author__ = "730759980"

from exercises.ex05.utils import only_evens
from exercises.ex05.utils import sub
from exercises.ex05.utils import add_at_index

# only_evens test cases


def test_only_evens_empty() -> None:
    """Test that only_evens returns an empty list when given an empty list"""
    assert only_evens([]) == []


def test_only_evens_all_odds() -> None:
    """Test that only_evens returns an empty list when all numbers are odd"""
    assert only_evens([1, 3, 5, 7]) == []


def test_only_evens_mixed() -> None:
    """Test that only_evens returns only the even numbers from a mixed list"""
    assert only_evens([1, 2, 3, 4]) == [2, 4]


# sub test cases


def test_sub_empty() -> None:
    """Test that sub returns an empty list when given an empty list."""
    assert sub([], 0, 3) == []


def test_sub_negative_start() -> None:
    """Test that sub handles a negative start index correctly."""
    assert sub([10, 20, 30, 40], -1, 3) == [10, 20, 30]


def test_sub_out_of_bounds() -> None:
    """Test that sub handles end index greater than the list length."""
    assert sub([10, 20, 30, 40], 1, 6) == [20, 30, 40]


# add_at_index cases


def test_add_at_index_valid() -> None:
    """Test if inserts correctly at a valid index."""
    list1 = [1, 2, 4]
    add_at_index(list1, 3, 2)
    assert list1 == [1, 2, 3, 4]


def test_add_at_index_out_of_bounds() -> None:
    """Test if inserts correctly at a valid index."""
    list1 = [2, 2, 4]
    add_at_index(list1, 3, 1)
    assert list1 == [2, 3, 2, 4]


def test_add_at_index_append() -> None:
    """Test if appends the element at the end of list when  index is len(list)."""
    list2 = [1, 2, 3]
    add_at_index(list2, 4, 3)
    assert list2 == [1, 2, 3, 4]
