from collections import OrderedDict

class LRUCache:
        
    def __init__(self, cap):
        self.cap = cap
        self.cache = OrderedDict()
        
    def get(self, key):
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]
           
    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.cap:
            self.cache.popitem(last=False)