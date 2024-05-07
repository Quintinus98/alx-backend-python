#!/usr/bin/env python3
"""
Multiple coroutines
"""
import asyncio
from typing import List

task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """wait n"""
    d_list: List[float] = [task_wait_random(max_delay) for _ in range(n)]
    res = await asyncio.gather(*d_list)

    return sorted(res)
