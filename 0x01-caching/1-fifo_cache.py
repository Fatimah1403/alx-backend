#!/usr/bin/python3
"""
a class FIFOCache that inherits from
BaseCaching and is a caching system
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """"
    self.cache_data - dictionary from the
    parent class BaseCaching
    """
    def __init__(self):
        """
        Initialize
        """
        super().__init__()

    def put(self, key, item):
        """
        Add item to the cache using FIFO
        """
        last_item = 0
        if key or item is None:
            pass
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            self.cache_data.pop(self.last_item)
            print("DISCORD: {}".format(last_item))
        self.cache_data[key] = item

    def get(self, key):
        """
         return the value in self.cache_data linked to key.
        """
        if key in self.cache_data:
            return self.cache_data.get(key)
        return None
