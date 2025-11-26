#!/usr/bin/env python3
"""
imports.
"""
from typing import List
import asyncio
from basic_async_syntax import wait_random

async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    async routine called wait_n that takes in 2 int.
    """
    delays = []
    tasks = []

    for _ in range(n):
        tasks.append(asyncio.create_task(wait_random(max_delay)))

    for t in tasks:
        d = await t
        delays.append(d)

        for i in range(len(delays)-1):
            if delays[i] > delays[-1]:
                delays[i], delays[-1] = delays[-1], delays[i]

    return delays
