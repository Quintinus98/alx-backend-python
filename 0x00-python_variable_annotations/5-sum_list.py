#!/usr/bin/env python3
"""
List of floats
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Returns the sum of float list"""
    sum: float = 0
    for elem in input_list:
        sum += elem
    return sum
