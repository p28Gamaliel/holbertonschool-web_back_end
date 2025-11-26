#!/usr/bin/env python3
"""
function make_multiplier that takes a float multiplier as argument.
"""
from typing import Callable


def make_multiplier(miltiplier: float) -> Callable[[float], float]:
    """
    make multiplier.
    """
    def multiplier_func(value: float) -> float:
        """
        multiply values.
        """
        return value * multiplier
    return multiplier_func
