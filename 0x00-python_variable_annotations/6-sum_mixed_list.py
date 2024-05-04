#!/usr/bin/env python3
"""
Mixed list
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Returns the sum of mixed list (float, int)"""
    sum: float = 0
    for elem in mxd_lst:
        sum += elem
    return sum
