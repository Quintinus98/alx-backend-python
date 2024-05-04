#!/usr/bin/env python3
"""
Return appropriate types
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return appropriate types"""
    return [(i, len(i)) for i in lst]
