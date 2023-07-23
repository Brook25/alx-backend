#!/usr/bin/env python3
"""FIFO caching system
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    def __init__(self):
        super().__init__()
        self.tracker = []

    def put(self, key, item):
        self.cache_data[key] = item
        self.tracker.append(key)
        if len(self.cache_data) > self.MAX_ITEMS:
            discarded = self.tracker.pop(0)
            self.cache_data.pop(discarded)
            print('DISCARD: {}'.format(discarded))

    def get(self, key):
        if key:
            return self.cache_data.get(key)
