#!/usr/bin/env python3
"""The basics of async"""
import asyncio
import random


async def wait_random(max_delay: float = 10) -> float:
    """Wait random"""
    await asyncio.sleep(max_delay)
    return random.random() * max_delay


if __name__ == "__main__":
    asyncio.run(wait_random())
