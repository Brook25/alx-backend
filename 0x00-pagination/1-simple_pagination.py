#!/usr/bin/env python3
"""Simple pagination"""
import csv
import math
from typing import List


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


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """takes page and page_size and
        returns list of rows from a dataset
        """
        assert type(page_size) is int and page_size > 0
        assert type(page) is int and page > 0
        ix_r = index_range(page, page_size)
        d_set = self.dataset()
        if ix_r[1] > len(d_set):
            return []
        return d_set[ix_r[0]:ix_r[1]]
