# !/usr/bin/env python3
""" BaseCaching module using FIFO algorithm """
from collections import OrderedDict


BaseCaching = __import__('base_caching').BaseCaching


# Create a class LIFOCache that inherits from BaseCaching system:

# You must use self.cache_data - dictionary from the base BaseCaching
# You can overload def __init__(self)
# def put(self, key, item):
# assign to the dictionary self.cache_data the item value for the key.
# If key or item is None, this method should not do anything.
# If items in self.cache_data is higher that BaseCaching.MAX_ITEMS:
# you must discard the least recently used item (LRU algorithm)
# print DISCARD: with the key discarded and following by a new line
# def get(self, key):
# Must return the value in self.cache_data linked to key.
# If key is None return None.


class MRUCache(BaseCaching):
    """ Caching System """

    def __init__(self):
        """ Initiliaze
        """
        super().__init__()
        self.cache_data = OrderedDict(self.cache_data)
        self.freq = {}

    def put(self, key, item):
        """
        Adding item to the cache
        """
        if key and item:
            if key in self.cache_data:
                self.frequency_update(self, key)
                self.cache_data[key] = item
                return
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # getting the lowest frequency frpm frequency dict
                discarded_items = [
                    (self.freq[key], key) for key in self.freq.keys()
                ]

                deleted_items = sorted(discarded_items)[0][1]
                del self.cache_data[deleted_items]
                del self.freq[deleted_items]
                print("DISCARD: {}".format(deleted_items))
                # add new items
                self.cache_data[key] = item
                self.freq[key] = 1
            self.cache_data[key] = item
            self.freq[key] = 1

    def get(self, key):
        """Get an item by key"""
        if key in self.cache_data:
            # increase the frequency for that key
            self.frequency_update(self, key)
            return self.cache_data.get(key)
        return None

    @staticmethod
    def frequency_update(self, key):
        """ updating the frequency of the dict"""
        self.freq[key] += 1
