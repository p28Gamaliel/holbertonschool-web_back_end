#!/usr/bin/env python3
"""
function make_multiplier that takes a float multiplier as argument.
"""
import typing


def make_multiplier(multiplier: float) -> typing.Callable[[float], float]:
    """
    Return a function that multiplies a float by multiplier.
    """
    return lambda x: x * multiplier
