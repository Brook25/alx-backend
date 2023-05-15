#!/usr/bin/env python3
"""
This module contains the definition of an index_range helper function
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    function takes two integer arguments and returns a tuple

    """
    beg, end = 0, 0
    for i in range(page):
        beg = end
        end += page_size

    return (beg, end)
