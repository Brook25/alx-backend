#!/usr/bin/env python3
""" module contains class LRUcache
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    class defines a caching system
    """
    def __init__(self):
        """
        Init method initializes an instance
        """
        super().__init__()
        self.usage = []

    def put(self, key, item):
        """
        instance method caches a key, value pair
        """
        if key is None or item is None:
            pass
        else:
            datalen = len(self.cache_data)
            if datalen >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
                print("DISCARD: {}".format(self.usage[0]))
                del self.cache_data[self.usage[0]]
                del self.usage[0]
            if key in self.usage:
                del self.usage[self.usage.index(key)]
            self.usage.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """
        method returns value associated with a given key
        """
        if key is not None and key in self.cache_data.keys():
            del self.usage[self.usage.index(key)]
            self.usage.append(key)
            return self.cache_data[key]
        return None
