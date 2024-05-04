#!/usr/bin/env python3
"""
Return appropriate types
"""
from typing import Sequence, List, Union, Any


# The types of the elements of the input are not know
def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Safe first element"""
    if lst:
        return lst[0]
    else:
        return None
