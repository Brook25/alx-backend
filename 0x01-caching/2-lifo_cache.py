#!/usr/bin/env python3
"""LIFO caching system
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    def __init__(self):
        super().__init__()
        self.discard = None

    def put(self, key, item):
        if not (key and item):
            return
        self.cache_data[key] = item
        if len(self.cache_data) > self.MAX_ITEMS:
            self.cache_data.pop(self.discard)
            print('Discard: {}'.format(self.discard))
        if len(self.cache_data) == self.MAX_ITEMS:
            self.discard = key

    def get(self, key):
        if key:
            return self.cache_data.get(key)


my_cache = LIFOCache()
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
my_cache.put("G", "San Francisco")
my_cache.print_cache()
