#!/usr/bin/env python3
"""
Async comprehension
"""
from typing import List

async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """Return 10 random numbers using async generator"""
    result = [res async for res in async_generator()]
    return result
