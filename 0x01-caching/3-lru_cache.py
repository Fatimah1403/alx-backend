#!/usr/bin/python3
""" Python caching systems """
from base_caching import BaseCaching
from collections import OrderedDict


class LIFOCache(BaseCaching):
    """ LIFO caching system """
    def __init__(self):
        """ Initialize class instance. """
        super().__init__()
        self.cache_data = OrderedDict(self.cache_data)

    def put(self, key, item):
        """ Add an item in the cache using LFU"""
        if key and item:
            # check if the number of item is higher than MAX_ITEMS
            self.cache_data[key] = item
            self.cache_data.move_to_end(key)
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                # discard the first item put in cache
                first_key, _ = self.cache_data.popitem(last=False)
                print("DISCARD: {}".format(first_key))

    def get(self, key):  # sourcery skip: assign-if-exp, reintroduce-else
        """ Get an item by key
        """
        if key in self.cache_data:
            self.cache_data.move_to_end(key)
            return self.cache_data.get(key)
        return None
