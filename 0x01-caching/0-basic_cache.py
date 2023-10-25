#!/usr/bin/python3
""" a class BasicCache that inherits from
BaseCaching and is a caching system:

"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """return dictionary from the parent class"""
    def put(self, key, item):
        """
        Add item to the cache
        """
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        """
        get item in the cache.
       """
        if key not in self.cache_data:
            return None
        else:
            return self.cache_data.get(key)
