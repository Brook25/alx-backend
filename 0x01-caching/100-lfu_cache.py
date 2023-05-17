#!/usr/bin/env python3
""" module contains class LFUCache that defines a caching system
"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    class that defines a FIFO caching system
    """

    def __init__(self):
        """
        Init method that initializes an instance
        """
        super().__init__()
        self.usage = []
        self.frequency = {}

    def put(self, key, item):
        """
        method caches a key, value pair
        """
        if key is None or item is None:
            pass
        else:
            datalen = len(self.cache_data)
            if datalen >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
                Lfu = min(self.frequency.values())
                keys = []
                for key, value in self.frequency.items():
                    if value == Lfu:
                        keys.append(key)
                if len(keys) > 1:
                    Lru_lfu = {}
                    for key in keys:
                        Lru_lfu[k] = self.usage.index(key)
                    remove = min(Lru_lfu.values())
                    remove = self.usage[remove]
                else:
                    remove = Lfu_keys[0]

                print("DISCARD: {}".format(discard))
                del self.cache_data[discard]
                del self.usage[self.usage.index(discard)]
                del self.frequency[discard]
            if key in self.frequency:
                self.frequency[key] += 1
            else:
                self.frequency[key] = 1
            if key in self.usage:
                del self.usage[self.usage.index(key)]
            self.usage.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """
        mehtod returns value associated with a given key
        """
        if key is not None and key in self.cache_data.keys():
            del self.usage[self.usage.index(key)]
            self.usage.append(key)
            self.frequency[key] += 1
            return self.cache_data[key]
        return None
