#!/usr/bin/env python3
"""
imports.
"""
from typing import List
import asyncio
from basic_async_syntax import wait_random

async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    async routine called that takes in 2 int.
    """
    delays = []
    tasks = []

    for _ in range(n):
        tasks.append(asyncio.create_task(wait_random(max_delay)))

    async for task in asyncio.as_completed(tasks):
        delays.append(await task)

    return delays
