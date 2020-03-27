class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = []

    def get(self, key: int) -> int:
        try:
            self.cache.insert(['key'])
            return self.cache['key']

        except KeyError:
            return -1

    def put(self, key: int, value: int) -> None:
        if len(self.cache) == self.capacity:
            self.cache.pop()
        if self.cache['key']:
            self.cache['key'].del()

        self.cache.insert((key, value))


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


LRU_cache = {
    1: 1,
    2: 2,
    3: 3
}

cap = 3
[(3, 3), (1, 1), (2, 2)]



LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       # returns 1
cache.put(3, 3);    # evicts key 2
cache.get(2);       # returns -1 (not found)
cache.put(4, 4);    # evicts key 1
cache.get(1);       # returns -1 (not found)
cache.get(3);       # returns 3
cache.get(4);       # returns 4
