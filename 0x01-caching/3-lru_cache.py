#!/usr/bin/env python3
"""LRU  caching system
"""

from base_caching import BaseCaching

class LRUCache(BaseCaching):
    """LRU caching system
    """
    def __init__(self):
        """Init cache system
        """
        super().__init__()
        self.tracker = []

    def put(self, key, item):
        """Adds data to caching system
        """
        if not (key and item):
            return
        self.cache_data[key] = item
        if key in self.tracker:
            self.tracker.remove(key)
        if len(self.tracker) == self.MAX_ITEMS:
            discard = self.tracker.pop()
            self.cache_data.pop(discard)
            print('DISCARD: {}'.format(discard))
        self.tracker.insert(0, key)

    def get(self, key):
        """Returns value associated with key in cache
        """
        if key:
            return self.cache_data.get(key)
