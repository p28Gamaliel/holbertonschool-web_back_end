#!/usr/bin/env python3
"""
Simple helper function for pagination
"""


def index_range(page, page_size):
    """
    Return a tuple with start and end index for pagination
    """
    start = (page - 1) * page_size
    end = page * page_size
    return (start, end)
