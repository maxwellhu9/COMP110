"""Linked Lists."""

from __future__ import annotations

__author__ = "730759980"


class Node:
    """Class Node."""

    value: int
    next: Node | None

    def __init__(self, value: int, next: Node | None = None) -> None:
        """Initalizing."""
        self.value = value
        self.next = next


def value_at(head: Node | None, index: int) -> int:
    """Index Value."""
    if head is None:
        raise IndexError("Index is out of bounds on the list.")
    if index == 0:
        return head.value
    return value_at(head.next, index - 1)


def max(head: Node | None) -> int:
    """Max Value."""
    if head is None:
        raise ValueError("Cannot call max with None")
    if head.next is None:
        return head.value

    if head.value > max(head.next):
        return head.value
    else:
        return max(head.next)


def linkify(items: list[int]) -> Node | None:
    """Linking Lists."""
    if not items:
        return None
    return Node(items[0], linkify(items[1:]))


def scale(head: Node | None, factor: int) -> Node | None:
    """Scaling Lists."""
    if head is None:
        return None
    return Node(head.value * factor, scale(head.next, factor))
