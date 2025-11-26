#!/usr/bin/env python3
"""
function sum_mixed_list which takes a list mxd_lst of integers and floats.
"""
import typing


def sum_mixed_list(mxd_lst: typing.List[typing.Union[int, float]]) -> float:
    """
    Return the sum of a list of ints and floats as a float.
    """
    return float(sum(mxd_lst))
