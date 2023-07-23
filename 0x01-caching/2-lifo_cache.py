#!/usr/bin/env python3
"""LIFO caching system
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFO caching system
    """
    def __init__(self):
        """Init cache system
        """
        super().__init__()
        self.discard = None

    def put(self, key, item):
        """Adds data to caching system
        """
        if not (key and item):
            return
        self.cache_data[key] = item
        if len(self.cache_data) > self.MAX_ITEMS:
            self.cache_data.pop(self.discard)
            print('DISCARD: {}'.format(self.discard))
        if len(self.cache_data) == self.MAX_ITEMS:
            self.discard = key

    def get(self, key):
        """Returns value associated with key in cache
        """
        if key:
            return self.cache_data.get(key)
