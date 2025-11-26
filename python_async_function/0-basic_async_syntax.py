#!/usr/bin/env python3
"""
takes in an integer argument.
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    argument with value igual diez.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
