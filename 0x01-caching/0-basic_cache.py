#!/usr/bin/env python3
"""Basic Cache"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """class with methods for Basic caching"""
    def put(self, key, item):
        """puts data into the caching system"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """gets data from the caching system"""
        return self.cache_data.get(key)
