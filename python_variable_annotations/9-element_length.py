#!/usr/bin/env python3
"""
functions parameters.
"""
import typing


def element_length(lst: typing.Iterable[typing.Sequence]) -> typing.List[typing.Tuple[typing.Sequence, int]]:
    """
    Return a list of tuples where each tuple.
    """
    return [(i, len(i)) for i in lst]
