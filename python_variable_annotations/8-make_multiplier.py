#!/usr/bin/env python3
"""
function make_multiplier that takes a float multiplier as argument.
"""


def make_multiplier(miltiplier: float) -> typing.callable[[float], float]:
    """
    make multiplier.
    """
    def multiply(value: float) -> float:
        """
        multiply values.
        """
        return value * multiplier
    return multiply
