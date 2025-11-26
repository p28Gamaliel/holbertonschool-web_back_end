#!/usr/bin/env python3
"""
functions parameters.
"""
import typing

def element_length(
    lst: typing.Iterable[typing.Sequence]
) -> typing.List[typing.Tuple[typing.Sequence, int]]:
    """
    Return a list of tuples where each tuple contains an element from lst
    and its length.
    """
    return [
        (i, len(i))
        for i in lst
    ]
