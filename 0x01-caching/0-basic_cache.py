#!/usr/bin/env python3
""" module contains function for basechacing
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    Function defines a class for caching information in key, value pairs
    """

    def __init__(self):
        """
        Init method initializes the class
        """
        BaseCaching.__init__(self)

    def put(self, key, item):
        """
        instance method Stores a key, value pair
        """
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        """
        method reurns value that is linked to a key
        """
        if key is not None and key in self.cache_data.keys():
            return self.cache_data[key]
        return None
