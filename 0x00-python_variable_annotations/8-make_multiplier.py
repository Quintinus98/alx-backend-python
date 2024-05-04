#!/usr/bin/env python3
"""
Mixed list
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """complex types - functions"""

    def func(val: float) -> Callable[[float], float]:
        return multiplier * val

    return func
