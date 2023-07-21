#!/usr/bin/env python3
"""Simple helper function"""


def index_range(*args, **kwargs) -> tuple:
    """recieves current page and page size
    returns pagination indices.
    """
    if args:
        page, page_size = args
    else:
        page = kwargs.get('page')
        page_size = kwargs.get('page_size')
    return (page_size * page - page_size, page_size * page)
