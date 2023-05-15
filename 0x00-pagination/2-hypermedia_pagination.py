#!/usr/bin/env python3
"""
Nodule contains A Class with that creates simple pagination from csv data
"""
import csv
from typing import List
index_range = __import__('0-simple_helper_function').index_range


class Server:
    """Class Server to paginate a database of baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        funciton reads from csv file and returns a dataset.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                read = csv.reader(f)
                d_set = [row for row in read]
            self.__dataset = d_set[1:]

        return self.__dataset

    @staticmethod
    def assert_positive_integer_type(value: int) -> None:
        """
        checks that the value is a positive integer.
        """
        assert type(value) is int and value > 0

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        funciton returns a page of the dataset.
        """
        self.assert_positive_integer_type(page)
        self.assert_positive_integer_type(page_size)
        d_set = self.dataset()
        beg, end = index_range(page, page_size)
        try:
            data = d_set[beg:end]
        except IndexError:
            data = []
        return data

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """
        function returns a page of the dataset.
        """
        tot_pages = len(self.dataset()) // page_size + 1
        data = self.get_page(page, page_size)
        res = {
            "page": page,
            "page_size": page_size if page_size <= len(data) else len(data),
            "total_pages": tot_pages,
            "data": data,
            "prev_page": page - 1 if page > 1 else None,
            "next_page": page + 1 if page + 1 <= tot_pages else None
        }
        return res
