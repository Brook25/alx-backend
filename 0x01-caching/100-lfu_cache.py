#!/usr/bin/env python3
"""LFU  caching system
"""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """LFU caching system
    """
    def __init__(self):
        """Init cache system
        """
        super().__init__()
        self.freq = {}
        self.recency = []

    def put(self, key, item):
        """Adds data to caching system
        """
        if not (key and item):
            return
        self.cache_data[key] = item
        if key in self.recency:
            self.recency.remove(key)
        if len(self.cache_data) > self.MAX_ITEMS:
            min_fr = min(self.freq.values())
            black_lst = [k for k, v in self.freq.items() if v == min_fr]
            for k in self.recency:
                if k in black_lst:
                    self.cache_data.pop(k)
                    self.freq.pop(k)
                    self.recency.remove(k)
                    print('DISCARD: {}'.format(k))
                    break
        self.freq[key] = 1 if key not in self.freq else self.freq[key] + 1
        self.recency.append(key)

    def get(self, key):
        """Returns value associated with key in cache
        """
        if key and key in self.cache_data:
            self.freq[key] += 1
            self.recency.remove(key)
            self.recency.append(key)
            return self.cache_data.get(key)
