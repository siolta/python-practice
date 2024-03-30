# use an OrderedDict
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """

        self.capacity = int(capacity)
        self._cache = {}
        self.recency = []

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """

        self.recency.insert(0) = key
        return self._cache[key]

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """

        if len(self._cache) < self.capacity:
            self._cache[key] = f"{value}"
            self.recency.insert(0) = key

        if len(self._cache) > self.capacity:
            self._cache.pop(self.recency[capacity - 1])


LRUCache cache = new LRUCache(2)

cache.put(1, 1)
cache.put(2, 2)
cache.get(1)       # returns 1
cache.put(3, 3)    # evicts key 2
cache.get(2)       # returns -1 (not found)
cache.put(4, 4)    # evicts key 1
cache.get(1)       # returns -1 (not found)
cache.get(3)       # returns 3
cache.get(4)       # returns 4
