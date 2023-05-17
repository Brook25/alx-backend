#!/usr/bin/env python3
""" module contains a class that defines a Fifo caching system
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    class that defines a FIFO caching system
    """

    def __init__(self):
        """
        Init method that initializes an instance
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """
        method caches a key, value pair
        """
        if key is None or item is None:
            pass
        else:
            data_len = len(self.cache_data)
            if data_len >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
                print("DISCARD: {}".format(self.order[0]))
                del self.cache_data[self.order[0]]
                del self.order[0]
            self.order.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """
        method returns value linked to the given key
        """
        if key is not None and key in self.cache_data.keys():
            return self.cache_data[key]
        return None
