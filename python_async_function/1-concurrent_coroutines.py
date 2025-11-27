#!/usr/bin/env python3
"""
Concurrent coroutines.
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
     async routine called wait_n that takes in 2 int.
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    delays: List[float] = []

    for task in asyncio.as_completed(tasks):
        delay = await task

        if len(delays) == 0:
            delays.append(delay)
        else:
            inserted = False
            for i in range(len(delays)):
                if delay < delays[i]:
                    delays.insert(i, delay)
                    inserted = True
                    break
            if not inserted:
                delays.append(delay)

    return delays
