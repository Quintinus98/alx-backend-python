#!/usr/bin/env python3
"""
Multiple coroutines
"""
import asyncio
from typing import List

wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    d_list: List[float] = [wait_random(max_delay) for _ in range(n)]
    res = await asyncio.gather(*d_list)

    return sorted(res)
