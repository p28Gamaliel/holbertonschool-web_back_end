#!/usr/bin/env python3
"""
create task_wait_random that returns an asyncio.task.
"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
"""
return an asyncio task that run.
"""
    return asyncio.create_task(wait_random(max_delay))
