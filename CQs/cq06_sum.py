"""Summing the elements of a list using different loops"""

__author__ = "730759980"


def w_sum(vals: list[float]) -> float:
    sum = 0.0
    i = 0
    while i < len(vals):
        sum += vals[i]
        i += 1
    return sum


def f_sum(vals: list[float]) -> float:
    sum = 0.0
    for i in vals:
        sum += i
    return sum


def f_range_sum(vals: list[float]) -> float:
    sum = 0.0
    for i in range(len(vals)):
        sum += vals[i]
    return sum
