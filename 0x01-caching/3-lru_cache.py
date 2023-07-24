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
        if key and key in self.tracker:
            self.tracker.remove(key)
            self.tracker.insert(0, key)
        return self.cache_data.get(key)

try:

    BaseCaching.MAX_ITEMS = 5
    LRUCache.MAX_ITEMS = 5
    my_cache = LRUCache()
    my_cache.MAX_ITEMS = 5
    prev_key = None

    for i in range(10):
        key = "key-{}".format(i)
        value = "value-{}".format(i)
        if prev_key is not None:
            my_cache.get(prev_key)
        prev_key = key
        my_cache.put(key, value)
        my_cache.print_cache()
    
    my_cache.get("key-0")
    my_cache.get("key-4")
    my_cache.get("key-6")
    my_cache.get("key-7")
    my_cache.print_cache()
    my_cache.put("key-20", "value-20")
    my_cache.put("key-21", "value-21")
    my_cache.put("key-22", "value-22")
    my_cache.print_cache()

except:
    print(sys.exc_info()[1])
