#!/usr/bin/env python3
"""FIFO caching system
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFO caching system
    """
    def __init__(self):
        """initialize FIFOCache instance
        """
        super().__init__()
        self.tracker = []

    def put(self, key, item):
        """update cache system with new value
        """
        if not (key and item):
            return
        self.cache_data[key] = item
        if key not in self.tracker:
            self.tracker.append(key)
        if len(self.cache_data) > self.MAX_ITEMS:
            discarded = self.tracker.pop(0)
            self.cache_data.pop(discarded)
            print('DISCARD: {}'.format(discarded))

    def get(self, key):
        """return value associated with key
        """
        if key:
            return self.cache_data.get(key)



my_cache = FIFOCache()
my_cache.put("A", "Hello")
my_cache.put("B", "World")
my_cache.put("C", "Holberton")
my_cache.put("D", "School")
my_cache.print_cache()
my_cache.put("E", "Battery")
my_cache.print_cache()
my_cache.put("C", "Street")
my_cache.print_cache()
my_cache.put("F", "Mission")
my_cache.print_cache()
