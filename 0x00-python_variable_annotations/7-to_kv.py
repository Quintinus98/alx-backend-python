#!/usr/bin/env python3
"""
Mixed list
"""
from typing import List, Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    square: float = v * v
    return (
        k,
        square,
    )
