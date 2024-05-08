#!/usr/bin/env python3
"""
Measure the runtime
"""
import time
import asyncio


async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime():
    """Measure the runtime"""
    start = time.time()
    comp = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*comp)
    end = time.time()
    total_time = end - start
    return total_time
