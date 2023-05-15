#!/usr/bin/env python3
"""
Module defines a Class Server that paginates a database of popular baby names
"""
import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    function takes to arguments and returns a tuple
    containing the start and end index.
    """
    beg, end = 0, 0
    for i in range(page):
        beg = end
        end += page_size

    return (beg, end)


class Server:
    """Class Server to paginate a baby name database.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Caches dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        func takes two arguments and returns requested page.
        """
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0

        d_set = self.dataset()
        d_length = len(d_set)
        try:
            ix = index_range(page, page_size)
            return d_set[ix[0]:ix[1]]
        except IndexError:
            return []
