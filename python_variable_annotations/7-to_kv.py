#!/usr/bin/env python3
"""
 function to_kv that takes a string.
"""
import typing


def to_kv(k: str, v: typing.Union[int, float]) -> typing.Tuple[str, float]:
    """
    Return a tuple where the second value is v squared.
    """
    return (k, float(v * v))
